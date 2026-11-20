from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

import os

from services.sql_parser import extract_tables
from services.sql_parser import extract_schema
from services.sql_parser import infer_relationships

router = APIRouter()


@router.post("/upload-sql")
async def upload_sql(file: UploadFile = File(...)):

    os.makedirs("uploads", exist_ok=True)

    content = await file.read()

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        buffer.write(content)

    sql_text = content.decode("utf-8")

    tables = extract_tables(sql_text)

    schema = extract_schema(sql_text)
    relationships = infer_relationships(schema)

    return {
        "filename": file.filename,
        "size_bytes": len(content),
        "tables_found": tables,
        "schema": schema,
        "relationships": relationships
    }