from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from datetime import datetime
from app.database import Base

class CasoJuridico(Base):
    __tablename__ = "caso_juridico"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(250), nullable=False)
    descricao = Column(Text, nullable=False)
    status = Column(String(50), default="EM_ANDAMENTO", nullable=False) # Ex: EM_ANDAMENTO, AGUARDANDO_APROVACAO, ENCERRADO[cite: 6]
    
    # Chaves estrangeiras para as amarrações do processo
    assistido_id = Column(Integer, ForeignKey("assistido.id"), nullable=False)
    aluno_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)       # Estagiário responsável[cite: 6]
    professor_id = Column(Integer, ForeignKey("usuario.id"), nullable=False)   # Professor orientador[cite: 6]
    
    criado_em = Column(DateTime, default=datetime.utcnow)
    deletado_em = Column(DateTime, nullable=True) # Exclusão lógica (RN04)[cite: 6]