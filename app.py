import streamlit as st
from main import run_pipeline

st.title("Hindi/Marathi Text Simplifier")

text = st.text_area("Enter text")

if st.button("Simplify"):
    result = run_pipeline(text)
    st.write(result)