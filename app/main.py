from fastapi import FastAPI
from app.database import engine, Base
import app.models.aluno  # Importa os modelos para serem registados no Base
import app.models.assistido
from app.routers import assistido
import app.models.caso_juridico
from app.routers import caso_juridico
from app.routers import atendimento
import app.models.atendimento
from app.routers import aluno, assistido, caso_juridico, atendimento, atividade
from app.routers import documento
from app.routers import prazo
from app.routers import supervisao

# Cria as tabelas na base de dados (se ainda não existirem)
Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="Sistema de Prática Jurídica - UNINASSAU",
    version="1.0.0"
)

app.include_router(aluno.router)
app.include_router(assistido.router)
app.include_router(caso_juridico.router)
app.include_router(atendimento.router)
app.include_router(atividade.router)
app.include_router(documento.router)
app.include_router(prazo.router)
app.include_router(supervisao.router)

@app.get("/")
def root():
    return {"message": "API da Prática Jurídica a funcionar com sucesso!"}