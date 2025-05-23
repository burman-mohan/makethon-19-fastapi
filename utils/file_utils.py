import os
import zipfile
from fastapi import UploadFile

def extract_zip_files(files: list[UploadFile]) -> list[str]:
    path_array = []
    for file in files:
        if file.content_type == 'application/zip':
            os.makedirs("res_code", exist_ok=True)
            with zipfile.ZipFile(file.file, 'r') as zip_ref:
                os.makedirs(f"res_code/{file.filename.split('.')[0]}", exist_ok=True)
                zip_ref.extractall(f"res_code/{file.filename.split('.')[0]}")
                extracted_path = os.path.abspath(f"res_code/{file.filename.split('.')[0]}")
                path_array.append(extracted_path)
    return path_array