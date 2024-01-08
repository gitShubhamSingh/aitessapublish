from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
load_dotenv()
import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone 

#Accessing embedding
from chat.embeddings.openai import embedding

from langchain.chains import MultiRetrievalQAChain


# take pdf -> extract text -> create embedding -> store on pinecone
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




def createEmbeddingForQuerryAndGetScore(querry:str):

    #Initialize Pinecone
    pinecone.init(
        api_key = os.getenv("PINECONE_API_KEY"),
        environment= os.getenv("PINECONE_ENV_NAME")
    )

    # Getting index
    index = pinecone.Index(index_name="docs")
    
    # Creating Query embedding
    # print('querryEmbedding:-', )
    queryEmbedding = embedding.embed_query(querry)
    # print('Embedding Created')
   
    response = index.query(vector=[queryEmbedding], top_k=2, include_values=True)
    try:
        # print('----',type(response.to_dict()['matches'][0]['score']))
        if type(response.to_dict()['matches'][0]['score']) == float:
            score = response.to_dict()['matches'][0]['score']
        else:
            score=0
    except Exception as e:
        # print(str(e))
        score=0
   
    
    return score

  

    

