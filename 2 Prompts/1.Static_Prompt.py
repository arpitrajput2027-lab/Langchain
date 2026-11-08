from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash')



st.header("Research Paper Summarizer")
user_input = st.text_input("Enter Your Research paper Query...")
if st.button("Summarize"):
    response = model.invoke(user_input)
    st.write(response.content[0]["text"])