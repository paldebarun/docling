from fastapi import APIRouter
from services.storage_service import save_file
from services.docling_service import process_document
from pydantic import BaseModel
from services.db_service import get_document, save_document
class ProcessRequest(BaseModel):
    file_path: str

router = APIRouter()

@router.post("/process-from-path")
def process_from_path(request: ProcessRequest):

    
    cached_text = get_document(request.file_path)

    if cached_text:
        return {
            "file_path": request.file_path,
            "text": cached_text,
            "source": "cache"
        }

   
    result = process_document(request.file_path)

  
    save_document(request.file_path, result["text"])

    return {
        "file_path": request.file_path,
        "text": result["text"],
        "source": "processed"
    }






@router.post("/process-from-path")
def process_from_path(request: ProcessRequest):

    cached_text = get_document(request.file_path)
    
    if cached_text:
      return {
        "file_path": request.file_path,
       
        "text": cached_text
    }
    

    result = process_document(request.file_path)

    return {
        "file_path": request.file_path,
        "text_length": result["length"],
        "text": result["text"]
    }