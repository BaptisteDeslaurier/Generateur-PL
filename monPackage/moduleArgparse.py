'''
Created on 8 oct. 2014

@author: etudiant
'''
import argparse

def fonctionArgparse():
    parser = argparse.ArgumentParser()

    '''argument positionnel'''
    parser.add_argument("temps", help="durer de la playlist en minute", type=int)
    parser.add_argument("nomfichier", help="nom donner a la playlist")
    parser.add_argument("formatfichier", help="extension de la playlist", choices=['m3u', 'xspf', 'pls'])

    '''argument optionnel'''
    parser.add_argument("-G", "--genre", help="genre et pourcentage du genre voulu dans la playlist", nargs=2, action="append")
    #parser.add_argument("-g", "--sousgenre", help="sous genre et pourcentage du sous genre voulu dans la playlist", nargs=2, action="append")
    parser.add_argument("-A", "--artiste", help="artiste et pourcentage de l'artiste voulu dans la playlist", nargs=2, action="append")
    parser.add_argument("-a", "--album", help="album voulu dans la playlist", action="append")
    parser.add_argument("-t", "--titre", help="titre voulu dans la playlist", action="append")

    args = parser.parse_args()

    return args