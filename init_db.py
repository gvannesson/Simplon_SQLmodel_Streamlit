import sqlite3
from sqlmodel import Session, SQLModel, create_engine, select
from models import  *

sqlite_file_name = "poigne_database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"


engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def main():
    create_db_and_tables()

if __name__ == "__main__":
    main()