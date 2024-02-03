from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALHEMY_DB_URL = 'postgresql+psycopg2://postres:true7#90@localhost/postgres'

engine = create_engine(SQLALHEMY_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflash=False, bind=engine)

Base = declarative_base()