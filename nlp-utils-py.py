import re
import spacy
from nltk.tokenize import word_tokenize, sent_tokenize

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Tokenize into sentences and words
    sentences = sent_tokenize(text)
    words = [word_tokenize(sentence) for sentence in sentences]
    
    return sentences, words

def perform_ner(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

def extract_relationships(text):
    doc = nlp(text)
    relationships = []
    for sent in doc.sents:
        for token in sent:
            if token.dep_ == "nsubj" and token.head.pos_ == "VERB":
                subject = token.text
                verb = token.head.text
                for child in token.head.children:
                    if child.dep_ == "dobj":
                        obj = child.text
                        relationships.append((subject, verb, obj))
    return relationships
