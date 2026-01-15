import streamlit as st

st.set_page_config(page_title="Add Two Numbers", layout="centered")

st.title("Addition App")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

if st.button("Add"):
    st.success(f"Result: {num1 + num2}")
