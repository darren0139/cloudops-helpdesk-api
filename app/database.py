import os
from dotenv import load_dotenv
import psycopg
from psycopg.rows import dict_row

# Loads variables from .env when running locally.
# In Docker/EC2, environment variables from -e or --env-file will also work.
load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"{name} environment variable is not set")

    return value


def get_connection():
    """
    Create a connection to PostgreSQL RDS.

    v1/v2:
    - App used SQLite, a local file database.

    v3:
    - App connects to Amazon RDS PostgreSQL over the network.
    - DB connection values come from environment variables.
    """

    return psycopg.connect(
        host=get_required_env("DB_HOST"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "helpdesk"),
        user=os.getenv("DB_USER", "postgres"),
        password=get_required_env("DB_PASSWORD"),
        row_factory=dict_row,
    )


def init_db():
    """
    Create the tickets table if it does not already exist.

    This is the PostgreSQL/RDS version of the old SQLite init.
    """

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS tickets (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT NOT NULL,
                    category TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    status TEXT NOT NULL DEFAULT 'open',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                """
            )

        conn.commit()