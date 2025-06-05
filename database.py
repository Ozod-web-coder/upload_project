from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:1234@db:5432/p_db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

class Base(DeclarativeBase):
    pass
