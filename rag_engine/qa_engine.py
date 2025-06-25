import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from rag_engine.retriever import retrieve_relevant_docs, format_context

load_dotenv()

# Initialize OpenAI Chat model (GPT-3.5 or GPT-4 based on your API key config)
llm = ChatOpenAI(
    model="gpt-4",  # Change to "gpt-3.5-turbo" if using that model
    temperature=0.3
)

def answer_query(question: str, k: int = 3) -> str:
    # Step 1: Retrieve top-k relevant chunks
    docs = retrieve_relevant_docs(question, k)
    
    if not docs:
        return "❌ Sorry, I couldn’t find relevant information in the documents."

    # Step 2: Format context into a readable string
    context = format_context(docs)

    # Step 3: Compose the final prompt
    prompt = f"""You are an internal company assistant. Based on the context below, answer the user's question clearly and concisely.

Context:
{context}

Question:
{question}

Answer:"""

    # Step 4: Generate answer from LLM
    response = llm.invoke(prompt)
    return response.content
