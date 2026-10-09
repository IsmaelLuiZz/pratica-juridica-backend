from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker



# Substitui com as tuas credenciais do PostgreSQL (se necessário)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/projeto_juridico"



engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



Base = declarative_base()



# Dependência para obter a sessão da base de dados nas rotas

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close() 

