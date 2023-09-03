#!/usr/bin/python3
"""
creates the State “California” with the City “San Francisco” from the database
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

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

    new_state = "California"
    new_city = "San Francisco"
    newState = State(name=new_state)
    newCity = City(name=new_city, state=newState)

    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
