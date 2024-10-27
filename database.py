from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

POSTGRESQL_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}'

engine = create_engine(
    POSTGRESQL_DATABASE_URL, connect_args={"client_encoding": "utf8"}
)
# , connect_args={"check_same_thread": False}
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
