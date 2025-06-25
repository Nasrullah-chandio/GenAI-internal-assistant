# rag_engine/retriever.py
import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

load_dotenv()

CHROMA_DIR = "vector_store"          # ← change to match ingest script

def load_retriever():
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings
    )
    return vectordb

def retrieve_relevant_docs(query: str, k: int = 3) -> list[Document]:
    vectordb = load_retriever()
    return vectordb.similarity_search(query, k=k)

def format_context(chunks: list[Document]) -> str:
    return "\n\n---\n\n".join([doc.page_content for doc in chunks])
