from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.documento import Documento
from app.schemas.supervisao import SupervisaoUpdate

router = APIRouter(prefix="/supervisao", tags=["Supervisão e Aprovação"])

@router.patch("/documentos/{documento_id}/aprovar")
def supervisionar_documento(
    documento_id: int, 
    dados: SupervisaoUpdate, 
    db: Session = Depends(get_db)
):
    # Procura o documento gerado pelo aluno
    documento = db.query(Documento).filter(Documento.id == documento_id).first()
    if not documento:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    
    # Atualiza o status de validação (Regra de Ouro)
    documento.tipo = f"{documento.tipo} - [{dados.status}]"
    if dados.observacoes_professor:
        documento.descricao = f"{documento.descricao or ''} | Obs. Professor: {dados.observacoes_professor}"
    
    db.commit()
    db.refresh(documento)
    
    return {
        "mensagem": f"Documento atualizado com sucesso para o status: {dados.status}",
        "documento_id": documento.id,
        "status_atual": dados.status,
        "observacoes": dados.observacoes_professor
    }