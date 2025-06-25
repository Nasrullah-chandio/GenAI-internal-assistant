import os
from dotenv import load_dotenv
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

DATA_DIR = "data"
VECTOR_STORE_DIR = "vector_store"

def ingest_documents():
    all_docs = []

    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            full_path = os.path.join(DATA_DIR, filename)
            print(f"📄 Loading: {full_path}")
            loader = PyPDFLoader(full_path)
            docs = loader.load()
            all_docs.extend(docs)

    if not all_docs:
        print("❌ No documents were loaded. Check your data/ folder.")
        return

    print(f"✅ Loaded {len(all_docs)} documents")

    # Split into smaller chunks
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = splitter.split_documents(all_docs)

    print(f"✅ Created {len(chunks)} chunks")

    # Embed and store
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(chunks, embeddings, persist_directory=VECTOR_STORE_DIR)

    print(f"✅ Vector store saved to {VECTOR_STORE_DIR}/")

if __name__ == "__main__":
    ingest_documents()
