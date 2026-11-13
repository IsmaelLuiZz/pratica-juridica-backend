from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.prazo import Prazo
from app.schemas.prazo import PrazoCreate, PrazoResponse

router = APIRouter(prefix="/prazos", tags=["Prazos"])

@router.post("/", response_model=PrazoResponse, status_code=status.HTTP_201_CREATED)
def criar_prazo(prazo: PrazoCreate, db: Session = Depends(get_db)):
    novo_prazo = Prazo(**prazo.dict())
    db.add(novo_prazo)
    db.commit()
    db.refresh(novo_prazo)
    return novo_prazo

@router.get("/", response_model=List[PrazoResponse])
def listar_prazos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    prazos = db.query(Prazo).offset(skip).limit(limit).all()
    return prazos

@router.get("/{prazo_id}", response_model=PrazoResponse)
def obter_prazo(prazo_id: int, db: Session = Depends(get_db)):
    prazo = db.query(Prazo).filter(Prazo.id == prazo_id).first()
    if not prazo:
        raise HTTPException(status_code=404, detail="Prazo não encontrado")
    return prazo

@router.delete("/{prazo_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_prazo(prazo_id: int, db: Session = Depends(get_db)):
    prazo = db.query(Prazo).filter(Prazo.id == prazo_id).first()
    if not prazo:
        raise HTTPException(status_code=404, detail="Prazo não encontrado")
    db.delete(prazo)
    db.commit()
    return None