import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

# URL de conexão com o banco PostgreSQL rodando no Docker
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql+psycopg://admin:adminpassword@localhost:5432/pratica_juridica"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Injeção de dependência do banco para o FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()