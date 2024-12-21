import streamlit as st
import os
from openai import OpenAI


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
        temperature=0.1,
    )
    return chat_completion.choices[0].message.content

@st.cache_data()
def ask_openai(query):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
    )
    chat_completion = client.chat.completions.create(
    messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="gpt-4o",
    )
    return chat_completion.choices[0].message.content


st.title("Hello World")
st.write("AI Examiner")
question = st.text_area("Input the question:")
reference = st.text_area("Input the reference Answer:")
marking = st.text_area("Input the Marking Answer:")
prompt = st.text_area(
    "Prompt:",
    """Check marking answer against reference answer considering question. 
             Question: {question}
             Marking Answer: {marking}
             Reference Answer: {reference}""",
)

if st.button("Submit"):
    query = prompt.format(question=question, marking=marking, reference=reference)
    st.header("Groq Says:")
    st.write(ask_llm(query))
    st.write("----")
    st.header("OpenAI Says:")
    st.write(ask_openai(query))
