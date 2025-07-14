import streamlit as st
import random

st.set_page_config(page_title="Carnatic Raga Quizzes", layout="centered")

st.image("quizzes.png")
st.write("Test your knowledge of Carnatic ragas with different types of quizzes!")

quiz_type = st.radio(
    "Select a Quiz Type:",
    [
        "1. Guess the Raga from Aro/Avo Audio",
        "2. Identify the Raga from Swaras",
        "3. Match Composition to Raga",
        "4. Multiple Choice - Raga Facts"
    ]
)
# Quiz 1: Guess the Raga from Audio
if quiz_type == "1. Guess the Raga from Aro/Avo Audio":
    st.header("🎧 Guess the Raga from Arohanam and Avarohanam")
    st.write("Listen to the audio and select the correct raga.")

    quiz_data = [
        {
            "audio_path": "audio/mohanam_ar_avo.mp3",
            "answer": "Mohanam",
            "options": ["Mohanam", "Kalyani", "Todi", "Kharaharapriya"]
        },
        {
            "audio_path": "audio/kalyani_ar_avo.mp3",
            "answer": "Kalyani",
            "options": ["Shankarabharanam", "Kalyani", "Bhairavi", "Hamsadhwani"]
        }
    ]

    q = random.choice(quiz_data)
    st.audio(q["audio_path"])
    user_answer = st.radio("Which raga is this?", q["options"])
    if st.button("Submit Answer"):
        if user_answer == q["answer"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. The correct answer is **{q['answer']}**.")
