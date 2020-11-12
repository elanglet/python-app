# -*- coding: utf-8 -*-

'''
Created on 27 juin 2018

@author: Etienne
'''
import unittest
from code.classes import Calculatrice, Voiture

class TestCalculatrice(unittest.TestCase):
    
    calculatrice = None
    
    @classmethod
    def setUpClass(cls):
#         print("DEBUT")
        cls.calculatrice = Calculatrice()
     
#     def setUp(self):
#         print("Avant un test")
#          
#     def tearDown(self):
#         print("Après un test")    
#          
#     @classmethod
#     def tearDownClass(cls):
#         print("FIN")    
        
    def testAddition(self):
        resultat = self.calculatrice.addition(9, 6)
        self.assertEqual(resultat, 15, "La valeur attendue est 15")
        
    def testSoustraction(self):
        resultat = self.calculatrice.soustraction(15, 8)
        self.assertEqual(resultat, 7, "La valeur attendue est 7")
        
    def testMultiplication(self):
        resultat = self.calculatrice.multiplication(11, 8)
        self.assertEqual(resultat, 88, "La valeur attendue est 88")
        
    def testDivision(self):
        resultat = self.calculatrice.division(88, 8)
        self.assertEqual(resultat, 11, "La valeur attendue est 11")
        
    def testDivisionParZero(self):
        with self.assertRaises(ZeroDivisionError):
            resultat = self.calculatrice.division(88, 0)
 
class TestVoiture(unittest.TestCase):
    
    voiture = None
    
    def setUp(self):
        # On créé un objet Voiture avant chaque test ...
        self.voiture = Voiture(25000)
    
    def testKilometrage(self):
        kilometrage = self.voiture.kilometrage
        self.assertEqual(kilometrage, 25000, "La valeur attendue est 25000")
    
    def testRouler(self):
        self.voiture.rouler(1000)
        self.assertEqual(self.voiture.kilometrage, 26000, "La valeur attendue est 26000")
    
    def testRoulerErreur(self):
        #         with self.assertRaises(ValueError):
        #             self.voiture.rouler(-10)
        with self.assertRaisesRegex(ValueError, "Nombre de kilomètres incohérent."):
            self.voiture.rouler(-10)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        
# if __name__ == '__main__':
#     unittest.main()