#!/usr/bin/python3
"""
list all State objects, and corresponding City objects,
contained in the database
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from relationship_city import City
from relationship_state import Base, State

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
    session = Session(engine)

    all_states = session.query(State).order_by(State.id).all()
    for state in all_states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("{}{}: {}".format(" "*4, city.id, city.name))

    session.close()
