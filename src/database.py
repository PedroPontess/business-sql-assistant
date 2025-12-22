import os

from langchain_community.utilities import SQLDatabase
from sqlalchemy.pool import StaticPool


def get_db_connection() -> SQLDatabase:
    """
    Establishes a READ-ONLY connection to the Chinook SQLite database.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)

    db_path_data = os.path.join(project_root, "data", "Chinook.db")
    db_path_root = os.path.join(project_root, "Chinook.db")

    if os.path.exists(db_path_data):
        db_path = db_path_data
    elif os.path.exists(db_path_root):
        db_path = db_path_root
    else:
        raise FileNotFoundError("Database 'Chinook.db' not found.")

    print(f"📂 Database found at: {db_path}")

    db_uri = f"sqlite:///file:{db_path}?mode=ro&uri=true"

    try:
        return SQLDatabase.from_uri(
            db_uri,
            engine_args={
                "connect_args": {"uri": True},
                "poolclass": StaticPool,  # Good for SQLite + Streamlit
            },
        )
    except Exception as e:
        raise RuntimeError(f"Failed to connect to database: {e}")
