from fastapi import APIRouter,UploadFile,File
from schema.file import ProcessRequest
from services.docling_service import process_document

from services.db_service import get_document, save_document
from services.storage_service import save_file



router = APIRouter()

@router.post("/upload-and-process")
async def upload_and_process(file: UploadFile = File(...)):
    file_bytes = await file.read()


    file_path = save_file(file_bytes, file.filename)

    
    cached_text = get_document(file_path)

    if cached_text:
        return {
            "filename": file.filename,
            "file_path": file_path,
            "text": cached_text,
            "cached": True
        }


    result = process_document(file_path)

    
    save_document(file_path, result["text"])

    return {
        "filename": file.filename,
        "file_path": file_path,
        "text_length": result["length"],
        "text": result["text"],
        "cached": False
    }






@router.post("/process-from-path")
def process_from_path(request: ProcessRequest):

   
    cached_text = get_document(request.file_path)

    if cached_text:
        return {
            "file_path": request.file_path,
            "text": cached_text,
            "cached": True
        }

   
    result = process_document(request.file_path)


    save_document(request.file_path, result["text"])

    return {
        "file_path": request.file_path,
        "text_length": result["length"],
        "text": result["text"],
        "cached": False
    }