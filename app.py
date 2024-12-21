import streamlit as st

st.title("Hello World")

st.write("This is a paragraph")

question = st.text_area("Input the question:")
reference = st.text_area("Input the reference Answer:")
marking = st.text_area("Input the Marking Answer:")

if st.button("Submit"):
    st.write(question)
    st.write(reference)
    st.write(marking)