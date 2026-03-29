from pydantic import BaseModel

class ProcessRequest(BaseModel):
    file_path: str