from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CasoJuridicoBase(BaseModel):
    titulo: str = Field(..., max_length=250, description="Título ou assunto principal do caso")
    descricao: str = Field(..., description="Descrição detalhada dos fatos jurídicos")
    status: Optional[str] = Field("EM_ANDAMENTO", description="Status atual do caso (ex: EM_ANDAMENTO, AGUARDANDO_APROVACAO, ENCERRADO)")
    assistido_id: int
    aluno_id: int
    professor_id: int

class CasoJuridicoCreate(CasoJuridicoBase):
    pass

class CasoJuridicoResponse(CasoJuridicoBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True