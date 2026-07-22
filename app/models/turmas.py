from sqlalchemy import Column, Integer, String, SmallInteger, ForeignKey
from app.core.database import Base

class Turma(Base):
    __tablename__ = "turmas2"

    id_turma = Column(Integer, primary_key=True, index=True)
    id_curso = Column(Integer, ForeignKey("cursos2.id_curso"), nullable=False)
    codigo_turma = Column(String(20), unique=True, nullable=False)
    semestre = Column(SmallInteger)
    ano = Column(Integer)
    serie = Column(String(20))
    turno = Column(String(20))
    sala = Column(String(20))
    vagas = Column(Integer)
    status = Column(String(20), default="ativa")
