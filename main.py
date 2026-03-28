from fastapi import FastAPI
from api.routes import router
import uvicorn
from services.db_service import init_db

def create_app() -> FastAPI:
    app = FastAPI(
        title="Docling API Service",
        description="Document processing service using Docling",
        version="1.0.0"
    )

    # Include routes
    app.include_router(router)

    return app


app = create_app()
init_db()

@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "docling-api"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",   # module:variable
        host="0.0.0.0",
        port=8000,
        reload=True
    )