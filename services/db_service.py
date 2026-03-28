import psycopg2

DATABASE_URL = "postgresql://admin:admin@localhost:5432/docling_db"


def get_connection():
    return psycopg2.connect(DATABASE_URL)


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id SERIAL PRIMARY KEY,
            file_path TEXT UNIQUE,
            extracted_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def get_document(file_path: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT extracted_text FROM documents WHERE file_path = %s",
        (file_path,)
    )

    result = cur.fetchone()

    cur.close()
    conn.close()

    return result[0] if result else None


def save_document(file_path: str, text: str):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO documents (file_path, extracted_text)
        VALUES (%s, %s)
        ON CONFLICT (file_path)
        DO UPDATE SET extracted_text = EXCLUDED.extracted_text;
    """, (file_path, text))

    conn.commit()
    cur.close()
    conn.close()