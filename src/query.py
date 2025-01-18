import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from src.utils.connection import engine


# Helper Functions
def load_data_to_postgres(file_path, table_name):
    """
    Load a CSV file into a PostgreSQL table.
    :param file_path: Path to the CSV file.
    :param table_name: Name of the table in PostgreSQL.
    """
    print(f"Loading data from {file_path} into table '{table_name}'...")
    df = pd.read_csv(file_path)
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(tabulate(df.head(), headers="keys", tablefmt="psql", showindex=False))
    print(f"Data successfully inserted into PostgreSQL table '{table_name}'.")


def execute_query(query):
    """
    Execute a SQL query and return results as a Pandas DataFrame.
    :param query: The SQL query string.
    :return: Query results as a Pandas DataFrame.
    """
    with engine.connect() as connection:
        return pd.read_sql_query(query, connection)


def display_and_plot(df, title, x_col, y_col, chart_type="bar", palette="viridis"):
    """
    Display query results as a table and plot a visualization.
    :param df: DataFrame to display and plot.
    :param title: Title of the chart.
    :param x_col: Column for x-axis.
    :param y_col: Column for y-axis.
    :param chart_type: Type of chart ('bar' or 'line').
    :param palette: Color palette for the chart.
    """
    print(tabulate(df, headers="keys", tablefmt="psql", showindex=False))

    plt.figure(figsize=(12, 6))
    if chart_type == "bar":
        sns.barplot(data=df, x=x_col, y=y_col, palette=palette)
    elif chart_type == "line":
        sns.lineplot(data=df, x=x_col, y=y_col, marker="o", color="b")
    
    plt.title(title, fontsize=16)
    plt.xlabel(x_col, fontsize=12)
    plt.ylabel(y_col, fontsize=12)
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Queries
def get_ev_count_by_make():
    query = """
        SELECT "Make", COUNT(*) AS total_vehicles
        FROM electric_vehicles
        GROUP BY "Make"
        ORDER BY total_vehicles DESC;
    """
    return execute_query(query)


def get_avg_range_by_vehicle_type():
    query = """
        SELECT "Electric Vehicle Type", AVG("Electric Range") AS avg_range
        FROM electric_vehicles
        GROUP BY "Electric Vehicle Type";
    """
    return execute_query(query)


def get_ev_count_by_county():
    query = """
        SELECT "County", COUNT(*) AS total_vehicles
        FROM electric_vehicles
        GROUP BY "County"
        ORDER BY total_vehicles DESC;
    """
    return execute_query(query)


def get_top_ev_models(limit=10):
    query = f"""
        SELECT "Make", "Model", COUNT(*) AS total
        FROM electric_vehicles
        GROUP BY "Make", "Model"
        ORDER BY total DESC
        LIMIT {limit};
    """
    return execute_query(query)


def get_cafv_eligibility_counts():
    query = """
        SELECT "Clean Alternative Fuel Vehicle (CAFV) Eligibility", COUNT(*) AS total
        FROM electric_vehicles
        GROUP BY "Clean Alternative Fuel Vehicle (CAFV) Eligibility";
    """
    return execute_query(query)


# Main Script
if __name__ == "__main__":
    # Path to the CSV file
    file_path = "src/data/Electric_Vehicles.csv"
    table_name = "electric_vehicles"

    # Load data into PostgreSQL
    load_data_to_postgres(file_path, table_name)

    # Run queries and display/plot results
    print("\nEV Count by Manufacturer:")
    ev_count = get_ev_count_by_make()
    display_and_plot(ev_count, "EV Count by Manufacturer", "Make", "total_vehicles")

    print("\nAverage Range by Vehicle Type:")
    avg_range = get_avg_range_by_vehicle_type()
    display_and_plot(avg_range, "Average Range by Vehicle Type", "Electric Vehicle Type", "avg_range")

    print("\nEV Count by County:")
    ev_count_county = get_ev_count_by_county()
    display_and_plot(ev_count_county, "EV Count by County", "County", "total_vehicles")

    print("\nTop EV Models:")
    top_ev_models = get_top_ev_models(limit=10)
    display_and_plot(top_ev_models, "Top EV Models", "Model", "total")

    print("\nCAFV Eligibility Counts:")
    cafv_counts = get_cafv_eligibility_counts()
    display_and_plot(cafv_counts, "CAFV Eligibility Counts", "Clean Alternative Fuel Vehicle (CAFV) Eligibility", "total")
