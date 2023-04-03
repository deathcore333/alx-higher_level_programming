#!/usr/bin/python3
"""
Script that prints all City objects from database
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State, City).join(City).order_by(City.id).all()
    for row in query:
        print("{}: ({}) {}".format(row[0].name, row[1].id, row[1].name))
    session.close()
