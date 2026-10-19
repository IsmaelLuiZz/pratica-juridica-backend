from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from app.models.usuario import PerfilUsuario

class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: PerfilUsuario

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    perfil: PerfilUsuario
    ativo: bool
    created_at: datetime

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    usuario_id: Optional[int] = None
    perfil: Optional[str] = None