'''
Created on 12 nov. 2014

@author: Baptiste 'MagiKarpe' Deslaurier, Clément 'cLESE' Sebillet
'''
import logging

def VerifTps(temps):
    '''
    Vérifie le temps de la playlist que a saisi l'utilisateur à l'appel de l'application 
    @param temps : le temps de la playlist que a saisi l'utilisateur à l'appel de l'application 
    '''
    #On va essayer de mettre le pourcentage en entier positif
    try:
        #Convertion du temps en entier
        tps = int(temps)
        #Si le temps est nÃ©gatif ou Ã©gal Ã  0, on va mettre une message d'erreur dans le log et quitter le programme
        if (tps<=0):
            logging.error("le temps " + str(tps) + " n'est pas un entier positif et diffÃ©rent de 0")
            logging.info("***** Fin du programme *****")
            exit(1)
    #Si on y arrive pas on va lever une erreur de valeur, mettre un message dans le fichier log et quitter le programme
    except ValueError:
        logging.error('Impossible de convertir ' + str(tps) + ' en nombre entier !')
        logging.info("***** Fin du programme *****")
        exit(1)