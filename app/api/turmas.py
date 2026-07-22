from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.turmas import Turma as TurmaModel
from app.schemas.turmas import Turma, TurmaCreate, TurmaUpdate

router = APIRouter(prefix="/turmas", tags=["Turmas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Turma])
def listar_turmas(db: Session = Depends(get_db)):
    return db.query(TurmaModel).all()

@router.get("/{id_turma}", response_model=Turma)
def obter_turma(id_turma: int, db: Session = Depends(get_db)):
    turma = db.query(TurmaModel).filter(TurmaModel.id_turma == id_turma).first()
    if not turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return turma

@router.post("/", response_model=Turma, status_code=201)
def criar_turma(dados: TurmaCreate, db: Session = Depends(get_db)):
    turma = TurmaModel(**dados.dict())
    db.add(turma)
    db.commit()
    db.refresh(turma)
    return turma

@router.put("/{id_turma}", response_model=Turma)
def atualizar_turma(id_turma: int, dados: TurmaUpdate, db: Session = Depends(get_db)):
    turma = db.query(TurmaModel).filter(TurmaModel.id_turma == id_turma).first()
    if not turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")

    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(turma, campo, valor)

    db.commit()
    db.refresh(turma)
    return turma

@router.delete("/{id_turma}", status_code=204)
def excluir_turma(id_turma: int, db: Session = Depends(get_db)):
    turma = db.query(TurmaModel).filter(TurmaModel.id_turma == id_turma).first()
    if not turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")

    db.delete(turma)
    db.commit()
