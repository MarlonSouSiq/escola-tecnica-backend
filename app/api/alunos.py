from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.alunos import Aluno as AlunoModel
from app.schemas.alunos import Aluno, AlunoCreate, AlunoUpdate

router = APIRouter(prefix="/alunos", tags=["Alunos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Aluno])
def listar_alunos(
    matricula: str | None = None,
    nome: str | None = None,
    cpf: str | None = None,
    rg: str | None = None,
    sexo: str | None = None,
    telefone: str | None = None,
    email: str | None = None,
    cep: str | None = None,
    endereco: str | None = None,
    numero: str | None = None,
    bairro: str | None = None,
    cidade: str | None = None,
    estado: str | None = None,
    nome_pai: str | None = None,
    nome_mae: str | None = None,
    telefone_responsavel: str | None = None,
    email_responsavel: str | None = None,
    cuidados_especiais: str | None = None,
    observacoes: str | None = None,
    status: str | None = None,
    db: Session = Depends(get_db),
):
    query = db.query(AlunoModel)

    filtros = {
        "matricula": matricula,
        "nome": nome,
        "cpf": cpf,
        "rg": rg,
        "sexo": sexo,
        "telefone": telefone,
        "email": email,
        "cep": cep,
        "endereco": endereco,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "nome_pai": nome_pai,
        "nome_mae": nome_mae,
        "telefone_responsavel": telefone_responsavel,
        "email_responsavel": email_responsavel,
        "cuidados_especiais": cuidados_especiais,
        "observacoes": observacoes,
        "status": status,
    }

    for campo, valor in filtros.items():
        if valor:
            query = query.filter(getattr(AlunoModel, campo).ilike(f"%{valor}%"))

    return query.all()

@router.get("/{id_aluno}", response_model=Aluno)
def obter_aluno(id_aluno: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id_aluno == id_aluno).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.post("/", response_model=Aluno, status_code=201)
def criar_aluno(dados: AlunoCreate, db: Session = Depends(get_db)):
    aluno = AlunoModel(**dados.dict())
    db.add(aluno)
    db.commit()
    db.refresh(aluno)
    return aluno

@router.put("/{id_aluno}", response_model=Aluno)
def atualizar_aluno(id_aluno: int, dados: AlunoUpdate, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id_aluno == id_aluno).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(aluno, campo, valor)

    db.commit()
    db.refresh(aluno)
    return aluno

@router.delete("/{id_aluno}", status_code=204)
def excluir_aluno(id_aluno: int, db: Session = Depends(get_db)):
    aluno = db.query(AlunoModel).filter(AlunoModel.id_aluno == id_aluno).first()
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    db.delete(aluno)
    db.commit()
