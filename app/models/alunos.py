from sqlalchemy import Column, Integer, String, Date
from app.core.database import Base

class Aluno(Base):
    __tablename__ = "alunos"

    id_aluno = Column(Integer, primary_key=True, index=True)
    matricula = Column(String(20), unique=True, nullable=False, index=True)
    nome = Column(String(150), nullable=False, index=True)
    cpf = Column(String(14), index=True)
    rg = Column(String(20))
    data_nascimento = Column(Date)
    sexo = Column(String(1))
    telefone = Column(String(20))
    email = Column(String(150), index=True)
    cep = Column(String(9))
    endereco = Column(String(150))
    numero = Column(String(10))
    bairro = Column(String(80))
    cidade = Column(String(80), index=True)
    estado = Column(String(2))
    nome_pai = Column(String(150))
    nome_mae = Column(String(150))
    telefone_responsavel = Column(String(20))
    email_responsavel = Column(String(150))
    cuidados_especiais = Column(String)
    observacoes = Column(String)
    status = Column(String(20), default="ativo", index=True)
