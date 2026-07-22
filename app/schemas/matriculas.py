from pydantic import BaseModel
from datetime import date

class MatriculaBase(BaseModel):
    matricula_aluno: int
    id_turma: int
    data_matricula: date | None = None
    situacao: str | None = None
    observacoes: str | None = None

class MatriculaCreate(MatriculaBase):
    pass

class MatriculaUpdate(BaseModel):
    matricula_aluno: int | None = None
    id_turma: int | None = None
    data_matricula: date | None = None
    situacao: str | None = None
    observacoes: str | None = None

class Matricula(MatriculaBase):
    id_matricula: int

    class Config:
        orm_mode = True
