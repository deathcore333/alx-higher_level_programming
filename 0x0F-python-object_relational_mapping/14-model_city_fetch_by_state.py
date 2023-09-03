#!/usr/bin/python3
"""
prints all city objects from the database
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_city import City

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
    query = session.query(State, City).join(City).order_by(City.id).all()
    for row in query:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
    session.close()
