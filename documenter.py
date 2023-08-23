import streamlit as st
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (ChatPromptTemplate,
                                    HumanMessagePromptTemplate,
                                    SystemMessagePromptTemplate)
from langchain.document_loaders import *
from langchain.chains.summarize import load_summarize_chain
import tempfile
from langchain.docstore.document import Document

st.title("Code documenter")

code_samples = st.text_area("Enter code samples written in Python")

def documentationGenerator(code_samples):
    chat = ChatOpenAI(
        model="gpt-3.5-turbo-16k",
        temperature=0
    )
    system_template = """You are an assistant tasked with generating expanded documentation for each function in the given code samples. The code samples are stored in the variable {code_samples}."""
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_template = """Please generate expanded documentation for each function in the provided code samples. The code samples are stored in the variable {code_samples}."""
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run(code_samples=code_samples)
    return result

if st.button("Generate Documentation"):
    if code_samples:
        expanded_documentation = documentationGenerator(code_samples)
        st.markdown(expanded_documentation)
    else:
        st.markdown("")
