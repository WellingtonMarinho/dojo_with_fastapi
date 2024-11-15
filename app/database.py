import os

from sqlmodel import SQLModel, create_engine, Session


database = os.getenv('DATABASE_NAME')
db_user = os.getenv('DATABASE_USER')
db_password = os.getenv('DATABASE_PASSWORD')
db_host = os.getenv('DATABASE_HOST')

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:5432/{database}"

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
