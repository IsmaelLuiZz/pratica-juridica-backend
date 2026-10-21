from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.assistido import Assistido
from app.schemas.assistido import AssistidoCreate, AssistidoResponse

router = APIRouter(
    prefix="/assistidos",
    tags=["Gestão de Assistidos"]
)

@router.get("/", response_model=List[AssistidoResponse])
def listar_assistidos(db: Session = Depends(get_db)):
    return db.query(Assistido).filter(Assistido.deletado_em.is_(None)).all()

@router.post("/", response_model=AssistidoResponse, status_code=status.HTTP_201_CREATED)
def criar_assistido(assistido_data: AssistidoCreate, db: Session = Depends(get_db)):
    # Validação de unicidade do CPF
    assistido_existente = db.query(Assistido).filter(
        Assistido.cpf == assistido_data.cpf,
        Assistido.deletado_em.is_(None)
    ).first()
    
    if assistido_existente:
        raise HTTPException(
            status_code=400,
            detail="Já existe um assistido cadastrado com este CPF."
        )

    novo_assistido = Assistido(**assistido_data.model_dump())
    db.add(novo_assistido)
    db.commit()
    db.refresh(novo_assistido)
    return novo_assistido

@router.get("/{assistido_id}", response_model=AssistidoResponse)
def buscar_assistido(assistido_id: int, db: Session = Depends(get_db)):
    assistido = db.query(Assistido).filter(
        Assistido.id == assistido_id,
        Assistido.deletado_em.is_(None)
    ).first()
    
    if not assistido:
        raise HTTPException(status_code=404, detail="Assistido não encontrado.")
    return assistido