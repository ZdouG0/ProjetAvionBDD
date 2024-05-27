from sqlalchemy import create_engine, Column,Integer,String
from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine("mysql+mysqlconnector://root:password@127.0.0.1/avionbdd", echo= None)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session= Session()





class Avion(Base):
    __tablename__ = 'Avion'
    IdAvion = Column(Integer, primary_key=True, autoincrement=True)

class Client(Base):
    __tablename__ = 'Client'
    IdClient = Column(Integer, primary_key=True, autoincrement=True)

class Prestataire(Base):
    __tablename__ = 'Prestataire'
    IdPrestataire = Column(Integer, primary_key=True, autoincrement=True)
    NomPresta = Column(String(50))

class Ville(Base):
    __tablename__ = 'Ville'
    IdVille = Column(Integer, primary_key=True, autoincrement=True)
    VilleNom = Column(String(50))

class Trajet(Base):
    __tablename__ = 'Trajet'
    IdTrajet = Column(Integer, primary_key=True, autoincrement=True)
    VilleDepart = Column(String(50))
    VilleArrive = Column(String(50))

class Vol(Base):
    __tablename__ = 'Vol'
    IdVol = Column(Integer, primary_key=True, autoincrement=True)
    DateVol = Column(DateTime, nullable=False)
    IdAvion = Column(Integer, ForeignKey('Avion.IdAvion'), nullable=False)
    IdTrajet = Column(Integer, ForeignKey('Trajet.IdTrajet'))
    IdPrestataire = Column(Integer, ForeignKey('Prestataire.IdPrestataire'), nullable=False)
    
    avion = relationship("Avion")
    trajet = relationship("Trajet")
    prestataire = relationship("Prestataire")

class Billet(Base):
    __tablename__ = 'Billet'
    IdBillet = Column(Integer, primary_key=True, autoincrement=True)
    PrixBillet = Column(Integer, nullable=False)
    Categorie = Column(Integer, nullable=False)
    IdClient = Column(Integer, ForeignKey('Client.IdClient'), nullable=False)
    IdVol = Column(Integer, ForeignKey('Vol.IdVol'), nullable=False)
    
    client = relationship("Client")
    vol = relationship("Vol")

class Relie(Base):
    __tablename__ = 'Relie'
    IdVille = Column(Integer, ForeignKey('Ville.IdVille'), primary_key=True)
    IdTrajet = Column(Integer, ForeignKey('Trajet.IdTrajet'), primary_key=True)
    
    ville = relationship("Ville")
    trajet = relationship("Trajet")

# Création des tables dans la base de données
Base.metadata.create_all(engine)


 


#ajout de données initial dans la base de donnée :

# Requête SQL brute pour insérer des données dans la table Avion
sql_avion = text("""
    INSERT INTO Avion (IdAvion) 
    VALUES 
    (1),
    (2),
    (3);
""")
session.execute(sql_avion)

# Requête SQL brute pour insérer des données dans la table Client
sql_client = text("""
    INSERT INTO Client (IdClient) 
    VALUES 
    (1),
    (2),
    (3);
""")
session.execute(sql_client)

# Requête SQL brute pour insérer des données dans la table Prestataire
sql_prestataire = text("""
    INSERT INTO Prestataire (IdPrestataire, NomPresta) 
    VALUES 
    (1, 'Airline Company 1'),
    (2, 'Airline Company 2'),
    (3, 'Airline Company 3');
""")
session.execute(sql_prestataire)

# Requête SQL brute pour insérer des données dans la table Ville
sql_ville = text("""
    INSERT INTO Ville (IdVille, VilleNom) 
    VALUES 
    (1, 'Paris'),
    (2, 'New York'),
    (3, 'Tokyo');
""")
session.execute(sql_ville)

# Requête SQL brute pour insérer des données dans la table Trajet
sql_trajet = text("""
    INSERT INTO Trajet (IdTrajet, VilleDepart, VilleArrive) 
    VALUES 
    (1, 'Paris', 'New York'),
    (2, 'New York', 'Tokyo'),
    (3, 'Tokyo', 'Paris');
""")
session.execute(sql_trajet)

# Requête SQL brute pour insérer des données dans la table Vol
sql_vol = text("""
    INSERT INTO Vol (IdVol, DateVol, IdAvion, IdTrajet, IdPrestataire) 
    VALUES 
    (1, '2023-06-15 08:00:00', 1, 1, 1),
    (2, '2023-07-20 10:00:00', 2, 2, 2),
    (3, '2023-08-25 12:00:00', 3, 3, 3);
""")
session.execute(sql_vol)

# Requête SQL brute pour insérer des données dans la table Billet
sql_billet = text("""
    INSERT INTO Billet (IdBillet, PrixBillet, Categorie, IdClient, IdVol) 
    VALUES 
    (1, 500, 1, 1, 1),
    (2, 700, 2, 2, 2),
    (3, 1000, 1, 3, 3);
""")
session.execute(sql_billet)

# Requête SQL brute pour insérer des données dans la table Relie
sql_relie = text("""
    INSERT INTO Relie (IdVille, IdTrajet) 
    VALUES 
    (1, 1),
    (2, 2),
    (3, 3);
""")
session.execute(sql_relie)

# Validez la transaction
session.commit()
