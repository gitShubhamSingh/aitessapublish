from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone 

#Accessing embedding
from chat.embeddings.openai import embedding




def createEmbeddingsForPdf(pdfId:str, pdfPath:str):
   
    # Creating text splitter
    textSplitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    # load pdf
    loader = PyPDFLoader(pdfPath)

    # create chunks
    docs = loader.load_and_split(text_splitter=textSplitter)

    pinecone.init(
        api_key = os.getenv("PINECONE_API_KEY"),
        environment= os.getenv("PINECONE_ENV_NAME")
    )

    vector_store = Pinecone.from_existing_index(
        os.getenv("PINECONE_INDEX_NAME"),
        embedding
    )

    vector_store.add_documents(docs)