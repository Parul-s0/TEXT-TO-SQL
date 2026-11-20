from fastapi import FastAPI
from routers.upload import router as upload_router

app = FastAPI(
    title="TEXT TO SQL",
    version="1.0.0"
)

app.include_router(upload_router)


@app.get("/")
def root():
    return {
        "message": "Backend running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }