#!/usr/bin/python3
"""
Contains the class definition of State an instance of
Base = declarative_base()
"""

from sqlalchemy import create_engine, Integer, column, string
import sys
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2], sys.argv[3]),
                       pool_pre_ping=True)


class State(Base):
     """
    Represents a State object that is linked to a MySQL database table.

    Attributes:
        __tablename__ (str): database name.
        id (int): An auto-generated, unique integer
        name (str): string representing state name
    """
    __tablename__ = 'states'
    id = column(integer, primary_key=True, autoincrement=True)
    name = column(string(128), nullable=False)


Base.metadata.create_all(engine)
