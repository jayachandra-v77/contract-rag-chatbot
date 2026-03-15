import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone.vectorstores import PineconeVectorStore


# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")


# Load PDF
loader = PyPDFLoader(".\contracts\EY Consulting Contract.pdf")
documents = loader.load()

#print(f"Total pages loaded: {len(documents)}")


#chunking 

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap= 200
)


docs = text_splitter.split_documents(documents=documents)

#print(f"Total number of documents after chunking: {len(docs)}")


# # Embeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=OPENAI_API_KEY)


#intializing pinecone

pc = Pinecone(api_key=PINECONE_API_KEY)


#Creating Index if not exist


# if INDEX_NAME not in pc.list_indexes().names():
   
#    pc.create_index(
#         name=INDEX_NAME,
#         dimension=1536,
#         metric="cosine",
#         spec=ServerlessSpec(cloud="aws", region="us-east-1")
# )
#    print("Index has been created")   
        
# else:
#      print("Index name is already exist")




# # creating vectore store

# vector_store = PineconeVectorStore.from_documents(
#      documents=docs,
#      embedding=embeddings,
#      index_name=INDEX_NAME
# )

vector_store = PineconeVectorStore.from_existing_index(
    index_name=INDEX_NAME,
    embedding=embeddings
)

retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# LLM

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)

# Custom Prompt Template
prompt_template = """
You are a legal AI assistant specialized in analyzing contracts.

Answer the question ONLY based on the context provided below.

If the answer is not present in the context, say:
"Not mentioned in the contract."

Context:
{context}

Question:
{question}

Answer:
"""
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)


# RAG Chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff",
    chain_type_kwargs={"prompt": prompt},
    return_source_documents=True
)


# Ask function
def ask_bot(question):

    result = qa.invoke({"query": question})

    return result["result"]

