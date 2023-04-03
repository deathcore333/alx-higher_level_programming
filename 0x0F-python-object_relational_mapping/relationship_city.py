#!/usr/bin/python3
"""
Defines a class City that inherits from base, similar to State
"""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ City class """
    __tablename__ = 'cities'

    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                unique=True,
                primary_key=True
                )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False
                      )
