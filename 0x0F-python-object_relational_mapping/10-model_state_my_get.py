#!/usr/bin/python3
"""
prints the State object with the name passed as argument from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    param = argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(
        State.name.like(param)).first()
    if state is None:
        print("Not found")
    print(state.id)
    session.close()
