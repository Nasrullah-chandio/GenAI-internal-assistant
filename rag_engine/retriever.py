from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

CHROMA_DIR = "vector_store"

def load_retriever():
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )
    return vectordb
