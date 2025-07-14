import streamlit as st
from rag_engine.qa_engine import answer_query

st.set_page_config(page_title="GenAI Internal Assistant", page_icon="🤖")

st.title("📄 GenAI Internal Assistant")

# User input
query = st.text_input("💬 Enter your question here:")

if query:
    with st.spinner("🔍 Thinking..."):
        response = answer_query(query)
        st.success("✅ Answer:")
        st.write(response)
