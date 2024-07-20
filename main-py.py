import logging
from pdf_processor import process_pdf
from api import app

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting PDF processing application")
    # Add any initialization code here
    app.run(debug=True)

if __name__ == "__main__":
    main()
