from pydantic import BaseModel
from typing import Optional

class SupervisaoUpdate(BaseModel):
    status: str  # Ex: "APROVADO", "REJEITADO_AJUSTES"
    observacoes_professor: Optional[str] = None