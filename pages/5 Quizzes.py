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

# Choose question only once
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(quiz_data)

q = st.session_state.current_question

# Display the current question
st.audio(q["audio_path"])
user_answer = st.radio("Which raga is this?", q["options"], key="user_response")

# Submit button
if st.button("Submit Answer"):
    if user_answer == q["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer is **{q['answer']}**.")

    # Optionally allow user to try another question
    if st.button("Try Another"):
        st.session_state.current_question = random.choice(quiz_data)
        st.experimental_rerun()
