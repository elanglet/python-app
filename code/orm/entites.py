# -*- coding: utf-8 -*-

'''
Created on 27 juin 2018

@author: Etienne
'''
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

Base = declarative_base()
class Client(Base):
    
    __tablename__ = 'client'
    
    idclient = Column('idclient', Integer(), primary_key=True)
    nom = Column('nom', String(100), nullable=False)
    adresse = Column('adresse', String(200), nullable=False)
    codepostal = Column('codepostal', String(10), nullable=False)
    ville = Column('ville', String(100), nullable=False)
    activite = Column('activite', String(200), nullable=False)
    
