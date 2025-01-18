import pandas as pd

def execute_query(engine, query):
    """Executes a SQL query and returns the results as a Pandas DataFrame."""
    with engine.connect() as connection:
        return pd.read_sql_query(query, connection)
