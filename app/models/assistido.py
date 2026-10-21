from sqlalchemy import Column, Integer, String, DateTime, Text
from datetime import datetime
from app.database import Base

class Assistido(Base):
    __tablename__ = "assistido"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(250), nullable=False)
    cpf = Column(String(14), unique=True, index=True, nullable=False)
    telefone = Column(String(20), nullable=True)
    email = Column(String(250), nullable=True)
    endereco = Column(Text, nullable=True)
    observacoes = Column(Text, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)
    deletado_em = Column(DateTime, nullable=True)