import streamlit as st
import os
from openai import AzureOpenAI


@st.cache_data()
def ask_llm(question, model="llama-3.1-70b-versatile"):
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
    client = AzureOpenAI(
        api_version="2024-08-01-preview",
        azure_endpoint=os.environ.get("OPENAI_API_BASE"),
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


st.title("AI Examiner")
question = st.text_area("Input the question:",value="What is the purpose of feature scaling in machine learning, and which common methods are used to perform it?")
reference = st.text_area("Input the reference Answer:",value="Feature scaling is used to standardize the range of independent variables or features of data to ensure that no feature dominates the learning algorithm due to its larger magnitude. Common methods for feature scaling include Normalization (Min-Max Scaling), which scales values to a range of [0, 1], and Standardization (Z-score scaling), which centers the data around the mean with a standard deviation of 1.")
marking = st.text_area("Input the Marking Answer:",value="Feature scaling adjusts the magnitude of features in the dataset. A commonly used method is Normalization, which scales values between [0, 1].")
prompt = st.text_area(
    "Prompt:",
    """Check marking answer against reference answer considering question. 
             Question: {question}
             Marking Answer: {marking}
             Reference Answer: {reference}

Find the Accuracy, Correctness, Structure, Relevance and Completeness
Score each and total from 1 to 100
""",
)

if st.button("Submit"):
    query = prompt.format(question=question, marking=marking, reference=reference)
    st.header("Groq Says:")
    st.write(ask_llm(query))
    st.write("----")
    st.header("OpenAI Says:")
    st.write(ask_openai(query))
