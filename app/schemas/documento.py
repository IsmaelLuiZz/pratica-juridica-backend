from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class DocumentoBase(BaseModel):
    titulo: str
    tipo: str
    caminho_arquivo: Optional[str] = None
    descricao: Optional[str] = None
    caso_juridico_id: int

class DocumentoCreate(DocumentoBase):
    pass

class DocumentoResponse(DocumentoBase):
    id: int
    data_criacao: datetime

    class Config:
        from_attributes = True