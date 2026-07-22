from sqlalchemy import Column, Integer, String
from app.core.database import Base

class Curso(Base):
    __tablename__ = "cursos2"

    id_curso = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=True)
    carga_horaria = Column(Integer, nullable=True)
    modalidade = Column(String, nullable=True)
    eixo_tecnologico = Column(String, nullable=True)
    duracao_meses = Column(Integer, nullable=True)
    turno = Column(String, nullable=True)
    status = Column(String, nullable=True)
