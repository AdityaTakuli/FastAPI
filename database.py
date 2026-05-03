from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:SambaSadashiv@localhost:5432/FastAPI-Testing"
engine = create_engine(db_url)
session = sessionmaker(autocommit = False, autoflush= False, bind = engine)