from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import alunos
from app.api import cursos
from app.api import turmas
from app.api import matriculas

from app.core.database import Base, engine

# Cria as tabelas no banco automaticamente
#main.pyBase.metadata.create_all(bind=engine)

app = FastAPI(
    title="Escola Técnica API",
    version="1.0.0",
    description="Backend da Escola Técnica"
)

# Configuração de CORS para permitir o frontend React
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas
app.include_router(alunos.router)
app.include_router(cursos.router)
app.include_router(turmas.router)
app.include_router(matriculas.router)

@app.get("/")
def root():
    return {"status": "Backend funcionando!"}
