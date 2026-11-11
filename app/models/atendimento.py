from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Atendimento(Base):
    __tablename__ = "atendimento"

    id = Column(Integer, primary_key=True, index=True)
    relato = Column(Text, nullable=False)
    
    caso_juridico_id = Column(Integer, ForeignKey("caso_juridico.id"), nullable=False)
    assistido_id = Column(Integer, ForeignKey("assistido.id"), nullable=False)
    aluno_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)
    
    data_hora = Column(DateTime, default=datetime.utcnow, nullable=False)
    deletado_em = Column(DateTime, nullable=True)