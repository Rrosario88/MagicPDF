# PDF Data Extraction and Processing System

This project implements a system for extracting structured data from PDFs, with the goal of using this data in a Retrieval-Augmented Generation (RAG) application.

## Features

- PDF text and structure extraction
- Data preprocessing and cleaning
- Named Entity Recognition (NER)
- Relationship extraction
- Table extraction and structuring
- Metadata extraction
- Database integration
- API for PDF processing
- Batch processing system

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Set up the database: `python -c "from data_models import Base, engine; Base.metadata.create_all(engine)"`
6. Run the application: `python main.py`

## Usage

To process a PDF, send a POST request to `/process_pdf` with the PDF file in the request body.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
