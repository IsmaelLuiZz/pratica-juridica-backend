from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.database import Base

class PerfilEnum(str, enum.Enum):
    ALUNO = "aluno"
    PROFESSOR = "professor"
    ADMINISTRADOR = "administrador"

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_order=True, primary_key=True, index=True)
    nome = Column(String(250), nullable=False)
    email = Column(String(250), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    perfil = Column(Enum(PerfilEnum), default=PerfilEnum.ALUNO, nullable=False)
    ativo = Column(Boolean, default=True)
    criado_em = Column(DateTime, default=datetime.utcnow)

    # Exclusão lógica (RN04)
    deletado_em = Column(DateTime, nullable=True)
    deletado_por = Column(Integer, nullable=True)

class MatriculaEstagio(Base):
    __tablename__ = "matricula_estagio"

    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    disciplina = Column(String(100), nullable=False)
    periodo = Column(String(20), nullable=False)
    ativa = Column(Boolean, default=True)

    aluno = relationship("Usuario")