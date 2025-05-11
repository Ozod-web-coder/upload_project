from fastapi import FastAPI, UploadFile, File, Depends

import auth
import schemas
from database import db
from minio import upload_and_get_url
from models import Files, User

app = FastAPI()




@app.post("/upload")
async def upload_file(file: UploadFile = File(...), current_user: User = Depends(auth.get_current_user)):
    data = await upload_and_get_url(file)
    file = Files(original_filename=data.get("filename"),size=data.get("size_bytes"), url=data.get("url"))
    db.add(file)
    db.commit()




@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate):
    return auth.register_user(user)


@app.post("/login")
def login(user: schemas.UserCreate):
    return auth.login_user(user)