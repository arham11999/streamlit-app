import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("QUIZ_KEY")

st.set_page_config(layout="wide")

st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #0E1117, #1C1F26);
}

h1 {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
}

.stTextInput > div > div > input {
    background-color: #1C1F26;
    color: white;
    border-radius: 12px;
    border: 1px solid #6C63FF;
    padding: 12px;
}

.stButton > button {
    background-color: #6C63FF;
    color: white;
    border-radius: 12px;
    height: 45px;
    width: 100%;
    font-size: 16px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #5848e5;
    color: white;
}

.stFileUploader {
    background-color: #1C1F26;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #6C63FF;
}
</style>
""", unsafe_allow_html=True)

st.header("QUIZ GENERATOR")
st.divider()

if "questions" not in st.session_state:
    st.session_state.questions = None


data = st.text_area("ENTER TOPIC OR CONTENT HERE", height=300)
files = st.file_uploader("UPLOAD FILE (Optional)")
generate_button = st.button("SUBMIT")


if generate_button:

    user_text = None

    if data.strip() != "" and files is None:
        user_text = data

    elif files is not None and data.strip() == "":
        user_text = files.read().decode("utf-8")

    elif files is not None and data.strip() != "":
        user_text = data + "\n" + files.read().decode("utf-8")

    if not user_text:
        st.warning("Please enter text or upload a file.")
    else:
        try:
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=f"""
                Generate 15 questions:
                - 5 Easy
                - 5 Medium
                - 5 Hard

                Topic: {user_text}

                Format:
                - Fill in the blanks
                - Mention serial number
                - DO NOT include answers
                """
            )

            st.session_state.questions = response.text

        except Exception as e:
            st.error(f"API Error: {e}")


if st.session_state.questions:
    with st.container(border=True):
        st.text(st.session_state.questions)


answers = st.text_area("ENTER YOUR ANSWERS HERE")
check_button = st.button("LET'S CHECK YOUR ANSWERS")


if check_button:

    if not answers.strip():
        st.warning("Please enter your answers first.")
    elif not st.session_state.questions:
        st.warning("Generate questions first.")
    else:
        try:
            client = genai.Client(api_key=api_key)

            response1 = client.models.generate_content(
                model="gemini-1.5-flash",
                contents=f"""
                Compare the user's answers:

                {answers}

                With the correct answers of these questions:

                {st.session_state.questions}

                Instructions:
                - Treat given answers as final answers
                - Give score out of 10
                - Provide short feedback
                """
            )

            with st.container(border=True):
                st.text(response1.text)
                st.success("THANK YOU")

        except Exception as e:
            st.error(f"API Error: {e}")