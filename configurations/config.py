import os 


UPLOAD_DIR = os.environ.get("UPLOAD_DIR","uploads")
POSTGRES_USER=os.environ.get("POSTGRES_USER","admin")
POSTGRES_PASSWORD=os.environ.get("POSTGRES_PASSWORD","admin")
POSTGRESS_PORT=os.environ.get("POSTGRESS_PORT",5432)
POSTGRES_DB=os.environ.get("POSTGRES_DB","docling_db")
POSTGRES_HOST=os.environ.get("POSTGRES_HOST","localhost")

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRESS_PORT}/{POSTGRES_DB}"

PORT=os.environ.get("SERVER_PORT",8082)