from fastapi import FastAPI
from sqlalchemy import  Column, Integer, Text, String

from database import engine, Base

class Files(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    original_filename = Column(Text)
    size = Column(Integer)
    url = Column(Text)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

Base.metadata.create_all(bind=engine)
