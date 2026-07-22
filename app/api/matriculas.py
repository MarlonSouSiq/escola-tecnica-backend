from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import SessionLocal

from app.models.matriculas import Matricula as MatriculaModel
from app.models.alunos import Aluno as AlunoModel
from app.models.turmas import Turma as TurmaModel

from app.schemas.matriculas import Matricula, MatriculaCreate, MatriculaUpdate

router = APIRouter(prefix="/matriculas", tags=["Matrículas"])

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# LISTAR TODAS AS MATRÍCULAS (com nome do aluno e código da turma)
@router.get("", response_model=list[dict])
def listar_matriculas(db: Session = Depends(get_db)):
    dados = (
        db.query(
            MatriculaModel.id_matricula,
            MatriculaModel.matricula_aluno,
            MatriculaModel.id_turma,
            MatriculaModel.data_matricula,
            MatriculaModel.situacao,
            MatriculaModel.observacoes,
            func.coalesce(AlunoModel.nome, "").label("nome_aluno"),
            func.coalesce(TurmaModel.codigo_turma, "").label("codigo_turma")
        )
        .join(
            AlunoModel,
            AlunoModel.matricula == MatriculaModel.matricula_aluno,
            isouter=True
        )
        .join(
            TurmaModel,
            TurmaModel.id_turma == MatriculaModel.id_turma,
            isouter=True
        )
        .all()
    )

    resultado = []
    for row in dados:
        resultado.append({
            "id_matricula": row.id_matricula,
            "matricula_aluno": row.matricula_aluno,
            "id_turma": row.id_turma,
            "codigo_turma": row.codigo_turma,
            "data_matricula": row.data_matricula,
            "situacao": row.situacao,
            "observacoes": row.observacoes,
            "nome_aluno": row.nome_aluno,
        })

    return resultado


# OBTER UMA MATRÍCULA PELO ID
@router.get("/{id_matricula}", response_model=Matricula)
def obter_matricula(id_matricula: int, db: Session = Depends(get_db)):
    matricula = (
        db.query(MatriculaModel)
        .filter(MatriculaModel.id_matricula == id_matricula)
        .first()
    )

    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")

    return matricula


# CRIAR MATRÍCULA
@router.post("", response_model=Matricula, status_code=201)
def criar_matricula(dados: MatriculaCreate, db: Session = Depends(get_db)):
    matricula = MatriculaModel(**dados.dict())
    db.add(matricula)
    db.commit()
    db.refresh(matricula)
    return matricula


# ATUALIZAR MATRÍCULA
@router.put("/{id_matricula}", response_model=Matricula)
def atualizar_matricula(id_matricula: int, dados: MatriculaUpdate, db: Session = Depends(get_db)):
    matricula = (
        db.query(MatriculaModel)
        .filter(MatriculaModel.id_matricula == id_matricula)
        .first()
    )

    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")

    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(matricula, campo, valor)

    db.commit()
    db.refresh(matricula)
    return matricula


# EXCLUIR MATRÍCULA
@router.delete("/{id_matricula}", status_code=204)
def excluir_matricula(id_matricula: int, db: Session = Depends(get_db)):
    matricula = (
        db.query(MatriculaModel)
        .filter(MatriculaModel.id_matricula == id_matricula)
        .first()
    )

    if not matricula:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")

    db.delete(matricula)
    db.commit()
