import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
import os

# Set your OpenAI API key here or use environment variable
os.environ['OPENAI_API_KEY'] = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else "sk-..."

# Database connection
DB_URI = "mysql+mysqlconnector://root:remember@localhost:3306/Chinook"
db = SQLDatabase.from_uri(DB_URI)

def get_schema(_):
    return db.get_table_info()

def run_query(query):
    return db.run(query)

prompt_template = """
Based on the table schema below, write a SQL query that would answer the user's question.
Use the exact table names and column names as shown in the schema.
Return only the SQL query without any explanation or markdown formatting.

{schema}

Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(prompt_template)

llm = ChatOpenAI(model="gpt-4o-mini")
sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | prompt
    | llm.bind(stop="\nSQL Result:")
    | StrOutputParser()
)

def main():
    st.title("LangChain SQL Agent GUI")
    st.write("Enter a natural language question about your database.")
    question = st.text_input("Your question:", "How many artists are there?")
    if st.button("Generate SQL and Run Query"):
        with st.spinner("Generating SQL query..."):
            sql_query = sql_chain.invoke({"question": question})
        st.code(sql_query, language="sql")
        with st.spinner("Running SQL query..."):
            result = run_query(sql_query)
        st.write("**Result:**")
        st.write(result)

if __name__ == "__main__":
    main()
