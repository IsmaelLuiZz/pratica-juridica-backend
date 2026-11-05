from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.atendimento import Atendimento
from app.schemas.atendimento import AtendimentoCreate, AtendimentoResponse

router = APIRouter(prefix="/atendimentos", tags=["Atendimentos"])

@router.post("/", response_model=AtendimentoResponse, status_code=status.HTTP_201_CREATED)
def criar_atendimento(atendimento: AtendimentoCreate, db: Session = Depends(get_db)):
    novo_atendimento = Atendimento(**atendimento.model_dump())
    db.add(novo_atendimento)
    db.commit()
    db.refresh(novo_atendimento)
    return novo_atendimento

@router.get("/", response_model=List[AtendimentoResponse])
def listar_atendimentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    atendimentos = db.query(Atendimento).filter(Atendimento.deletado_em == None).offset(skip).limit(limit).all()
    return atendimentos