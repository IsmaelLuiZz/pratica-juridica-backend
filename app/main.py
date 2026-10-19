from fastapi import FastAPI
from app.routers import auth

app = FastAPI(
    title="Sistema de Gestão da Prática Jurídica - UNINASSAU",
    version="1.0.0"
)

app.include_router(auth.router)

@app.get("/")
def read_root():
    return {"status": "online"}