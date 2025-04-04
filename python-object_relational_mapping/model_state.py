#!/usr/bin/python3
"""
class definition module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(
        Integer,
        unique=True,
        autoincrement=True,
        primary_key=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
    )
