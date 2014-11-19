'''
Created on 12 nov. 2014

@author: etudiant
'''
import logging

def VerifTps(temps):
    #On va essayer de mettre le pourcentage en entier positif
    try:
        #Convertion du temps en entier
        tps = int(temps)
        #Si le temps est négatif ou égal à 0, on va mettre une message d'erreur dans le log et quitter le programme
        if (tps<=0):
            logging.error("le temps " + str(tps) + " n'est pas un entier positif et différent de 0")
            logging.info("***** Fin du programme *****")
            exit(1)
    #Si on y arrive pas on va lever une erreur de valeur, mettre un message dans le fichier log et quitter le programme
    except ValueError:
        logging.error('Impossible de convertir ' + str(tps) + ' en nombre entier !')
        logging.info("***** Fin du programme *****")
        exit(1)