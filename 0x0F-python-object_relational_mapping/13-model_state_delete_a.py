#!/usr/bin/python3
"""
Script that deletes all States with letter 'a' in thier name
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    delete_state = session.query(State).filter(
                    State.name.ilike('%a%')).delete()

    session.commit()
    session.close()
