import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_input("Enter text")

language = st.selectbox(
    "Select target language",
    ("hindi","french","spanish","german","japanese")
)

if st.button("Translate"):
    translated = GoogleTranslator(source='auto', target=language).translate(text)
    st.write("Translated Text:")
    st.success(translated)