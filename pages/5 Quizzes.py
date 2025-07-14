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

# ---------- Quiz 1: Guess the Raga from Audio ----------
if quiz_type == "1. Guess the Raga from Aro/Avo Audio":
    st.header("🎧 Guess the Raga from Arohanam and Avarohanam")
    st.write("Listen to the audio and select the correct raga.")

    quiz_data_1 = [
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

    # Init session state variables for Quiz 1
    if "current_question_1" not in st.session_state:
        st.session_state.current_question_1 = random.choice(quiz_data_1)
        st.session_state.submitted_1 = False

    q1 = st.session_state.current_question_1

    st.audio(q1["audio_path"])
    user_answer_1 = st.radio("Which raga is this?", q1["options"], key="user_response_1")

    if st.button("Submit Answer", key="submit_1") and not st.session_state.submitted_1:
        if user_answer_1 == q1["answer"]:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. The correct answer is **{q1['answer']}**.")
        st.session_state.submitted_1 = True

    if st.session_state.submitted_1:
        if st.button("Try Another", key="try_another_1"):
            st.session_state.current_question_1 = random.choice(quiz_data_1)
            st.session_state.submitted_1 = False
            st.experimental_rerun()


# ---------- Quiz 4: Multiple Choice - Raga Facts ----------
elif quiz_type == "4. Multiple Choice - Raga Facts":
    st.header("📚 Raga Trivia Quiz")
    st.write("Test your knowledge! Pick the correct answer and click Submit. Then try another question.")

    quiz_data_4 = [
        {
            "question": "Which Melakarta number is Kalyani?",
            "answer": "65",
            "options": ["65", "29", "8", "36"]
        },
        {
            "question": "Which raga is the 22nd Melakarta?",
            "answer": "Kharaharapriya",
            "options": ["Kharaharapriya", "Harikambhoji", "Natabhairavi", "Todi"]
        },
        {
            "question": "What is the Arohanam (ascending scale) of Raga Mohanam?",
            "answer": "S R2 G3 P D2 S",
            "options": ["S R2 G3 P D2 S", "S R1 G2 M1 P D1 N2 S", "S G3 M2 P N3 S", "S R2 M1 P D2 N2 S"]
        },
        {
            "question": "Which raga is commonly used to invoke Lord Ganesha?",
            "answer": "Hamsadhwani",
            "options": ["Hamsadhwani", "Bhairavi", "Kalyani", "Mohanam"]
        },
        {
            "question": "Which raga corresponds to Melakarta number 15?",
            "answer": "Mayamalavagowla",
            "options": ["Mayamalavagowla", "Harikambhoji", "Natabhairavi", "Kalyani"]
        },
        {
            "question": "What is the Avarohanam (descending scale) of Raga Kalyani?",
            "answer": "S N3 D2 P M2 G3 R2 S",
            "options": ["S N3 D2 P M2 G3 R2 S", "S R2 G3 M1 P D2 N3 S", "S D2 P M1 G3 R2 S", "S N2 D1 P M1 G2 R1 S"]
        },
        {
            "question": "Which Melakarta raga is number 29?",
            "answer": "Shankarabharanam",
            "options": ["Shankarabharanam", "Kharaharapriya", "Natabhairavi", "Todi"]
        },
        {
            "question": "Which raga uses the notes S R2 G2 M1 P D2 N2 S?",
            "answer": "Harikambhoji",
            "options": ["Harikambhoji", "Kalyani", "Bhairavi", "Todi"]
        },
        {
            "question": "Which janya (derived) raga comes from Mayamalavagowla?",
            "answer": "Hamsadhwani",
            "options": ["Hamsadhwani", "Kalyani", "Bilahari", "Charukesi"]
        }
    ]

    # Init session state variables for Quiz 4
    if "current_question_4" not in st.session_state:
        st.session_state.current_question_4 = random.choice(quiz_data_4)
        st.session_state.submitted_4 = False
        st.session_state.feedback_4 = ""

    q4 = st.session_state.current_question_4

    st.write(f"**Question:** {q4['question']}")
    user_answer_4 = st.radio("Choose your answer:", q4["options"], key="user_response_4")

    if st.button("Submit Answer", key="submit_4") and not st.session_state.submitted_4:
        if user_answer_4 == q4["answer"]:
            st.session_state.feedback_4 = "✅ Correct!"
        else:
            st.session_state.feedback_4 = f"❌ Incorrect. The correct answer is {q4['answer']}."
        st.session_state.submitted_4 = True

    if st.session_state.submitted_4:
        st.write(st.session_state.feedback_4)

    if st.session_state.submitted_4:
        if st.button("Try Another One", key="try_another_4"):
            st.session_state.current_question_4 = random.choice(quiz_data_4)
            st.session_state.submitted_4 = False
            st.session_state.feedback_4 = ""
            st.experimental_rerun()


# Optionally: you can add skeleton placeholders for quizzes 2 and 3 here

