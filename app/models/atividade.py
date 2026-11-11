from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class Atividade(Base):
    __tablename__ = "atividade"

    id = Column(Integer, primary_key=True, index=True)
    descricao = Column(String(255), nullable=False) # Ex: "Elaborar minuta da petição inicial"
    status = Column(String(50), default="PENDENTE", nullable=False) # PENDENTE, CONCLUIDO
    
    # Amarrações essenciais
    caso_juridico_id = Column(Integer, ForeignKey("caso_juridico.id"), nullable=False)
    responsavel_id = Column(Integer, ForeignKey("usuario.id"), nullable=False) # Aluno responsável pela tarefa
    
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)
    deletado_em = Column(DateTime, nullable=True) # Exclusão lógica (RN04)