#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from monPackage.pourcentage import gestionPctage
from monPackage.moduleArgparse import fonctionArgparse
from monPackage.temps import TransPctToTps
from monPackage.fichier import creationFichierm3u, creationFichierpls, creationFichierxpsf
from monPackage.recupDonnees import Playlist, recupererDonnees

logging.basicConfig(filename="monLog.log", level=logging.DEBUG)

logging.info("***** Démarrage du programme *****")

args = fonctionArgparse()

'''Vérifications'''
'''Vérification d'un temps positif'''
logging.info("Utilisation de la fonction pour vérifier que le temps est un entier positif")
if args.temps<0 :
    print ("Le temps doit être positive !")
    logging.error("le temps " + str(args.temps) + " n'est pas un entier positif")
    exit(1)

logging.info("Saisies : " + str(args))

for unArg in ['genre','artiste','album', 'titre']:
    '''Si l'argument est renseigné'''
    if getattr(args, unArg) is not None:
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        gestionPctage(getattr(args, unArg))

recupererDonnees(args)
playlist = Playlist(args)

print(playlist)

if (args.formatfichier =='m3u'):
    creationFichierm3u(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')

if(args.formatfichier =='xspf'):
    creationFichierxpsf(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')

if(args.formatfichier =='pls'):
    creationFichierpls(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')

print("Good job team")

logging.info("Tout est bon !!!")
logging.info("***** Fin du programme *****")