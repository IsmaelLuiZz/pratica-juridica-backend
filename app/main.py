from fastapi import FastAPI
from app.database import engine, Base
import app.models.usuario  # Importa os modelos para serem registados no Base
import app.models.assistido
from app.routers import assistido

# Cria as tabelas na base de dados (se ainda não existirem)
Base.metadata.create_all(bind=engine)

from app.routers import aluno

app = FastAPI(
    title="Sistema de Prática Jurídica - UNINASSAU",
    version="1.0.0"
)

app.include_router(aluno.router)
app.include_router(assistido.router)

@app.get("/")
def root():
    return {"message": "API da Prática Jurídica a funcionar com sucesso!"}