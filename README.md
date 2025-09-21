# LangChain SQL Agent

This project demonstrates how to use LangChain with OpenAI's GPT-4o-mini model to generate and execute SQL queries against a MySQL database (Chinook sample DB). It features an interactive notebook workflow for natural language to SQL conversion and result interpretation.

## Features
- Natural language to SQL query generation using LangChain and OpenAI
- Automatic schema extraction from MySQL database
- Query execution and result display
- Customizable prompt templates for precise SQL generation
- Uses the Chinook sample database


## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/ahmedmalik07/langchain_sql_agent.git
cd langchain_sql_agent
```

### 2. Set up Conda environment
```bash
conda create -n langchain_sql python=3.11
conda activate langchain_sql
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the Chinook MySQL database
- Import `Chinook_MySql.sql` into your local MySQL server.
- Update the connection string in the notebook and `app.py` if needed:
  ```python
  db_uri = "mysql+mysqlconnector://root:<your_password>@localhost:3306/Chinook"
  ```

### 5. Run the notebook
```bash
jupyter notebook main.ipynb
```

### 6. Run the Streamlit GUI
```bash
streamlit run app.py
```

## Usage
- Enter a natural language question in the notebook or GUI (e.g., "How many artists are there?")
- The agent will generate the SQL query, execute it, and return the result in natural language.

## Example
```
Question: How many artists are there?
SQL Query: SELECT COUNT(ArtistId) AS TotalArtists FROM Artist;
Response: There are a total of 275 artists in the database.
```

## Repository Structure
- `main.ipynb` — Main notebook for the agent workflow
- `app.py` — Streamlit GUI for interactive use
- `requirements.txt` — Python dependencies
- `Chinook_MySql.sql` — Sample database schema

## License
MIT

## Author
Ahmed Malik
