from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Prazo(Base):
    __tablename__ = "prazos"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(255), nullable=False)  # Ex: "Contestação", "Apresentação de Documentos"
    data_vencimento = Column(DateTime, nullable=False)
    status = Column(String(50), default="PENDENTE", nullable=False)  # PENDENTE, CONCLUIDO, ATRASADO
    
    # Amarrações essenciais
    caso_juridico_id = Column(Integer, ForeignKey("casos_juridicos.id"), nullable=False)
    caso_juridico = relationship("CasoJuridico", backref="prazos")
    
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)