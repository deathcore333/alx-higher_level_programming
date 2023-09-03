#!/usr/bin/python3
"""
lists all City objects from the database
"""
from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from relationship_city import Base, City
from relationship_state import State
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

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
