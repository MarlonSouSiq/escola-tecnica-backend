from pydantic import BaseModel

class CursoBase(BaseModel):
    nome: str | None = None
    carga_horaria: int | None = None
    modalidade: str | None = None
    eixo_tecnologico: str | None = None
    duracao_meses: int | None = None
    turno: str | None = None
    status: str | None = None

class CursoCreate(CursoBase):
    pass

class CursoUpdate(CursoBase):
    pass

class Curso(CursoBase):
    id_curso: int

    class Config:
        orm_mode = True
