from pydantic import BaseModel
from datetime import date

class AlunoBase(BaseModel):
    matricula: str | None = None
    nome: str | None = None
    cpf: str | None = None
    rg: str | None = None
    data_nascimento: date | None = None
    sexo: str | None = None
    telefone: str | None = None
    email: str | None = None
    cep: str | None = None
    endereco: str | None = None
    numero: str | None = None
    bairro: str | None = None
    cidade: str | None = None
    estado: str | None = None
    nome_pai: str | None = None
    nome_mae: str | None = None
    telefone_responsavel: str | None = None
    email_responsavel: str | None = None
    cuidados_especiais: str | None = None
    observacoes: str | None = None
    status: str | None = None

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(AlunoBase):
    pass

class Aluno(AlunoBase):
    id_aluno: int

    class Config:
        from_attributes = True
