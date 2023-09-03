#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           username,
                           password,
                           database),
                           pool_pre_ping=True
                           )
    Base.metadata.create_all(engine)
    session = Session(engine)
    delete_state = session.query(
                                 State).filter(
                                 State.name.contains("%a%")).all()
    for row in delete_state:
        session.delete(row)
    session.commit()
    session.close()
