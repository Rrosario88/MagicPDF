from pdf_extract_kit import PDFExtractor
from nlp_utils import preprocess_text, perform_ner, extract_relationships
from data_models import save_to_db

def process_pdf(pdf_path):
    # Extract content from PDF
    extractor = PDFExtractor(pdf_path)
    text = extractor.extract_text()
    tables = extractor.extract_tables()
    metadata = extractor.extract_metadata()

    # Preprocess and analyze text
    cleaned_sentences, tokenized_words = preprocess_text(text)
    entities = perform_ner(text)
    relationships = extract_relationships(text)

    # Process tables and metadata
    # (Add your table and metadata processing logic here)

    # Save processed data to database
    content = {
        "text_content": text,
        "entities": entities,
        "relationships": relationships,
        "tables": tables,
        "metadata": metadata
    }
    save_to_db(pdf_path, content)

    return content
