from rag_engine.retriever import load_retriever
from rag_engine.sql_engine import get_sql_connection, get_sql_query_from_question
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
import pyodbc

def run_sql_query(question: str) -> str:
    connection = get_sql_connection()
    cursor = connection.cursor()

    table_schema = """
    Table: dwh.fact_bss_churn_data
    Columns: customerID, SeniorCitizen, Partner, Dependents, tenure, MonthlyCharges, TotalCharges, churn_status, dim_customer_id
    """

    raw_query = get_sql_query_from_question(question)
    query_clean = raw_query.strip().strip("`").replace("sql", "").strip()

    if not query_clean.lower().startswith("select"):
        return f"⚠️ Generated SQL doesn't look safe or valid:\n\n{query_clean}"

    try:
        cursor.execute(query_clean)
        result = cursor.fetchone()
        return result[0] if result else "No results found."
    except Exception as e:
        return f"❌ SQL Error: {str(e)}"
    finally:
        connection.close()

def answer_query(question: str) -> str:
    if "how many" in question.lower() or "total" in question.lower() or "count" in question.lower():
        return run_sql_query(question)

    retriever = load_retriever().as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-4o", temperature=0),
        retriever=retriever,
        return_source_documents=False
    )
    return qa_chain.run(question)
