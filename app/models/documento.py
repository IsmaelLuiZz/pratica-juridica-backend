from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    tipo = Column(String(100), nullable=False)  # Ex: Petição, Procuração, Termo
    caminho_arquivo = Column(String(500), nullable=True)  # URL ou caminho no servidor/storage
    descricao = Column(Text, nullable=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamento com o Caso Jurídico
    caso_juridico_id = Column(Integer, ForeignKey("casos_juridicos.id"), nullable=False)
    caso_juridico = relationship("CasoJuridico", backref="documentos")