'''
Created on 19 juil. 2018

@author: Etienne
'''

import unittest
from test.TestCases import TestCalculatrice, TestVoiture

if __name__ == '__main__':
    
    # Créer la suite de test
    suite = unittest.TestSuite()
    
    # Ajouter les tests à la suite
    # (On ajoute des INSTANCES) des classes de tests 
    suite.addTest(TestCalculatrice())
    suite.addTest(TestVoiture())
    
    # Lancer l'exécution de la suite.
    runner = unittest.TextTestRunner()
    runner.run(suite)

