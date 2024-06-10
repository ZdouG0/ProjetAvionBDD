from createdatabase import *

class Prestataire():

    def __init__(self, nom=''):
        #creation de l'objet dans la BAse de donnees
        string = "SELECT * from Prestataire WHERE Prestataire.NomPresta ='"+nom+"'"
        sql = text(string)
        result = session.execute(sql)
        self.NomPresta = nom
    
    def publieTrajet(villeDepart,villeArrive):

        string = "INSERT INTO Trajet (VilleDepart, VilleArrive) VALUES '"+villeDepart+ ","+villeArrive+"; "
        sql = text(string)
        result = session.execute(sql)
    


