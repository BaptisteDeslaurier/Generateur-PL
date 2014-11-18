'''
Created on 12 nov. 2014

@author: etudiant
'''
import logging

def TransPctToTps(typeArg, temps):
    i = 0
    ligneList = 1

    '''Tant que la liste du type d'argument passé à encore une ligne'''
    while ligneList <= len(typeArg):
        logging.info("Utilisation de la fonction pour tranformer les pourcentage en seconde")
        typeArg[i][1] = 3600 * (typeArg[i][1])/50
        ligneList = ligneList + 1
        i = i + 1