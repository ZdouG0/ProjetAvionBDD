from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, text, inspect
from sqlalchemy.orm import relationship, sessionmaker, declarative_base, validates
from sqlalchemy.exc import IntegrityError

# Créer une connexion à la base de données
engine = create_engine("mysql+mysqlconnector://root:milan@127.0.0.1/avionbdd", echo=None)

Base = declarative_base()

# Définir une session
Session = sessionmaker(bind=engine)
session = Session()

# Définir les classes correspondant aux tables
class Avion(Base):
    __tablename__ = 'Avion'
    IdAvion = Column(Integer, primary_key=True, autoincrement=True)
    NomAvion = Column(String(50))

class Client(Base):
    __tablename__ = 'Client'
    IdClient = Column(Integer, primary_key=True, autoincrement=True)
    NomClient = Column(String(50))
    AgeClient = Column(Integer)
    Nationalite = Column(String(50))
    EmailClient = Column(String(50))
    PasswordClient = Column(String(50))
    TelephoneClient = Column(String(50))
    Adresse = Column(String(50))

class Prestataire(Base):
    __tablename__ = 'Prestataire'
    IdPrestataire = Column(Integer, primary_key=True, autoincrement=True)
    NomPresta = Column(String(50))
    TelephonePresta = Column(String(50))
    EmailPresta = Column(String(50))

class Ville(Base):
    __tablename__ = 'Ville'
    IdVille = Column(Integer, primary_key=True, autoincrement=True)
    NomVille = Column(String(50))
    PaysVille = Column(String(50))

class Trajet(Base):
    __tablename__ = 'Trajet'
    IdTrajet = Column(Integer, primary_key=True, autoincrement=True)
    VilleDepart = Column(Integer, ForeignKey('Ville.IdVille'))
    VilleArrive = Column(Integer, ForeignKey('Ville.IdVille'))

    ville_depart = relationship("Ville", foreign_keys=[VilleDepart])
    ville_arrive = relationship("Ville", foreign_keys=[VilleArrive])

    @validates('VilleDepart', 'VilleArrive')
    def validate_villes(self, key, value):
        if key == 'VilleArrive' and self.VilleDepart == value:
            raise ValueError("La ville de départ et la ville d'arrivée doivent être différentes.")
        return value

class Categorie(Base):
    __tablename__ = 'Categorie'
    IdCategorie = Column(Integer, primary_key=True, autoincrement=True)
    NomCategorie = Column(String(50))

class Vol(Base):
    __tablename__ = 'Vol'
    IdVol = Column(Integer, primary_key=True, autoincrement=True)
    DateVol = Column(DateTime, nullable=False)
    IdAvion = Column(Integer, ForeignKey('Avion.IdAvion'), nullable=False)
    IdTrajet = Column(Integer, ForeignKey('Trajet.IdTrajet'), nullable=False)
    IdPrestataire = Column(Integer, ForeignKey('Prestataire.IdPrestataire'), nullable=False)
    
    avion = relationship("Avion")
    trajet = relationship("Trajet")
    prestataire = relationship("Prestataire")

class Billet(Base):
    __tablename__ = 'Billet'
    IdBillet = Column(Integer, primary_key=True, autoincrement=True)
    PrixBillet = Column(Integer, nullable=False)
    IdCategorie = Column(Integer, ForeignKey('Categorie.IdCategorie'), nullable=False)
    IdClient = Column(Integer, ForeignKey('Client.IdClient'), nullable=False)
    IdVol = Column(Integer, ForeignKey('Vol.IdVol'), nullable=False)
    
    categorie = relationship("Categorie")
    client = relationship("Client")
    vol = relationship("Vol")

class Relie(Base):
    __tablename__ = 'Relie'
    IdVille = Column(Integer, ForeignKey('Ville.IdVille'), primary_key=True)
    IdTrajet = Column(Integer, ForeignKey('Trajet.IdTrajet'), primary_key=True)
    
    ville = relationship("Ville")
    trajet = relationship("Trajet")

# Fonction pour vérifier si une table existe
def table_exists(engine, table_name):
    inspector = inspect(engine)
    return inspector.has_table(table_name)

# Créer les tables si elles n'existent pas
if not table_exists(engine, 'Avion'):
    Base.metadata.create_all(engine, tables=[Avion.__table__])
if not table_exists(engine, 'Client'):
    Base.metadata.create_all(engine, tables=[Client.__table__])
if not table_exists(engine, 'Prestataire'):
    Base.metadata.create_all(engine, tables=[Prestataire.__table__])
if not table_exists(engine, 'Ville'):
    Base.metadata.create_all(engine, tables=[Ville.__table__])
if not table_exists(engine, 'Trajet'):
    Base.metadata.create_all(engine, tables=[Trajet.__table__])
if not table_exists(engine, 'Categorie'):
    Base.metadata.create_all(engine, tables=[Categorie.__table__])
if not table_exists(engine, 'Vol'):
    Base.metadata.create_all(engine, tables=[Vol.__table__])
if not table_exists(engine, 'Billet'):
    Base.metadata.create_all(engine, tables=[Billet.__table__])
if not table_exists(engine, 'Relie'):
    Base.metadata.create_all(engine, tables=[Relie.__table__])

