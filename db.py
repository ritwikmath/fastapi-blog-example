import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from functools import lru_cache

DB_HOST=os.getenv("DB_HOST")
DB_USER=os.getenv("DB_USER")
DB_PASS=os.getenv("DB_PASS")
DB_DATABASE=os.getenv("DB_DATABASE")
DB_PORT=os.getenv("DB_PORT")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@lru_cache(maxsize=None) # Check https://www.cockroachlabs.com/blog/what-is-connection-pooling/
def get_db(resource: str) -> Session:
    session = SessionLocal()
    return session