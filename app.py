import streamlit as st
st.title("AI CHATBOT")
st.write("welcome to ai chatbot")
prompt=st.text_input("Enter your prompt")
if st.button("Generate"):
    if prompt:
        st.success("Enter a question")
        st.write("You entered a question")
    else:
        st.warning("Please enter a question")
        