# Fonction pour ajouter des données initiales dans une table
def add_initial_data(table, data_list):
    for data in data_list:
        if not session.query(table).filter_by(**data).first():
            new_entry = table(**data)
            session.add(new_entry)
    session.commit()

# Ajouter des données initiales dans la table Avion
avion_data = [
    {'NomAvion': 'Boeing 747'},
    {'NomAvion': 'Airbus A320'},
    {'NomAvion': 'Concorde'}
]
add_initial_data(Avion, avion_data)

# Ajouter des données initiales dans la table Client
client_data = [
    {'NomClient': 'Milan', 'AgeClient': 30, 'Nationalite': 'USA', 'EmailClient': 'milan', 'PasswordClient': 'p', 'TelephoneClient': '1234567890', 'Adresse': '1'},
    {'NomClient': 'Jane Smith', 'AgeClient': 25, 'Nationalite': 'UK', 'EmailClient': 'jane.smith@example.com', 'PasswordClient': 'password2', 'TelephoneClient': '0987654321', 'Adresse': '456 Elm St'},
    {'NomClient': 'Alice Johnson', 'AgeClient': 35, 'Nationalite': 'Canada', 'EmailClient': 'alice.johnson@example.com', 'PasswordClient': 'password3', 'TelephoneClient': '1122334455', 'Adresse': '789 Maple St'}
]
add_initial_data(Client, client_data)

# Ajouter des données initiales dans la table Prestataire
prestataire_data = [
    {'NomPresta': 'Airline Company 1', 'TelephonePresta': '1234567890', 'EmailPresta': 'contact@airline1.com'},
    {'NomPresta': 'Airline Company 2', 'TelephonePresta': '0987654321', 'EmailPresta': 'contact@airline2.com'},
    {'NomPresta': 'Airline Company 3', 'TelephonePresta': '1122334455', 'EmailPresta': 'contact@airline3.com'}
]
add_initial_data(Prestataire, prestataire_data)

# Ajouter des données initiales dans la table Ville
ville_data = [
    {'NomVille': 'Paris', 'PaysVille': 'France'},
    {'NomVille': 'New York', 'PaysVille': 'USA'},
    {'NomVille': 'Tokyo', 'PaysVille': 'Japan'},
    {'NomVille': 'Londres', 'PaysVille': 'UK'},
    {'NomVille': 'Berlin', 'PaysVille': 'Germany'},
    {'NomVille': 'Sydney', 'PaysVille': 'Australia'},
    {'NomVille': 'Rome', 'PaysVille': 'Italy'}
]
add_initial_data(Ville, ville_data)

# Ajouter des données initiales dans la table Trajet
trajet_data = [
    {'VilleDepart': 1, 'VilleArrive': 2},
    {'VilleDepart': 2, 'VilleArrive': 3},
    {'VilleDepart': 3, 'VilleArrive': 1},
    {'VilleDepart': 1, 'VilleArrive': 28},
    {'VilleDepart': 1, 'VilleArrive': 29},
    {'VilleDepart': 1, 'VilleArrive': 30},
    {'VilleDepart': 1, 'VilleArrive': 31}
]
add_initial_data(Trajet, trajet_data)

# Ajouter des données initiales dans la table Categorie
categorie_data = [
    {'NomCategorie': 'Economy'},
    {'NomCategorie': 'Business'},
    {'NomCategorie': 'First Class'}
]
add_initial_data(Categorie, categorie_data)

# Ajouter des données initiales dans la table Vol
vol_data = [
    {'DateVol': '2023-06-15 08:00:00', 'IdAvion': 1, 'IdTrajet': 1, 'IdPrestataire': 1},
    {'DateVol': '2023-07-20 10:00:00', 'IdAvion': 2, 'IdTrajet': 2, 'IdPrestataire': 2},
    {'DateVol': '2023-08-25 12:00:00', 'IdAvion': 3, 'IdTrajet': 3, 'IdPrestataire': 3},
    {'DateVol': '2023-09-05 14:00:00', 'IdAvion': 1, 'IdTrajet': 30, 'IdPrestataire': 1},
    {'DateVol': '2023-09-10 16:00:00', 'IdAvion': 2, 'IdTrajet': 31, 'IdPrestataire': 2},
    {'DateVol': '2023-09-15 18:00:00', 'IdAvion': 3, 'IdTrajet': 32, 'IdPrestataire': 3},
    {'DateVol': '2023-09-20 20:00:00', 'IdAvion': 1, 'IdTrajet': 33, 'IdPrestataire': 1}
]
add_initial_data(Vol, vol_data)

# Ajouter des données initiales dans la table Billet
billet_data = [
    {'PrixBillet': 500, 'IdCategorie': 1, 'IdClient': 1, 'IdVol': 1},
    {'PrixBillet': 700, 'IdCategorie': 2, 'IdClient': 2, 'IdVol': 2},
    {'PrixBillet': 1000, 'IdCategorie': 3, 'IdClient': 3, 'IdVol': 3}
]
add_initial_data(Billet, billet_data)

# Ajouter des données initiales dans la table Relie
relie_data = [
    {'IdVille': 1, 'IdTrajet': 2}
]
add_initial_data(Relie, relie_data)

