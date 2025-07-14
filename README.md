<h1 align="left">GenAI Internal Assistant (RAG + SQL + OpenAI)</h1>

<h2>Table of Contents</h2>

- [Overview](#overview)
- [Objective](#objective)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [Setup & Installation](#setup)
- [Results](#results)
- [Next Steps](#next)

<a id="overview"></a>
<h2>Overview</h2>
<p align="justify">
This project presents an enterprise-ready GenAI Internal Assistant powered by Retrieval-Augmented Generation (RAG) architecture. It enables contextual natural language querying over both unstructured documents (PDFs, DOCX) and structured relational databases (SQL Server). The assistant is designed to support enterprise departments (e.g., HR, Network Ops, Customer Care) by providing document-based and SQL-based responses using OpenAI APIs.
</p>

<a id="objective"></a>
<h2>Objective</h2>
<p align="justify">
The main goal of this project is to build a conversational assistant capable of delivering insights across internal knowledge sources — including text documents and live databases. It uses RAG to enhance accuracy and contextual relevance in responses, making it suitable for domains requiring regulatory compliance, internal SOP adherence, and operational clarity.
</p>

<a id="features"></a>
<h2>Features</h2>

- ✅ Contextual Q&A over uploaded SOPs, policies, and department docs
- ✅ Dynamic SQL insights by connecting to MS SQL Server
- ✅ Modular architecture: retriever, router, LLM integration, UI
- ✅ Test scripts for document and SQL functionality
- ✅ Secure access via `.env` and external config loading

<a id="architecture"></a>
<h2>Architecture</h2>
<p align="justify">
The architecture follows a modular RAG design:
</p>

```text
                      +-----------------------------+
                      |        User Query           |
                      +-----------------------------+
                                 |
                                 v
                  +-------------------------------+
                  |           Router               |
                  | (Doc-based or SQL-based query?)|
                  +-------------------------------+
                        |                  |
        +------------------+         +---------------------+
        |  Vector Retriever|         | SQL Engine (pyodbc) |
        |     (Chroma)     |         |                     |
        +------------------+         +---------------------+
                |                            |
        +------------------+        +----------------------+
        | Retrieved Chunks |        | Queried Table Output |
        +------------------+        +----------------------+
                     \                 /
                      \               /
                       v             v
                 +---------------------------+
                 |      OpenAI / GPT-4o      |
                 +---------------------------+
                            |
                            v
                     +--------------+
                     | Final Answer |
                     +--------------+
```


<a id="technologies"></a>

<h2>Technologies</h2>
LangChain for retrieval pipeline

ChromaDB / FAISS for vector store

OpenAI (via langchain-openai) for LLM responses

PyODBC to query MS SQL Server securely

dotenv for managing secrets




<a id="run"></a>

<h2>🚀 How to Run the Assistant</h2> <p align="justify"> Follow the steps below to clone the repository, install dependencies, ingest documents, and start querying your assistant. Instructions are provided separately for Windows and Bash (Linux/macOS) users. </p>
<h3>🪟 For Windows Users (PowerShell)</h3> <ol> <li><strong>Clone the repository</strong> <pre><code>git clone https://github.com/your-username/genai-internal-assistant.git cd genai-internal-assistant</code></pre> </li> <li><strong>Set up virtual environment</strong> <pre><code>python -m venv venv venv\Scripts\activate pip install -r requirements.txt</code></pre> </li> <li><strong>Create a <code>.env</code> file in the root folder:</strong> <pre> OPENAI_API_KEY=your-openai-key SQL_SERVER=your-sql-server SQL_DATABASE=your-database SQL_USERNAME=your-username SQL_PASSWORD=your-password </pre> </li> <li><strong>Add your data</strong><br> Place your PDF, Word, Excel, or CSV files inside the <code>data/</code> folder. </li> <li><strong>Run ingestion script</strong> <pre><code>python rag_engine/ingest_docs.py</code></pre> </li> <li><strong>Run Streamlit UI</strong> <pre><code>streamlit run app.py</code></pre> Enter your question when prompted. </li> </ol>
<h3>🐧 For Linux/macOS (Bash)</h3> <ol> <li><strong>Clone the repository</strong> <pre><code>git clone https://github.com/your-username/genai-internal-assistant.git cd genai-internal-assistant</code></pre> </li> <li><strong>Set up virtual environment</strong> <pre><code>python3 -m venv venv source venv/bin/activate pip install -r requirements.txt</code></pre> </li> <li><strong>Create a <code>.env</code> file in the root folder:</strong> <pre> OPENAI_API_KEY=your-openai-key SQL_SERVER=your-sql-server SQL_DATABASE=your-database SQL_USERNAME=your-username SQL_PASSWORD=your-password </pre> </li> <li><strong>Add your data</strong><br> Place your PDF, Word, Excel, or CSV files inside the <code>data/</code> folder. </li> <li><strong>Run ingestion script</strong> <pre><code>python3 rag_engine/ingest_docs.py</code></pre> </li> <li><strong>Run Streamlit UI</strong> <pre><code>streamlit run app.py</code></pre> Enter your question when prompted. </li> </ol>

<h2>Next Steps</h2>
<p align="justify">
The following improvements are planned to enhance functionality, optimize retrieval accuracy, and prepare for scalable deployment:
</p>

🔲 Improve structured CSV support for hybrid lookup (e.g., asset ID-based queries)<br>
🔲 Prompt engineering for SQL insights generation<br>
🔲 Auto-table scan and metadata extraction to reduce query dependency<br>
🔲 Streamlit UI upgrade for hybrid chat + dashboard integration<br>
🔲 Dashboard summary generation using GenAI<br>
🔲 Docker containerization and GitHub Actions CI/CD pipeline setup<br>

