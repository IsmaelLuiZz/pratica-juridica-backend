from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.documento import Documento
from app.schemas.documento import DocumentoCreate, DocumentoResponse

router = APIRouter(prefix="/documentos", tags=["Documentos"])

@router.post("/", response_model=DocumentoResponse, status_code=status.HTTP_201_CREATED)
def criar_documento(documento: DocumentoCreate, db: Session = Depends(get_db)):
    novo_documento = Documento(**documento.dict())
    db.add(novo_documento)
    db.commit()
    db.refresh(novo_documento)
    return novo_documento

@router.get("/", response_model=List[DocumentoResponse])
def listar_documentos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    documentos = db.query(Documento).offset(skip).limit(limit).all()
    return documentos

@router.get("/{documento_id}", response_model=DocumentoResponse)
def obter_documento(documento_id: int, db: Session = Depends(get_db)):
    documento = db.query(Documento).filter(Documento.id == documento_id).first()
    if not documento:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    return documento

@router.delete("/{documento_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_documento(documento_id: int, db: Session = Depends(get_db)):
    documento = db.query(Documento).filter(Documento.id == documento_id).first()
    if not documento:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    db.delete(documento)
    db.commit()
    return None