#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy Base and links to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, backref, declarative_base

Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.

   __tablename__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete")
