

CREATE_DOCUMENTS_TABLE = """
CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    file_path TEXT UNIQUE,
    extracted_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

GET_DOCUMENT = """
SELECT extracted_text 
FROM documents 
WHERE file_path = %s;
"""

UPSERT_DOCUMENT = """
INSERT INTO documents (file_path, extracted_text)
VALUES (%s, %s)
ON CONFLICT (file_path)
DO UPDATE SET extracted_text = EXCLUDED.extracted_text;
"""