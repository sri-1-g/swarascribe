import streamlit as st

from predict import get_supported_ragas, predict_audio_class

st.set_page_config(layout="wide")
st.markdown(
    """
<style>
.st-emotion-cache-9s49fs, .st-emotion-cache-a6n1w7 {
    color: #fad07d !important;
}
</style>
""",
    unsafe_allow_html=True,
)
st.sidebar.image("swara.png")

RAGA_DETAILS = {
    "Mohanam": {
        "overview": (
            "Mohanam is a bright pentatonic (audava-audava) janya of the 28th Melakarta Harikambhoji. "
            "It skips madhyamam and nishadam, creating a sparkling canvas that is identical to the Hindustani raga Bhoop."
        ),
        "arohana": "S R2 G3 P D2 S",
        "avarohana": "S D2 P G3 R2 S",
        "mood": "Celebratory, devotional, and uplifting — often sung to open a concert.",
        "highlights": [
            "Pentatonic scale that highlights the symmetry between arohana and avarohana.",
            "Graceful slides between R2–G3 and G3–P define many signature phrases.",
            "Popular varnams and kritis include 'Nanu Palimpa' and 'Kapali'.",
        ],
        "compositions": [
            "Tyagaraja – 'Nanu Palimpa'",
            "Muthuswami Dikshitar – 'Kapali'",
            "Papanasam Sivan – 'Kapali'",
        ],
    },
    "Kanada": {
        "overview": (
            "Kanada is a vakra janya of the 22nd Melakarta Kharaharapriya. "
            "It luxuriates in gamakas around the madhyamam and rishabham, lending a dusk-like depth similar to the Hindustani Darbari Kanada."
        ),
        "arohana": "S R2 M1 G3 M1 P D2 N2 S",
        "avarohana": "S N2 D2 P M1 G3 M1 R2 S",
        "mood": "Grand, reflective, and slightly meditative — suited for late-evening concerts.",
        "highlights": [
            "Vakra movement with repeated M1–G3 oscillations gives Kanada its identity.",
            "Prefers elongated kampita gamakas, especially on R2 and D2.",
            "Pairs beautifully with compositions that emphasize bhakti and sringara rasas.",
        ],
        "compositions": [
            "Tyagaraja – 'Eti Janmamidi'",
            "Syama Sastri – 'Kanakasaila'",
            "Papanasam Sivan – 'Srinivasa Tiruvengadamudaiyane'",
        ],
    },
    "Saveri": {
        "overview": (
            "Saveri is an ancient janya of the 15th Melakarta Mayamalavagowla. "
            "It uses a bhashanga scale with Shuddha Rishabham in the ascent and Kakali Nishadam in the descent, producing a solemn aura."
        ),
        "arohana": "S R1 M1 P D1 S",
        "avarohana": "S N3 D1 P M1 G3 R1 S",
        "mood": "Grave and introspective, often chosen for devotional kritis and elaborate alapana.",
        "highlights": [
            "Audava–sampurna structure that omits ghandharam and nishadam in the ascent.",
            "Powerful phrases hover around R1 and D1, demanding delicate intonation.",
            "Works beautifully with tanam and neraval explorations thanks to its strong gamaka canvas.",
        ],
        "compositions": [
            "Muthuswami Dikshitar – 'Darini Telusukonti'",
            "Tyagaraja – 'Rama Bhirama'",
            "Gopalakrishna Bharathi – 'Sabhapatikku'",
        ],
    },
}


def render_raga_details(raga: str) -> None:
    st.success(f"This song is predicted to be in the ragam: {raga}")
    details = RAGA_DETAILS.get(raga)
    if not details:
        st.info("Detailed profile for this raga is coming soon.")
        return

    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Scale")
        st.markdown(
            f"**Arohana**: {details['arohana']}  \n**Avarohana**: {details['avarohana']}"
        )
        st.subheader("Overview")
        st.write(details["overview"])
        st.subheader("Musical Highlights")
        for bullet in details["highlights"]:
            st.markdown(f"- {bullet}")
        st.subheader("Popular Compositions")
        for item in details["compositions"]:
            st.markdown(f"- {item}")
    with c2:
        st.image("spec.png")
        st.subheader("Mood & Usage")
        st.write(details["mood"])
        st.markdown("#### Listening Tips")
        st.markdown(
            "- Focus on the signature gamakas in the madhyamam region.\n"
            "- Sing or play long phrases rather than short jumps to mimic concert phrasings.\n"
            "- Compare with the Hindustani counterpart to appreciate the stylistic differences."
        )


col1, col2, col3 = st.columns(3)
with col2:
    st.image("upload.png")

supported_ragas = get_supported_ragas()
st.write(
    "The integrated Raga_v4 classifier currently recognizes the following ragams: "
    + ", ".join(supported_ragas)
    + "."
)

uploaded_file = st.file_uploader("Choose a file", type=["wav", "mp3", "m4a", "flac", "ogg", "aac"])
st.divider()
audio_value = st.audio_input("Record a voice message")

if st.button("Analyze"):
    source = None
    is_widget = False
    if uploaded_file:
        source = uploaded_file
    elif audio_value:
        source = audio_value
        is_widget = True

    if source is None:
        st.warning("Please upload or record audio before running the analysis.")
    else:
        try:
            prediction = predict_audio_class(source, is_widget_data=is_widget)
        except Exception as exc:
            st.error(f"Unable to analyze the audio clip: {exc}")
        else:
            render_raga_details(prediction)
