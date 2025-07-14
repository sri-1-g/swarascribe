import streamlit as st
import random

st.set_page_config(page_title="Carnatic Raga Quizzes", layout="centered")

st.title("🎵 Carnatic Music Raga Quizzes")

quiz_type = st.sidebar.selectbox(
    "Choose a Quiz Type:",
    [
        "1. Guess the Raga from Aro/Avo Audio",
        "2. Identify the Raga from Swaras",
        "3. Match Composition to Raga",
        "4. Multiple Choice - Raga Facts"
    ]
)
