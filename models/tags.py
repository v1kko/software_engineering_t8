# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:01:46 2013

@author: David Schoorisse & Mustafa Karaalioglu
"""

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Sequence, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()

class TagNames(Base):
    __tablename__ = 'TagNames'
    
    id = Column(Integer, Sequence('id'), primary_key=True, unique=True)
    name = Column(String(32))
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        if self.id is None:
            return "<Tag('None', '%s')>" % (self.name)
        else:
            return "<Tag('%d', '%s')>" % (self.id, self.name)


Base.metadata.create_all(engine)

session = Session()

test_tag = TagNames('test')
print test_tag
session.add(test_tag)

tag = session.query(TagNames).filter_by(name='test').first()
print tag