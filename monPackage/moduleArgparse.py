'''
Created on 8 oct. 2014

Liste des arguments obligatoires ou optionnels sur la ligne de commande du programme afin de pouvoir generer une playlist selon 3 formats
@author: Baptiste 'MagiKarpe' Deslaurier, Clément 'cLESE' Sebillet
'''
import argparse

def fonctionArgparse():
    '''
    Permet de créer tout les arguments que va devoir saisir ou pas obligatoirement l'utilisateur
    @args sont les arguments obligatoires ou non à l'appel de l'application
    '''
    parser = argparse.ArgumentParser()

    '''argument positionnel'''
    #temps est la duree de la playlist en minutes
    parser.add_argument("temps", help="duree de la playlist en minute", type=int)
    #nomfichier est le nom de la playlist
    parser.add_argument("nomfichier", help="nom donner a la playlist")
    #formatfichier est le format de sortie de la playlist
    parser.add_argument("formatfichier", help="extension de la playlist", choices=['m3u', 'xspf', 'pls'])

    '''argument optionnel'''
    #-G ou --genre permettera de specifie un genre de musique voulu
    parser.add_argument("-G", "--genre", help="genre et pourcentage du genre voulu dans la playlist", nargs=2, action="append")
    #-A ou --artiste permettre de specifie un artiste voulu
    parser.add_argument("-A", "--artiste", help="artiste et pourcentage de l'artiste voulu dans la playlist", nargs=2, action="append")
    #-a ou --album permettera de specifie un album voulu
    parser.add_argument("-a", "--album", help="album voulu dans la playlist", action="append")
    #-t ou --titre permettera de specifie un titre voulu
    parser.add_argument("-t", "--titre", help="titre voulu dans la playlist", action="append")

    args = parser.parse_args()

    return args