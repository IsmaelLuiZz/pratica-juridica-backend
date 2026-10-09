from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.database import get_db



router = APIRouter(

prefix="/alunos",

tags=["Alunos e Estagiários"]

)



# Endpoint de teste para o módulo de alunos

@router.get("/")

def listar_atendimentos(db: Session = Depends(get_db)):

    return {

"mensagem": "Módulo de Atendimento e Casos Jurídicos do Aluno ativo!",

"status": "sucesso"

} 

