'''
Created on 18 nov. 2014

@author: etudiant
'''
import sqlalchemy
import random
from monPackage.accesDB import table_morceaux, engine as connect

#Définition d'une variable regroupant un ensemble d'arguments
argument_cli = ['genre','artiste','album','titre']

#Définition de la playlist
playlist =[]

#Fonction permettant de récupérer des données dans la BDD par rapport aux besoins de l'utilisateur
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

                # connectection à la BDD puis execution de la requète
                recuperation = connect.execute(RecuperationDonnees)
                #Insertion des données récuperées dans un list
                recuperation = list(recuperation)
                #Melange la musique dans la list
                random.shuffle(recuperation)

                #Rajoute une liste au 3eme rang de la liste argument
                argument.insert(2,[])
                i=0   #Initialisation de la valeur à 0
                duree = 0 #Initialisation de la valeur à 0

                for champBDD in recuperation: #Pour chaque musique recuperer dans la liste, on vérifie la durée afin de correspondre au mieux au demande de l'utilisateur
                    duree += champBDD[5]  #Correspond au champ durée dans la BDD
                    if(duree < argument[1]*60): #Si durée inf. à durée demandé par utilisateur + conversion en minutes
                        argument[2].insert(i, champBDD)
                        i += 1
                    else:
                        duree -= champBDD[5] #Correspond au champ durée dans la BDD


#Génération de la liste de playlist
def generationPlaylist(args):
    i = 0
    for attribut in argument_cli:
        if getattr(args, attribut) is not None:
            for argument in getattr(args, attribut):
                for musique in argument[2]: # Pour chaque musique dans la playlist on insére le titre, l'artiste, l'album, le format et le chemin
                    playlist.insert(i, [musique[0], musique[2], musique[1], musique[5], musique[8]])
                    i += 1
    random.shuffle(playlist) #On mélange les musiques aléatoirement

def Playlist(args):
    duree = 0 #initialisation à 0
    for musique in playlist: #Pour chaque musique dans la playlist selon un genre précis
        duree += musique[3]

    if(duree < args.temps*60): #Si la duree de la musique est inférieur à la durée totale demandée par l'utilisateur on effectue la requête permettant d'aller chercher des musiques alétoirement dans la base correspondant au genre
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