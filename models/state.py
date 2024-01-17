#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import models
from sqlalchemy import String
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from models.city import City
from os import getenv
from sqlalchemy.orm import relationship

class State(BaseModel):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade='all, delete')

    @property
    def cities(self):
        """cites"""
        list = []
        ac = models.storage.all(City)
        for i in ac:
            if ac[i] == self.id:
                nlist.append(ac[i])
        return nlist
