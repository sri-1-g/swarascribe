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

# Initialize session state values
if "question_id" not in st.session_state:
    st.session_state.question_id = random.choice([q["id"] for q in quiz_data])
if "quiz_step" not in st.session_state:
    st.session_state.quiz_step = 0
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None

def load_question():
    return next(q for q in quiz_data if q["id"] == st.session_state.question_id)

def pick_new_question():
    current_id = st.session_state.question_id
    other_questions = [q for q in quiz_data if q["id"] != current_id]
    if other_questions:
        new_q = random.choice(other_questions)
        st.session_state.question_id = new_q["id"]
    # Reset answer & step
    st.session_state.user_answer = None
    st.session_state.quiz_step = 0

q = load_question()

if st.session_state.quiz_step == 0:
    # Show question
    st.audio(q["audio_path"])
    st.session_state.user_answer = st.radio(
        "Which raga is this?",
        q["options"],
        index=q["options"].index(st.session_state.user_answer) if st.session_state.user_answer in q["options"] else 0,
        key="answer_radio"
    )
    if st.button("Submit Answer"):
        if st.session_state.user_answer is None:
            st.warning("Please select an answer before submitting.")
        else:
            st.session_state.quiz_step = 1
            st.experimental_rerun()

elif st.session_state.quiz_step == 1:
    # Show result
    if st.session_state.user_answer == q["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Incorrect. The correct answer is **{q['answer']}**.")

    if st.button("Try Another"):
        pick_new_question()
        st.experimental_rerun()
