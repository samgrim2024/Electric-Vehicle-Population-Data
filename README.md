
# Electric Vehicle Population Data Project

This project connects to a PostgreSQL database using Python and performs various analyses on electric vehicle population data. It uses SQLAlchemy and pg8000 for database interaction.


## Installation

Follow these steps to set up the project:

### 1. Clone the Repository

### 2. Create and Activate a Virtual Environment

Create a virtual environment to keep your project’s dependencies isolated:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  export PYTHONPATH=$(pwd)

  ```
- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```

### 3. Install the Required Python Packages

Install all necessary packages listed in the `requirements.txt` file using `pip`:

```bash
pip install -r requirements.txt
```

This installs `SQLAlchemy` and `pg8000`, along with any other dependencies.

### 4. Set Up Environment Variables

Before running the project, make sure to set up the following environment variables to connect to your PostgreSQL database:

```bash
export DB_USER='your_postgres_username'
export DB_PASSWORD='your_postgres_password'
```

You can set these in your terminal session or add them to your `.bashrc` or `.zshrc` file for persistent use.

### 5. Run the Project

Now you can run the project to connect to PostgreSQL and perform queries:

```bash
python3 connection.py
```

If everything is set up correctly, the script will connect to the database and execute the queries defined in the code.


