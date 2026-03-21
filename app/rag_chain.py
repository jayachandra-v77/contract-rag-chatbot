import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone

import certifi

os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()



#loading environmental variables

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = os.getenv("INDEX_NAME")


embeddings = OpenAIEmbeddings(api_key=OPENAI_API_KEY)



vectorstore = PineconeVectorStore(
    index_name=INDEX_NAME,
    embedding=embeddings
)


retriever = vectorstore.as_retriever(search_kwargs={"k":3})


llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)


def ask_question(question):
    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])


    prompt = f"""
    
    You are a helpful AI assistant.
    Answer ONLY from the given context.
    If answer is not in context, say "I don't know".

    Context:
    {context}

    Question: {question}
    """

    response = llm.invoke(prompt)

    return response.content