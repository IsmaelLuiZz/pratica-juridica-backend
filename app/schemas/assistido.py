from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class AssistidoBase(BaseModel):
    nome: str
    cpf: str = Field(..., min_length=11, max_length=14)
    telefone: Optional[str] = None
    email: Optional[EmailStr] = None
    endereco: Optional[str] = None
    observacoes: Optional[str] = None

class AssistidoCreate(AssistidoBase):
    pass

class AssistidoResponse(AssistidoBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True