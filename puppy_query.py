from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from puppies import Base, Puppy, Shelter

import datetime

engine = create_engine('sqlite:///puppyshelter.db')


Base.metadata.bind = engine


DBSession = sessionmaker(bind = engine)


session = DBSession()



def query_one():
      """Query all of the puppies and return results in ascending alphabetical order"""
    puppies = session.query(Puppy).order_by(puppy.name).all()


        for puppy in puppies:
          print puppy.name
          print puppy.id
          print "/n"             

def query_two():
      """Query all of the puppies that are less than 6 months old organized by the youngest first"""
      sixMonthsAgo = datetime.date.today()-datetime.timedelta(6*365/12)
      puppies = session.query(Puppy).filter(Puppy.dateOfBirth > sixMonthsAgo).order_by(Puppy.dateOfBirth.desc()).all()
      for puppy in puppies:
          print puppy.name
          print puppy.dateOfBirth

def query_three():
    """ Query all puppies by ascending weight """
    puppies = session.query(Puppy).order_by(Puppy.weight).all()

    for puppy in puppies:
        print puppy.name
        print puppy.weight
                       
def query_four():
    """ Query all puppies grouped by the shelter in which they are staying"""

    puppies = session.query(Puppy).order_by(Puppy.shelter_id).all()

    for puppy in puppies:
        print puppy.name
        print puppy.shelter_id


#query_one()
#query_two()
#query_three()
#query_four()                       
                       
                       
                       

                       
      
                       
