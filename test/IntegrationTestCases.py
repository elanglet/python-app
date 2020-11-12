# -*- coding: utf-8 -*-

'''
Created on 19 juil. 2018

@author: Etienne
'''

import unittest
import sqlite3 as db
from code.orm.classes import ClientEntityManager, EntityNotFoundException
from code.orm.entites import Client

class TestClientEntityManager(unittest.TestCase):


    em = None

    def setUp(self):
        # On initialise le jeu de données
        with db.connect('../db/python-app.db') as conn:
            cursor = conn.cursor()
            with open('./scripts/init-db.sql') as script:
                cursor.executescript(
                    "".join(script.readlines())
                )

        self.em = ClientEntityManager()
    
    def tearDown(self):
        # On purge le jeu de données
        with db.connect('../db/python-app.db') as conn:
            cursor = conn.cursor()
            with open('./scripts/clean-db.sql') as script:
                cursor.executescript(
                    "".join(script.readlines())
                )
    
    def testAjouterClient(self):
        try:
            client = Client()
            client.nom = "Rénovation Réhabilitation Restauration"
            client.adresse = "91 Quai Emile Cormerais"
            client.codepostal = "44800"
            client.ville = "Saint-Herblain"
            client.activite = "Maçonnerie"
            self.em.ajouterClient(client)
        except Exception as e:
            self.fail(e)
    
    def testRechercherClientParId(self):
        try:
            client = self.em.rechercherClientParId(1)
            self.assertEqual(client.idclient, 1, "La valeur attendue est '1'")
            self.assertEqual(client.nom, 'ENI Service', "La valeur attendue est 'ENI Service'")
            self.assertEqual(client.adresse, '7bis Avenue Jacques Cartier', "La valeur attendue est '7bis Avenue Jacques Cartier'")
            self.assertEqual(client.codepostal, '44800', "La valeur attendue est '44800'")
            self.assertEqual(client.ville, 'Saint-Herblain', "La valeur attendue est 'Saint-Herblain'")
            self.assertEqual(client.activite, 'Formation Informatique', "La valeur attendue est 'Formation Informatique'")      
        except Exception as e:
            self.fail(e)
            
    def testRechercherClientParIdErreur(self):
        try:
            with self.assertRaises(EntityNotFoundException):
                client = self.em.rechercherClientParId(14)   
        except Exception as e:
            self.fail(e)
            
    def testRechercherTousLesClients(self):
        try:
            listeClients = self.em.rechercherTousLesClients()
            nbClients = len(listeClients)
            self.assertEqual(nbClients, 3, "La valeur attendue est 3")
            
            [ self.assertIn(
                    client.nom,
                    ['ENI Service', 'Guerin Peintures', 'Store Nantais'],
                    "Le client devrait etre dans la liste"
                ) for client in listeClients           
            ]
            
#             for client in listeClients:
#                 self.assertIn(
#                     client.nom, 
#                     ['ENI Service', 'Guerin Peintures', 'Store Nantais'], 
#                     "Le client devrait etre dans la liste"
#                 )

        except Exception as e:
            self.fail(e)
