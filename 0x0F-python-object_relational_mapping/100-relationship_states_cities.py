#!/usr/bin/python3
"""
creates the state of 'California' with the City 'San Fransisco'
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    newState = State(name="California")
    newCity = City(name="San Francisco", state=newState)
    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
