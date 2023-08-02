from sqlmodel import create_engine, Session  # add SessionLocal
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def get_db_url():
    return getenv("DATABASE_URL")

engine = create_engine(get_db_url())

# add this function to create a new session
def get_db():
    with Session(engine) as session:
        yield session
