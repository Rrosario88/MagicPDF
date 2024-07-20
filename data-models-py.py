from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class PDFData(Base):
    __tablename__ = 'pdf_data'

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    content = Column(JSON)

engine = create_engine('sqlite:///pdf_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def save_to_db(filename, content):
    session = Session()
    pdf_data = PDFData(filename=filename, content=content)
    session.add(pdf_data)
    session.commit()
    session.close()
