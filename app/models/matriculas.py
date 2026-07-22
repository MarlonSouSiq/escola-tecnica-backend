from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from app.core.database import Base

class Matricula(Base):
    __tablename__ = "matriculas2"

    id_matricula = Column(Integer, primary_key=True, index=True)
    matricula_aluno = Column(String(20), nullable=False)
    id_turma = Column(Integer, nullable=False)
    data_matricula = Column(Date)
    situacao = Column(String(20), default="ativa")
    observacoes = Column(Text)
