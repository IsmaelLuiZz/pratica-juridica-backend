from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class AtendimentoBase(BaseModel):
    relato: str = Field(..., description="Descrição detalhada do atendimento realizado")
    caso_juridico_id: int = Field(..., description="ID do caso jurídico associado")
    assistido_id: int = Field(..., description="ID do assistido atendido")
    aluno_id: int = Field(..., description="ID do aluno responsável pelo atendimento")

class AtendimentoCreate(AtendimentoBase):
    pass

class AtendimentoResponse(AtendimentoBase):
    id: int
    data_hora: datetime
    deletado_em: Optional[datetime] = None

    class Config:
        from_attributes = True