import pandas as pd
from src.utils.connection import engine

df = pd.read_csv('src/data/Electric_Vehicles.csv')
df.to_sql('electric_vehicles', con=engine, if_exists='replace', index=False)
print("Data successfully inserted into PostgreSQL")