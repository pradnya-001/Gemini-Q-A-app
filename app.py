from dotenv import load_dotenv # type: ignore
load_dotenv()  # Load environment variables from .env.

import streamlit as st # type: ignore
import os
import textwrap
import google.generativeai as genai # type: ignore
from IPython.display import Markdown # type: ignore


def to_markdown(text):
    text = text.replace('•', ' *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


# Load the API key from environment variables
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Google API key not found. Please set it in the .env file.")


def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    if input_text:
        response = get_gemini_response(input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please enter a question.")
