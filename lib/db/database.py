from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///shop.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def setup_database():
    Base.metadata.create_all(engine)
    return Session()
