from celery import Celery
from pdf_processor import process_pdf

app = Celery('pdf_processor', broker='redis://localhost:6379/0')

@app.task
def process_pdf_task(pdf_path):
    return process_pdf(pdf_path)
