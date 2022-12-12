from apps.config import settings
from sqlmodel import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USERNAME = settings.DB_USERNAME
DB_PASSWORD = settings.DB_PASSWORD
DB_HOST = settings.DB_HOST
DB_PORT = settings.DB_PORT
DB_DATABASE = settings.DB_DATABASE
DB_URL = settings.DB_URL

engine = create_engine(DB_URL,echo=False, pool_pre_ping=True, pool_recycle=280)

#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
