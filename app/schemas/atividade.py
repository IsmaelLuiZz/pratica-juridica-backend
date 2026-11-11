from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AtividadeBase(BaseModel):
    descricao: str
    caso_juridico_id: int
    responsavel_id: int

class AtividadeCreate(AtividadeBase):
    pass

class AtividadeUpdate(BaseModel):
    descricao: Optional[str] = None
    status: Optional[str] = None # PENDENTE ou CONCLUIDO

class AtividadeResponse(AtividadeBase):
    id: int
    status: str
    criado_em: datetime

    class Config:
        from_attributes = True