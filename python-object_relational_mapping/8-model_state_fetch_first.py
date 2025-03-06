#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <mysql_username> <mysql_password> <database_name>")
        return
    
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost:3306/{database_name}')

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if first_state is None:
        print("Nothing")
    else:
        print(f"{first_state.id}: {first_state.name}")
    session.close()

if __name__ == "__main__":
    main()
