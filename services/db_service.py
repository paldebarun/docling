import psycopg2
from configurations.config import DATABASE_URL
from configurations.queries import (
    CREATE_DOCUMENTS_TABLE,
    GET_DOCUMENT,
    UPSERT_DOCUMENT
)



def get_connection():
    return psycopg2.connect(DATABASE_URL)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(CREATE_DOCUMENTS_TABLE)

    conn.commit()
    cur.close()
    conn.close()


def get_document(file_path: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        GET_DOCUMENT, (file_path,)
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result[0] if result else None


def save_document(file_path: str, text: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(UPSERT_DOCUMENT, (file_path, text))

    conn.commit()
    cur.close()
    conn.close()