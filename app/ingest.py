import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec


#loading environmental variables

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")




#documents loading

loader = PyPDFLoader(".\contract-rag-chatbot\data\EY Consulting Contract.pdf")

docs = loader.load()

# chunking 

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap = 200
)

chunks = text_splitter.split_documents(docs)


# embeddings

embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

pc = Pinecone(api_key=PINECONE_API_KEY)


#creating index if not exist

if INDEX_NAME not in pc.list_indexes().names():
    pc.create_index(
        index= INDEX_NAME,
        dimension=1536,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )

    print("Index created")

else:

    print("Index already exist")



vectorestore = PineconeVectorStore(
        chunks,
    embeddings,
    index_name=INDEX_NAME
)

print("✅ PDF ingested successfully")
