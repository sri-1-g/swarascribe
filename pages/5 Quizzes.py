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
    st.write("Listen to each audio clip and select the correct raga.")

    quiz_data = [
        {
            "audio_path": "Raga Mohanam_ Arohanam, Avarohanam and Alapana  Raga Surabhi.mp3",
            "answer": "Mohanam",
            "options": ["Mohanam", "Kalyani", "Todi", "Kharaharapriya"]
        },
        {
            "audio_path": "Raga Kalyani_ Arohanam, Avarohanam and Alapana  Raga Surabhi.mp3",
            "answer": "Kalyani",
            "options": ["Shankarabharanam", "Kalyani", "Bhairavi", "Hamsadhwani"]
        }
    ]

    # Store responses
    responses = []

    for i, q in enumerate(quiz_data):
        st.subheader(f"Question {i + 1}")
        st.audio(q["audio_path"])
        user_answer = st.radio(
            f"Which raga is this? (Q{i+1})", q["options"], key=f"audio_q{i}"
        )
        responses.append((user_answer, q["answer"]))

    if st.button("Submit All Answers"):
        score = 0
        for i, (user_answer, correct_answer) in enumerate(responses):
            if user_answer == correct_answer:
                st.success(f"✅ Question {i+1}: Correct!")
                score += 1
            else:
                st.error(f"❌ Question {i+1}: Incorrect. Correct answer: **{correct_answer}**.")
        st.info(f"Your total score: {score} / {len(responses)}")
