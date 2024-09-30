from PyPDF2 import PdfReader
from fastapi import UploadFile, HTTPException

async def extract_text_from_pdf(pdf_file: UploadFile):
    try:
        pdf_reader = PdfReader(pdf_file.file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
