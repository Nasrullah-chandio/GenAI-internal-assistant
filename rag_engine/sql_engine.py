import os
import pyodbc
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

def get_sql_connection():
    return pyodbc.connect(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={os.getenv("SQL_SERVER")};'
        f'DATABASE={os.getenv("SQL_DATABASE")};'
        f'UID={os.getenv("SQL_USERNAME")};'
        f'PWD={os.getenv("SQL_PASSWORD")}'
    )

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI

def get_sql_query_from_question(question: str) -> str:
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

    prompt = PromptTemplate.from_template("""
    You are a helpful SQL assistant working with SQL Server.

    Use the following table schema:

    Table: dwh.fact_bss_churn_data
    Columns:
    - customerID (varchar)
    - SeniorCitizen (bit)
    - Partner (varchar)
    - Dependents (varchar)
    - tenure (int)
    - MonthlyCharges (float)
    - TotalCharges (float)
    - churn_status (varchar)  -- Values: 'Churned', 'Active'
    - dim_customer_id (varchar)

    Based on the schema above, convert the user's question into a valid SQL Server query.

    Only return SQL code. Avoid placeholders. Use exact table and column names.

    Question: "{question}"
    """)

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(question=question)
