from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Dict, Iterator, Tuple

import torch
import torchaudio
import torchaudio.functional as AF
import torch.nn.functional as F

from models import ConvAudioClassifier


MODEL_DIR = Path(__file__).resolve().parent / "saved_models"
CHECKPOINT_PATH = MODEL_DIR / "best_model.pt"
CLASS_MAPPING_PATH = MODEL_DIR / "class_mapping.json"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
AUDIO_EXTENSIONS = {".wav", ".mp3", ".flac", ".ogg", ".m4a", ".aac"}

_MODEL_CACHE: ConvAudioClassifier | None = None
_CLASS_NAMES: Tuple[str, ...] | None = None
_METADATA: Dict[str, float | int] | None = None


def _load_checkpoint() -> Dict:
    if not CHECKPOINT_PATH.exists():
        raise FileNotFoundError(f"Checkpoint not found at {CHECKPOINT_PATH}")
    try:
        payload = torch.load(str(CHECKPOINT_PATH), map_location=DEVICE, weights_only=False)
    except TypeError:
        payload = torch.load(str(CHECKPOINT_PATH), map_location=DEVICE)
    required = {"model_state", "class_names", "metadata"}
    missing = required - payload.keys()
    if missing:
        raise KeyError(f"Checkpoint missing required keys: {missing}")
    return payload


def _load_class_names() -> Tuple[str, ...]:
    global _CLASS_NAMES
    if _CLASS_NAMES is not None:
        return _CLASS_NAMES
    if CLASS_MAPPING_PATH.exists():
        mapping = json.loads(CLASS_MAPPING_PATH.read_text(encoding="utf-8"))
        _CLASS_NAMES = tuple(mapping[str(idx)] for idx in sorted(map(int, mapping.keys())))
    else:
        checkpoint = _load_checkpoint()
        _CLASS_NAMES = tuple(checkpoint["class_names"])
    return _CLASS_NAMES


def _ensure_model() -> Tuple[ConvAudioClassifier, Tuple[str, ...], Dict[str, float | int]]:
    global _MODEL_CACHE, _METADATA
    class_names = _load_class_names()
    if _MODEL_CACHE is None or _METADATA is None:
        checkpoint = _load_checkpoint()
        metadata = checkpoint.get("metadata", {})
        n_mels = int(metadata.get("n_mels", 128))
        model = ConvAudioClassifier(n_mels=n_mels, n_classes=len(class_names))
        model.load_state_dict(checkpoint["model_state"])
        model.to(DEVICE)
        model.eval()
        _MODEL_CACHE = model
        _METADATA = metadata
    return _MODEL_CACHE, class_names, _METADATA


def _decode_with_ffmpeg(path: Path, target_sr: int) -> torch.Tensor:
    ffmpeg_bin = shutil.which("ffmpeg")
    if ffmpeg_bin is None:
        raise RuntimeError("FFmpeg binary not found on PATH. Install FFmpeg to decode this file.")
    cmd = [
        ffmpeg_bin,
        "-v",
        "error",
        "-i",
        str(path),
        "-f",
        "f32le",
        "-ac",
        "1",
        "-ar",
        str(target_sr),
        "pipe:1",
    ]
    result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not result.stdout:
        raise RuntimeError(f"FFmpeg produced no data for {path}")
    waveform = torch.frombuffer(result.stdout, dtype=torch.float32).clone().view(1, -1)
    return waveform


def _load_waveform(path: Path, sample_rate: int, clip_duration: float) -> torch.Tensor:
    try:
        waveform, sr = torchaudio.load(str(path))
    except RuntimeError as exc:
        if path.suffix.lower() in AUDIO_EXTENSIONS:
            waveform = _decode_with_ffmpeg(path, sample_rate)
            sr = sample_rate
        else:
            raise RuntimeError(f"Unable to read audio file {path}: {exc}") from exc

    if waveform.dim() == 1:
        waveform = waveform.unsqueeze(0)
    if waveform.size(0) > 1:
        waveform = waveform.mean(dim=0, keepdim=True)
    if sr != sample_rate:
        waveform = AF.resample(waveform, sr, sample_rate)

    target_samples = int(sample_rate * clip_duration)
    num_samples = waveform.size(1)
    if num_samples < target_samples:
        pad_amount = target_samples - num_samples
        waveform = F.pad(waveform, (0, pad_amount))
    elif num_samples > target_samples:
        offset = (num_samples - target_samples) // 2
        waveform = waveform[:, offset : offset + target_samples]
    return waveform


def _waveform_to_spec(waveform: torch.Tensor, sample_rate: int, n_mels: int) -> torch.Tensor:
    mel_transform = torchaudio.transforms.MelSpectrogram(
        sample_rate=sample_rate,
        n_fft=2048,
        hop_length=512,
        n_mels=n_mels,
        power=2.0,
    )
    db_transform = torchaudio.transforms.AmplitudeToDB(top_db=80.0)
    spec = mel_transform(waveform)
    spec = db_transform(spec)
    spec = spec - spec.mean()
    spec = spec / (spec.std() + 1e-6)
    return spec


@contextmanager
def _temporary_audio_file(file_or_data, is_widget_data: bool) -> Iterator[Path]:
    if is_widget_data:
        raw_bytes = file_or_data.getvalue()
        suffix = ".wav"
    else:
        raw_bytes = file_or_data.read()
        file_or_data.seek(0)
        suffix = str(Path(getattr(file_or_data, "name", "upload.wav")).suffix) or ".wav"

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(raw_bytes)
        tmp_path = Path(str(tmp.name))
    try:
        yield tmp_path
    finally:
        tmp_path.unlink(missing_ok=True)


def predict_audio_class(audio_file, is_widget_data: bool = False) -> str:
    model, class_names, metadata = _ensure_model()
    sample_rate = int(metadata.get("sample_rate", 22050))
    clip_duration = float(metadata.get("clip_duration", 5.0))
    n_mels = int(metadata.get("n_mels", 128))

    with _temporary_audio_file(audio_file, is_widget_data) as path:
        waveform = _load_waveform(path, sample_rate, clip_duration)

    spec = _waveform_to_spec(waveform, sample_rate, n_mels)
    spec = spec.unsqueeze(0).to(DEVICE)

    with torch.no_grad():
        logits = model(spec)
        probs = torch.softmax(logits, dim=1)[0]
        predicted_idx = probs.argmax().item()

    return class_names[predicted_idx]


def get_supported_ragas() -> Tuple[str, ...]:
    return _load_class_names()
