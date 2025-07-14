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


# Quiz 4
if quiz_type == "4. Multiple Choice - Raga Facts":
    st.header("📚 Raga Trivia Quiz")
    st.write("Test your knowledge! Pick the correct answer and click Submit. Then try another question.")

    quiz_data = [
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

    if "trivia_question" not in st.session_state:
        st.session_state.trivia_question = random.choice(quiz_data)
        st.session_state.trivia_submitted = False
        st.session_state.trivia_feedback = ""

    q = st.session_state.trivia_question

    st.write(f"**Question:** {q['question']}")
    user_answer = st.radio("Choose your answer:", q["options"], key="trivia_answer")

    if st.button("Submit Answer") and not st.session_state.trivia_submitted:
        if user_answer == q["answer"]:
            st.session_state.trivia_feedback = "✅ Correct!"
        else:
            st.session_state.trivia_feedback = f"❌ Incorrect. The correct answer is {q['answer']}."
        st.session_state.trivia_submitted = True

    if st.session_state.trivia_submitted:
        st.write(st.session_state.trivia_feedback)

    if st.button("Try Another One"):
        st.session_state.trivia_question = random.choice(quiz_data)
        st.session_state.trivia_submitted = False
        st.session_state.trivia_feedback = ""
        st.experimental_rerun()
