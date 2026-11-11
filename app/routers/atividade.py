from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.atividade import Atividade
from app.schemas.atividade import AtividadeCreate, AtividadeResponse, AtividadeUpdate

router = APIRouter(prefix="/atividades", tags=["Atividades"])

@router.post("/", response_model=AtividadeResponse, status_code=status.HTTP_201_CREATED)
def criar_atividade(atividade: AtividadeCreate, db: Session = Depends(get_db)):
    nova_atividade = Atividade(**atividade.dict())
    db.add(nova_atividade)
    db.commit()
    db.refresh(nova_atividade)
    return nova_atividade

@router.get("/", response_model=List[AtividadeResponse])
def listar_atividades(db: Session = Depends(get_db)):
    atividades = db.query(Atividade).filter(Atividade.deletado_em == None).all()
    return atividades

@router.patch("/{atividade_id}", response_model=AtividadeResponse)
def atualizar_atividade(atividade_id: int, dados_atualizacao: AtividadeUpdate, db: Session = Depends(get_db)):
    atividade = db.query(Atividade).filter(Atividade.id == atividade_id, Atividade.deletado_em == None).first()
    if not atividade:
        raise HTTPException(status_code=404, detail="Atividade não encontrada")
    
    for key, value in dados_atualizacao.dict(exclude_unset=True).items():
        setattr(atividade, key, value)
    
    db.commit()
    db.refresh(atividade)
    return atividade