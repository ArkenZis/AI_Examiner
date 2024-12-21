import streamlit as st
import os

st.title("Hello World")

st.write("This is a paragraph")

question = st.text_area("Input the question:")
reference = st.text_area("Input the reference Answer:")
marking = st.text_area("Input the Marking Answer:")

if st.button("Submit"):
    st.write(question)
    st.write(reference)
    st.write(marking)

@st.cache_data()
def ask_llm(question, model="llama3-8b-8192"):
    from groq import Groq
    client = Groq(
        api_key=os.environ.get(os.environ.get("GROQ_API_KEY")),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model=model,
    )
    st.write(chat_completion.choices[0].message.content)


ask_llm("Hi")