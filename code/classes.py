# -*- coding: utf-8 -*-

'''Créé le 27 juin 2018 par Etienne.

Ce module contient les classes principales de l'application.
Classe Calculatrice, classe Voiture.
'''

class Calculatrice:
    '''Classe Calculatrice.
    Elle implémente les opérations mathématiques de base.
    ''' 
    def addition(self, a, b):
        '''Additionne deux nombres et renvoi le résultat.
        
        :param a: Le premier nombre
        :param b: Le second nombre
        :return: Le résultat de l'addition de a et b.
        '''
        return a + b
   
    def soustraction(self, a, b):
        '''Soustrait deux nombres et renvoi le résultat.
        
        :param a: Le premier nombre
        :param b: Le second nombre
        :return: Le résultat de la soustraction de a par b.
        '''
        return a - b
    
    def multiplication(self, a, b):
        '''Multiplie deux nombres et renvoi le résultat.
        
        :param a: Le premier nombre
        :param b: Le second nombre
        :return: Le résultat de la multiplication de a et b.
        '''
        return a * b
    
    def division(self, a, b):
        '''Divise deux nombres et renvoi le résultat.
        
        :param a: Le premier nombre
        :param b: Le second nombre
        :return: Le résultat de la division de a par b.
        :raises ZeroDivisionError: Si b vaut 0.
        '''
        if b != 0:
            return a / b
        else:
            raise ZeroDivisionError("Division par 0 interdite")
        
class Voiture:
    '''Implémentation d'une voiture
    '''
    __kilometrage = 0
    '''Le kilométrage de la voiture.
    ''' 
    
    def __init__(self, kilometrage):
        '''Constructeur permettant d'initialiser le kilométrage.
        '''
        self.__kilometrage = kilometrage

    def rouler(self, nbKilometres):
        '''Méthode permettant de faire rouler la voiture
        d'un certain nombre de kilomètres.
        
        :param nbKilometres: Le nombre de kilomètres que la voiture doit parcourir.
        :raises ValueError: Si le nombre de kilomètre est négatif ou supérieur à 500000.
        '''
        if 0 < nbKilometres < 500000:
            self.__kilometrage += nbKilometres
        else:
            raise ValueError("Nombre de kilomètres incohérent.")    
 
    def get_kilometrage(self):
        '''Accesseur en lecture retournant le kilometrage de la voiture.
        
        :return: Le kilometrage.
        '''
        return self.__kilometrage
    
    kilometrage = property(get_kilometrage, None, None, None)
    '''Propriété publique sur le kilométrage.
    '''