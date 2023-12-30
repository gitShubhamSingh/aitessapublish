
from langchain.chains import RetrievalQA
from chat.llms.chatopenai import build_llm

import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone 

#Accessing embedding
from chat.embeddings.openai import embedding


pinecone.init(
    api_key = os.getenv("PINECONE_API_KEY"),
    environment= os.getenv("PINECONE_ENV_NAME")
)

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"),
    embedding
)

def buid_retriever():
    return vector_store.as_retriever()

def build_chat():
    retriever = buid_retriever() 
    llm = build_llm()

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )