#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Created on 8 oct. 2014

Connexion à la base Postgresql
@author: Baptiste 'MagiKarpe' Deslaurier, Clément 'cLESE' Sebillet
'''

import sqlalchemy

#Création de la variable engine initialisé avec la connexion à la BDD
engine = sqlalchemy.create_engine('postgresql://b.deslaurier:passe@172.16.99.2:5432/bdeslaurier/radio')

# la collection de métadonnées est stockée dans l'objet MetaData
metadonnees = sqlalchemy.MetaData()

# récupère dans table_morceaux la structure de la table morceaux de la base de données
table_morceaux = sqlalchemy.Table('morceaux',metadonnees,
                                  sqlalchemy.Column('titre',sqlalchemy.String),
                                  sqlalchemy.Column('album',sqlalchemy.String),
                                  sqlalchemy.Column('artiste',sqlalchemy.Integer),
                                  sqlalchemy.Column('genre',sqlalchemy.Integer),
                                  sqlalchemy.Column('sousgenre',sqlalchemy.String),
                                  sqlalchemy.Column('duree', sqlalchemy.Integer),
                                  sqlalchemy.Column('format',sqlalchemy.String),
                                  sqlalchemy.Column('polyphonie',sqlalchemy.Integer),
                                  sqlalchemy.Column('chemin',sqlalchemy.String)
                                  )

# récupère dans table_artiste la structure de la table artiste de la base de données
table_artiste = sqlalchemy.Table('artiste',metadonnees,
                                  sqlalchemy.Column('id',sqlalchemy.integer),
                                  sqlalchemy.Column('libelle_first',sqlalchemy.String),
                                  sqlalchemy.Column('libelle_second',sqlalchemy.String)
                                  )

# récupère dans table_artiste la structure de la table genre de la base de données
table_genre = sqlalchemy.Table('genre',metadonnees,
                                  sqlalchemy.Column('id',sqlalchemy.integer),
                                  sqlalchemy.Column('libelle_first',sqlalchemy.String),
                                  sqlalchemy.Column('libelle_second',sqlalchemy.String)
                                  )

# s définit la requête à effectuer
s = sqlalchemy.select([table_morceaux, table_artiste, table_genre])

# défini conn qui établi la connection à la base de données
conn = engine.connect()

# result est la variable qui reçoit la liste des musiques
result = conn.execute(s)
