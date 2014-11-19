#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
from monPackage.pourcentage import gestionPctage
from monPackage.moduleArgparse import fonctionArgparse
from monPackage.temps import VerifTps
from monPackage.fichier import creationFichierm3u, creationFichierpls, creationFichierxpsf
from monPackage.recupDonnees import Playlist, recupererDonnees

#création d'un fichier de log
logging.basicConfig(filename="monLog.log", level=logging.DEBUG)

logging.info("***** Démarrage du programme *****")

#création d'un fichier de log
args = fonctionArgparse()

logging.info("Saisies : " + str(args))

#Vérification du temps voulu pour la playlist
logging.info("Utilisation de la fonction pour vérifier que le temps de la playlist")
VerifTps(args.temps)

for unArg in ['genre','artiste','album', 'titre']:
    '''Si l'argument est renseigné'''
    if getattr(args, unArg) is not None:
        logging.info("Utilisation de la fonction pour vérifier que le pourcentage est entre 0 et 100")
        gestionPctage(getattr(args, unArg))

#recuperation des données
recupererDonnees(args)
playlist = Playlist(args)

#génération de la playlist selon le format choisi
if (args.formatfichier =='m3u'):
    creationFichierm3u(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')

if(args.formatfichier =='xspf'):
    creationFichierxpsf(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')

if(args.formatfichier =='pls'):
    creationFichierpls(args.nomfichier, args.formatfichier, playlist)
    print('La playlist a bien ete genere')

logging.info("Tout est bon !!!")
logging.info("***** Fin du programme *****")