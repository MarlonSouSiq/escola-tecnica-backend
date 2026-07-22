from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.models.cursos import Curso as CursoModel
from app.schemas.cursos import Curso, CursoCreate, CursoUpdate

router = APIRouter(prefix="/cursos", tags=["Cursos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[Curso])
def listar_cursos(db: Session = Depends(get_db)):
    return db.query(CursoModel).all()

@router.get("/{id_curso}", response_model=Curso)
def obter_curso(id_curso: int, db: Session = Depends(get_db)):
    curso = db.query(CursoModel).filter(CursoModel.id_curso == id_curso).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@router.post("/", response_model=Curso, status_code=201)
def criar_curso(dados: CursoCreate, db: Session = Depends(get_db)):
    curso = CursoModel(**dados.dict())
    db.add(curso)
    db.commit()
    db.refresh(curso)
    return curso

@router.put("/{id_curso}", response_model=Curso)
def atualizar_curso(id_curso: int, dados: CursoUpdate, db: Session = Depends(get_db)):
    curso = db.query(CursoModel).filter(CursoModel.id_curso == id_curso).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(curso, campo, valor)

    db.commit()
    db.refresh(curso)
    return curso

@router.delete("/{id_curso}", status_code=204)
def excluir_curso(id_curso: int, db: Session = Depends(get_db)):
    curso = db.query(CursoModel).filter(CursoModel.id_curso == id_curso).first()
    if not curso:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    db.delete(curso)
    db.commit()
