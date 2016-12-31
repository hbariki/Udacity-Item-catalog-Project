import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):

    __tablename__ = 'restaurant'


    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):

   __tablename__ = 'menu_item'


   id = Column(Integer, primary_key=True)
   name = Column(String(250), nullable=False)
   description = Column(String(250), nullable=False)
   price = Column(String(8))
   course = Column(String(250), nullable=False)
   restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
   restaurant = relationship(Restaurant)
                          

engine = create_engine('sqlite:///restaurant.db')


Base.metadata.create_all(engine)                          
