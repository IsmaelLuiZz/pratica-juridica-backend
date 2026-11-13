from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PrazoBase(BaseModel):
    descricao: str
    data_vencimento: datetime
    status: Optional[str] = "PENDENTE"
    caso_juridico_id: int

class PrazoCreate(PrazoBase):
    pass

class PrazoResponse(PrazoBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True