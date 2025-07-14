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
        "id": 1,
        "audio_path": "Raga Mohanam_ Arohanam, Avarohanam and Alapana  Raga Surabhi.mp3",
        "answer": "Mohanam",
        "options": ["Mohanam", "Kalyani", "Todi", "Kharaharapriya"]
    },
    {
        "id": 2,
        "audio_path": "Raga Kalyani_ Arohanam, Avarohanam and Alapana  Raga Surabhi.mp3",
        "answer": "Kalyani",
        "options": ["Shankarabharanam", "Kalyani", "Bhairavi", "Hamsadhwani"]
    }
]

# Initialize session state
if "question_id" not in st.session_state:
    st.session_state.question_id = random.choice([q["id"] for q in quiz_data])
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Get current question by ID
current_question = next(q for q in quiz_data if q["id"] == st.session_state.question_id)

# Show question
st.audio(current_question["audio_path"])
user_answer = st.radio("Which raga is this?", current_question["options"], key="user_answer")

# Submit Answer
if st.button("Submit Answer"):
    st.session_state.submitted = True

if st.session_state.submitted:
    if user_answer == current_question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer is **{current_question['answer']}**.")

# Try Another
if st.button("Try Another"):
    # Choose a new question ID that's different
    new_id = st.session_state.question_id
    while new_id == st.session_state.question_id:
        new_id = random.choice([q["id"] for q in quiz_data])
    
    st.session_state.question_id = new_id
    st.session_state.submitted = False
    st.session_state.user_answer = None  # Reset the radio button
    st.experimental_rerun()
