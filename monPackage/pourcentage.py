'''
Created on 8 oct. 2014

@author: etudiant
'''
import logging

#Fonction de vérification des poucentages
def verifPourcentage(arg):
    #On va essayer de mettre le pourcentage en entier positif
    try:
        pct = abs(int(arg))
        #Si le pourcentage est supérieur à 100 on va le passer à 10 et le retourner
        if pct>100:
            pct = 10
            logging.warning('La quantité saisie est supérieur à 100')
            logging.info('Nombre supérieur à 100 transformé en : ' + str(pct))
        return pct
    #Si on y arrive pas on va lever une erreur de valeur, mettre un message dans le fichier log et quitter le programme
    except ValueError:
        logging.error('Impossible de convertir ' + arg + ' en nombre entier !')
        logging.info("***** Fin du programme *****")
        exit(1)


#Fonction de gestion des poucentages
def gestionPctage(typeArg):
    i = 0
    ligneList = 1
    j = 0
    ligneList2 = 1
    somme = 0

    #Tant que la liste du type d'argument passé à encore une ligne
    while ligneList <= len(typeArg):
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        #Vérification du pourcentage
        typeArg[i][1] = verifPourcentage(typeArg[i][1])
        #On ajoute le pourcentage retourné à l'ancienne somme
        somme = somme + typeArg[i][1]
        ligneList = ligneList + 1
        i = i + 1

    logging.info('Total des sommes des %: ' + str(somme))

    #SI la somme des pourcentages n'est pas égale à 100
    if somme > 100 or somme < 100:
        logging.info('Remise du total des % à 100 grace à la proportionalité')
        #Tant que la liste du type d'argument passé à encore une ligne
        while ligneList2 <= len(typeArg):
            #On va remettre sur base 100
            #Round() permet d'arrondir à l'entier le plus proche
            typeArg[j][1] = round(int(typeArg[j][1])*100/somme)
            j = j + 1
            ligneList2 = ligneList2 + 1