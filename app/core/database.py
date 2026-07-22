from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = (
    "postgresql+psycopg2://postgres.tbfdgliarpnswugouhfg:NLXA%2Fjm9K%24C%406Ey"
    "@aws-0-ca-central-1.pooler.supabase.com:5432/postgres"
)

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
