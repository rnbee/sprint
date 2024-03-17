from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALHEMY_DB_URL = "postgresql+psycopg2://postgres:post@localhost/sprint"

engine = create_engine(SQLALHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
