from fastapi import FastAPI, UploadFile, File, Depends, Form

import auth
import schemas
from database import db
from minio import upload_and_get_url
from models import *

print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
Base.metadata.create_all(bind=engine)
app = FastAPI()




@app.post("/upload")
async def upload_file(file: UploadFile = File(...),file_name: str = Form(...)):
    data = await upload_and_get_url(file)
    file = Files(original_filename=file_name,size=data.get("size_bytes"), url=data.get("url"))
    db.add(file)
    db.commit()


@app.get("/get_files")
def get_files():
    return db.query(Files).all()



@app.get("/get_files/{user_id}")
def get_files(user_id: int):
    return db.query(Files).filter(Files.user_id == user_id).all()


@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate):
    return auth.register_user(user)


@app.post("/login")
def login(user: schemas.UserCreate):
    return auth.login_user(user)