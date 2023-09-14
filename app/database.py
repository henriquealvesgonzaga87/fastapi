from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
#import psycopg2
#from psycopg2.extras import RealDictCursor
#from time import sleep

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

#while True:
 #   try:
        #conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='admin1234', cursor_factory=RealDictCursor)
        #cursor = conn.cursor()
        #print("Connection to database was succesfull")
        #break

    #except Exception as error:
        #print("Connection to database failed")
        #print(f"Error: {error}")
        #sleep(2)