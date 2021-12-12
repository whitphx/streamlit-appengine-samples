import streamlit as st

st.title("App Engine sample app")

uploaded_file = st.file_uploader("Upload some file")
if uploaded_file:
    st.write(f"{uploaded_file.name} was uploaded.")
