#!/usr/bin/python3
"""
Start link class to table in database
"""
from sqlalchemy import create_engine
import sys
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)


class State(Base):
    """ Defines a class State that inherits from Base """
    __tablename__ = 'states'
    id = column(integer, primary_key=True, autoincrement=True)
    name = column(string(128), nullable=False)


Base.metadata.create_all(engine)
