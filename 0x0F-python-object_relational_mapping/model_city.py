#!/usr/bin/python3
"""
class definition of city, similar to state
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """ City class """
    __tablename__ = 'cities'
    id = Column(
                Integer,
                autoincrement=True,
                unique=True,
                nullable=False,
                primary_key=True
                )
    name = Column(
                  String(128),
                  nullable=False
                  )
    state_id = Column(
                      Integer,
                      ForeignKey("states.id"),
                      nullable=False,
                      )
