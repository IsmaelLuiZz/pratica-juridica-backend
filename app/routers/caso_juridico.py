from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.caso_juridico import CasoJuridico
from app.schemas.caso_juridico import CasoJuridicoCreate, CasoJuridicoResponse

router = APIRouter(
    prefix="/casos",
    tags=["Casos Jurídicos"]
)

@router.get("/", response_model=List[CasoJuridicoResponse])
def listar_casos(db: Session = Depends(get_db)):
    return db.query(CasoJuridico).filter(CasoJuridico.deletado_em.is_(None)).all()

@router.post("/", response_model=CasoJuridicoResponse, status_code=status.HTTP_201_CREATED)
def criar_caso(caso_data: CasoJuridicoCreate, db: Session = Depends(get_db)):
    novo_caso = CasoJuridico(**caso_data.model_dump())
    db.add(novo_caso)
    db.commit()
    db.refresh(novo_caso)
    return novo_caso

@router.get("/{caso_id}", response_model=CasoJuridicoResponse)
def buscar_caso(caso_id: int, db: Session = Depends(get_db)):
    caso = db.query(CasoJuridico).filter(
        CasoJuridico.id == caso_id,
        CasoJuridico.deletado_em.is_(None)
    ).first()
    
    if not caso:
        raise HTTPException(status_code=404, detail="Caso jurídico não encontrado.")
    return caso