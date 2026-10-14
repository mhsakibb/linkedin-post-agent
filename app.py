from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

load_dotenv()

st.title("LinkedIn Post Generator AI Agent")

topic = st.text_input("Enter Topic")

language = st.selectbox(
    "Select Language",
    ["English", "Bengali"]
)

tone = st.selectbox(
    "Select Tone",
    ["Professional", "Inspirational", "Storytelling"]
)

length = st.selectbox(
    "Select Length",
    ["Short", "Medium", "Long"]
)

if st.button("Generate Post"):

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.8
    )

    prompt = f"""
    You are a professional LinkedIn post writer.

    Topic: {topic}
    Language: {language}
    Tone: {tone}
    Length: {length}

    Write a professional LinkedIn post.

    Requirements:
    - 2-4 paragraphs
    - Engaging hook
    - Professional style
    - End with a question
    - Add 5 hashtags
    """

    response = llm.invoke(prompt)

    st.subheader("Generated LinkedIn Post")

    st.write(response.content)

