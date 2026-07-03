import os
import uuid
import boto3
from fastapi import UploadFile

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

s3_client = boto3.client("s3", region_name=AWS_REGION)


def upload_ticket_file(ticket_id: int, file: UploadFile) -> dict:
    if not S3_BUCKET_NAME:
        raise RuntimeError("S3_BUCKET_NAME environment variable is not set")

    original_filename = file.filename or "upload.bin"
    safe_filename = original_filename.replace(" ", "_")
    object_key = f"tickets/{ticket_id}/{uuid.uuid4()}-{safe_filename}"

    s3_client.upload_fileobj(
        file.file,
        S3_BUCKET_NAME,
        object_key,
        ExtraArgs={"ContentType": file.content_type or "application/octet-stream"},
    )

    return {
        "bucket": S3_BUCKET_NAME,
        "key": object_key,
        "filename": original_filename,
        "content_type": file.content_type,
    }
