from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models.usuario import PerfilEnum

# Schema de criação de Aluno/Usuário
class AlunoCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    disciplina: Optional[str] = "Estágio Supervisionado"
    periodo: Optional[str] = "2026.2"

# Schema de resposta da API
class AlunoResponse(BaseModel):
    id: int
    nome: str
    email: str
    perfil: PerfilEnum
    ativo: bool
    criado_em: datetime

    class Config:
        from_attributes = True