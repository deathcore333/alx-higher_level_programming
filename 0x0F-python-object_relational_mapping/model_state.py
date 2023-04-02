#!/usr/bin/python3
"""
This module defines a State class that represents a table in a MySQL database, with columns for an auto-generated,
unique integer ID and a string name with a maximum length of 128 characters. The class inherits from SQLAlchemy's
declarative_base() function and is linked to the 'states' table in the database.

The module requires the following dependencies:
    - SQLAlchemy

Example usage:
    python3 my_module.py <username> <password> <database_name>
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
        __tablename__ (str): The name of the database table that the class maps to.
        id (int): An auto-generated, unique integer ID for the State object. This is a primary key and can't be null.
        name (str): A string representing the name of the State. It has a maximum length of 128 characters and can't be null.
    """
    __tablename__ = 'states'
    id = column(integer, primary_key=True, autoincrement=True)
    name = column(string(128), nullable=False)


Base.metadata.create_all(engine)
