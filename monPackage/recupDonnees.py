'''
Created on 18 nov. 2014

@author: etudiant
'''
import sqlalchemy
import random
from monPackage.accesDB import table_morceaux, engine as connect

#Définition d'une variable regroupant l'ensemble d'arguments pouvant être saisi par l'utilisateur
argument_cli = ['genre','artiste','album','titre']

#Définition de la playlist
playlist =[]

#Fonction permettant de créer la requete et récupérer des données dans la BDD par rapport aux besoins de l'utilisateur
def recupererDonnees(args):
    for attribut in argument_cli:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                #RecuperationDonnees va construire la requete
                #Si l'utilisateur a saisi un ou plusieurs genres
                if (attribut == 'genre'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.genre == argument[0])
                #Si l'utilisateur a saisi un ou plusieurs artistes
                if (attribut == 'artiste'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.artiste == argument[0])
                #Si l'utilisateur a saisi un ou plusieurs albums
                if (attribut == 'album'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.album == argument[0])
                #Si l'utilisateur a saisi un ou plusieurs titres
                if (attribut== 'titre'):
                    RecuperationDonnees = sqlalchemy.select([table_morceaux]).where(table_morceaux.c.titre == argument[0])

                # connection à la BDD puis execution de la requète
                recuperation = connect.execute(RecuperationDonnees)
                #Insertion des données récuperées dans un list
                recuperation = list(recuperation)
                #Melange la musique dans la list
                random.shuffle(recuperation)

                #Rajoute une liste au 3eme rang de la liste argument
                argument.insert(2,[])
                #Initialisation de la valeur i à 0 pour la prochaine boucle for
                i=0
                #Initialisation de la valeur durée à 0 pour connaitre la duée de la playlist en cours de création
                duree = 0

                #Boucle qui va permettre de combler la playlist s'l reste assez de temps pour une ou plusieurs musiques
                for champBDD in recuperation:
                    #Ajoute la durée de la musique à la durée de la playlist en cours de créationn
                    duree += champBDD[5]
                    #Si durée de la playlist en cours de création est inférieur à la durée demandé par utilisateur
                    if(duree < argument[1]*60):
                        #Insertion de la musique dans la playlist
                        argument[2].insert(i, champBDD)
                        i += 1
                    #Sinon suppression de la durée de la musique anciennement ins
                    else:
                        duree -= champBDD[5]


#Génération de la liste pour la playlist
def generationPlaylist(args):
    i = 0
    for attribut in argument_cli:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                # Pour chaque musique dans la playlist on insére le titre, l'artiste, l'album, le format et le chemin
                for musique in argument[2]:
                    playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
                    i += 1
    #Mélange les musiques aléatoirement
    random.shuffle(playlist)

def Playlist(args):
    #Définition de la duree en cours de la playlist généré et initialisation à 0
    duree = 0
    #Pour chaque ligne de playlist on va ajouter le temps de la musique à la duree
    for musique in playlist:
        duree += musique[3]

''''Si la duree de la musique est inférieur à la durée demandée par l'utilisateur on effectue la requête
permettant d'aller chercher des musiques alétoirement dans la base correspondant au genre'''
    if(duree < args.temps*60):
        select_morceaux = sqlalchemy.select([table_morceaux])
        resultat = connect.execute(select_morceaux)
        resultat = list(resultat)
        random.shuffle(resultat)

    i=len(playlist)
    for musique in resultat:
        duree += musique[5] #
        if(duree < args.temps*60):
            playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
            i += 1
        else:
            duree -= musique[5]

    return playlist