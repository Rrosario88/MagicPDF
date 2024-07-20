import os
import fitz
from pdf_extract_kit import PDFExtractKit
from multiprocessing import Pool
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from langchain import OpenAI, LLMChain, PromptTemplate
import streamlit as st
from dotenv import load_dotenv

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

load_dotenv()  # Load environment variables

# 1. Improved PDF Processing
def process_pdf(pdf_path):
    extractor = PDFExtractKit()
    text_pdf_extract = extractor.extract_text(pdf_path)
    
    doc = fitz.open(pdf_path)
    text_pymupdf = ""
    for page in doc:
        text_pymupdf += page.get_text()
    
    return text_pdf_extract + " " + text_pymupdf

def process_pdfs_parallel(pdf_paths):
    with Pool() as pool:
        texts = pool.map(process_pdf, pdf_paths)
    return texts

# 2. Enhanced Text Processing
def process_text(text):
    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    processed_tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    return " ".join(processed_tokens)

# 3. Improved Embedding and Vector Search
model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(texts):
    return model.encode(texts)

def search_similar(query, embeddings, texts, top_k=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    return [texts[i] for i in top_indices]

# 4. LLM Integration
def setup_llm():
    llm = OpenAI(temperature=0)
    template = """Question: {question}
    Context: {context}
    Answer: Let's approach this step-by-step:
    """
    prompt = PromptTemplate(template=template, input_variables=["question", "context"])
    return LLMChain(llm=llm, prompt=prompt)

# 5. Query Function
def query_llm(embeddings, texts, llm_chain, query):
    similar_texts = search_similar(query, embeddings, texts)
    context = "\n".join(similar_texts)
    return llm_chain.run(question=query, context=context)

# Streamlit UI
def main():
    st.title("Enhanced PDF-based RAG Application")

    # File uploader
    uploaded_files = st.file_uploader("Choose PDF files", accept_multiple_files=True, type="pdf")

    if uploaded_files:
        # Process PDFs
        pdf_paths = [file.name for file in uploaded_files]
        texts = process_pdfs_parallel(pdf_paths)
        processed_texts = [process_text(text) for text in texts]

        # Create embeddings
        embeddings = create_embeddings(processed_texts)

        # Setup LLM
        llm_chain = setup_llm()

        # Query input
        query = st.text_input("Enter your question:")

        if query:
            response = query_llm(embeddings, processed_texts, llm_chain, query)