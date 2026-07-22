from pydantic import BaseModel

class TurmaBase(BaseModel):
    id_curso: int
    codigo_turma: str
    semestre: int | None = None
    ano: int | None = None
    serie: str | None = None
    turno: str | None = None
    sala: str | None = None
    vagas: int | None = None
    status: str | None = "ativa"

class TurmaCreate(TurmaBase):
    pass

class TurmaUpdate(BaseModel):
    id_curso: int | None = None
    codigo_turma: str | None = None
    semestre: int | None = None
    ano: int | None = None
    serie: str | None = None
    turno: str | None = None
    sala: str | None = None
    vagas: int | None = None
    status: str | None = None

class Turma(TurmaBase):
    id_turma: int

    class Config:
        orm_mode = True
