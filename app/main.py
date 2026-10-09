from fastapi import FastAPI

from app.database import engine, Base

from app.routers import aluno



# Cria as tabelas na base de dados (se ainda não existirem)

Base.metadata.create_all(bind=engine)



app = FastAPI(

title="Prática Jurídica API",

description="Backend para gestão de atendimentos, casos e documentos da UNINASSAU",

version="1.0.0"

)



# Inclui as rotas do módulo do Aluno/Estagiário

app.include_router(aluno.router)



@app.get("/")

def read_root():

    return {"message": "API da Prática Jurídica a funcionar com sucesso!"} 

