from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.usuario import Usuario, MatriculaEstagio, PerfilEnum
from app.schemas.aluno import AlunoCreate, AlunoResponse

router = APIRouter(
    prefix="/alunos",
    tags=["Alunos"]
)

@router.get("/", response_model=List[AlunoResponse])
def listar_alunos(db: Session = Depends(get_db)):
    alunos = db.query(Usuario).filter(
        Usuario.perfil == PerfilEnum.ALUNO,
        Usuario.deletado_em.is_(None)
    ).all()
    return alunos

@router.post("/", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def criar_aluno(aluno_data: AlunoCreate, db: Session = Depends(get_db)):
    # Verificar se e-mail já existe
    usuario_existente = db.query(Usuario).filter(Usuario.email == aluno_data.email).first()
    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="Já existe um utilizador registado com este e-mail."
        )

    # Nota: Em produção, aplicar hash na senha (ex: Argon2/Bcrypt)
    novo_aluno = Usuario(
        nome=aluno_data.nome,
        email=aluno_data.email,
        senha_hash=aluno_data.senha,
        perfil=PerfilEnum.ALUNO,
        ativo=True
    )
    db.add(novo_aluno)
    db.commit()
    db.refresh(novo_aluno)

    # Regista a matrícula do estágio supervisionado (RN02)
    matricula = MatriculaEstagio(
        aluno_id=novo_aluno.id,
        disciplina=aluno_data.disciplina or "Estágio Supervisionado",
        periodo=aluno_data.periodo or "2026.2",
        ativa=True
    )
    db.add(matricula)
    db.commit()

    return novo_alunos