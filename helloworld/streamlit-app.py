import streamlit as st

st.title("App Engine sample app")

name = st.text_input("Your name?")

st.write(f"Hello, {name or 'world'}!")
