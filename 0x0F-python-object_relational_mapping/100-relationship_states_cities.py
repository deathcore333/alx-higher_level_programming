#!/usr/bin/python3
"""
creates the state of 'California' with the City 'San Fransisco'
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = "California"
    new_city = "San Francisco"
    newState = State(name=new_state)
    newCity = City(name=new_city, state=newState)

    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
