import os
from sqlalchemy import create_engine

DATABASE_TYPE = 'postgresql'
DBAPI = 'pg8000'
HOST = 'localhost'
USER = os.getenv('DB_USER', 'postgres')
PASSWORD = os.getenv('DB_PASSWORD', '')
DATABASE = 'ev_database'
PORT = 5432

engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

with engine.connect() as connection:
    print("Connection successful!")