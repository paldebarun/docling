import os
import uuid
from configurations.config import UPLOAD_DIR

os.makedirs(UPLOAD_DIR, exist_ok=True)


def save_file(file_bytes: bytes, filename: str) -> str:
    unique_name = f"{uuid.uuid4()}_{filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    return file_path


def get_file_path(path: str) -> str:
    # Later → replace with S3/Azure logic
    return path