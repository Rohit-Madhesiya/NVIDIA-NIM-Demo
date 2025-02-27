import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from langchain_nvidia_ai_endpoints import ChatNVIDIA,NVIDIAEmbeddings
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
import time


# load the nvidia api key
os.environ['NVIDIA_API_KEY']=os.getenv("NVIDIA_API_KEY")

# llm models
# NVIDIA NIM Inferencing
llm=ChatNVIDIA(model="deepseek-ai/deepseek-r1")


def vector_embedding():
  if "vectors" not in st.session_state:
    st.session_state.embeddings=NVIDIAEmbeddings()
    st.session_state.loader=PyPDFDirectoryLoader("research_papers")
    st.session_state.docs=st.session_state.loader.load()
    st.session_state.splitter=RecursiveCharacterTextSplitter(chunk_size=700,chunk_overlap=50)
    st.session_state.final_docs=st.session_state.splitter.split_documents(st.session_state.docs[:30])
    st.session_state.vectors=FAISS.from_documents(st.session_state.final_docs,st.session_state.embeddings)




prompt=ChatPromptTemplate.from_template(
  """
  Answer the questions based on the provided context only.
  Please provide the most accurate response based on the question.
  <context>{context}</context>
  Question:{input}
  Answer:
  """
)


# streamlit frontend
st.set_page_config(page_title="NVIDIA Deepseek AI",page_icon="🧠",layout="wide")
st.title("NVIDIA Deepseek AI")

question=st.text_input("Enter your question here:")

if st.button("Document Embedding"):
  vector_embedding()
  st.write("FAISS Vector Store Db is Ready using NVIDIAEmbedding")

if question:
  document_chain=create_stuff_documents_chain(llm,prompt)
  retriever=st.session_state.vectors.as_retriever()
  retrieval_chain=create_retrieval_chain(retriever,document_chain)
  start=time.process_time()
  response=retrieval_chain.invoke({"input":question})
  print("Response Time:",time.process_time()-start)
  st.write(response['answer'])

  with st.expander("Document Similarity Search"):
    # Find the relevant document chunks
    for i,doc in enumerate(response['context']):
      st.write(doc.page_content)
      st.write("------------------------------------")
