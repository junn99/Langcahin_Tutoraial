import streamlit as st

from langchain.embeddings import HuggingFaceBgeEmbeddings
# from langchain_huggingface import HuggingFaceEmbeddings # 공식문서엔 이건데 뭐지
from langchain.vectorstores import FAISS
from langchain.chains import conversationRetrieverChain
from langchain_ollama import ChatOllama

st.title("ai 기사 챗봇")

@st.cache_resource
def load_vector_store():
    embeddings = HuggingFaceBgeEmbeddings()
    vector_store = FAISS.load_local("이게 뭐지?", embeddings)
    return vector_store

db = load_vector_store()

llm = ChatOllama(
    model="gemma2:2b",
    temperature=0.5
    # other params...
)

chain = conversationRetrieverChain.from_llm(
    llm,
    db.as_retriever(search_kwargs={'k':3}),
    return_source_documents = True
)