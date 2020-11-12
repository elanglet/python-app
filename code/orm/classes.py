# -*- coding: utf-8 -*-

'''
Created on 27 juin 2018

@author: Etienne
'''
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from code.orm.entites import Client
from sqlalchemy.orm.exc import NoResultFound

class EntityNotFoundException(Exception):
    pass

class ClientEntityManager:
    
    def __connexion(self):
        url = "sqlite:///../db/python-app.db"
        
        engine = create_engine(url, encoding='utf-8')
        session = scoped_session(sessionmaker(autoflush=True))
        session.configure(bind=engine)
        
        return session

    def ajouterClient(self, client):
        session = None
        try:
            session = self.__connexion()
            session.add(client)
            session.commit()
        except:
            if session is not None:
                session.rollback()
            raise Exception("Erreur d'enregistrement du client")
        finally:
            if session is not None:
                session.close()
            
    def rechercherClientParId(self, idclient):
        session = None
        try:
            session = self.__connexion()
            return session.query(Client).filter(Client.idclient == idclient).one()

        except NoResultFound:
            raise EntityNotFoundException("Client introuvable.")
        except:
            raise Exception("Erreur de récupération du client")
        finally:
            if session is not None:
                session.close()    
            
    def rechercherTousLesClients(self):
        session = None
        try:
            session = self.__connexion()
            liste = session.query(Client).all()
            return liste
        except:
            raise Exception("Erreur de récupération de la liste des clients")
        finally:
            if session is not None:
                session.close()            

