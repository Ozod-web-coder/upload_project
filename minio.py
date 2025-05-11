from datetime import timedelta

import boto3
from botocore.client import Config
import uuid
import os

from fastapi import UploadFile, HTTPException, File

minio_client = boto3.client(
    's3',
    endpoint_url = "http://localhost:9000",
    aws_access_key_id = "minioadmin",
    aws_secret_access_key = "minioadmin",
    config = Config(signature_version='s3v4'),
    region_name = 'us-east-1'
)

BUCKET_NAME = "files"

ALLOWED_EXTENSIONS = {".dcm",".jpg",".jpeg",".png",".pdf"}

async def upload_and_get_url(file):
    _, ext = os.path.splitext(file.filename.lower())
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Недопустимый тип файла: {ext}")


    content = await file.read()
    file_size = len(content)


    unique_filename = f"{uuid.uuid4()}{ext}"


    minio_client.put_object(
        Bucket=BUCKET_NAME,
        Key=unique_filename,
        Body=content,
        ContentType=file.content_type
    )


    url = minio_client.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': BUCKET_NAME, 'Key': unique_filename},
        ExpiresIn=int(timedelta(days=1).total_seconds())
    )

    return {
        "filename": unique_filename,
        "size_bytes": file_size,
        "url": url
    }





