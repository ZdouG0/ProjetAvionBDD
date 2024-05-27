from createdatabase import *

class CUsers() :
    
    

    def __init__(self,email='', password='', number=0,nom='') :
        #creation de l'objet dans la BAse de donnees
        string = "SELECT * from Users WHERE Users.UserEmail ='"+email+"'"
        sql = text(string)
        result = session.execute(sql)
        for user in result :
            self.UserId = user.IdUser
        self.UserName = nom
        self.UserEmail = email
        self.UserPassword = password
        self.UserNumber = number

    def makeoffer(self,IdAnnonce):
        string = "SELECT * from Advertisement WHERE Advertisement.IdAd ="+str(IdAnnonce)
        sql = text(string)
        result = session.execute(sql)
        idVendeur=0
        for ad in result :
            idVendeur = ad.IdUser
        prix = float(input("Entrer le montant de votre offre :"))
        quest ="INSERT INTO Offers(OfferAcceptation,OfferPrice,IdUserAcheteur,IdUserVendeur,IdAd) VALUES (False,"+str(prix)+","+str(self.UserId)+","+str(idVendeur)+","+str(IdAnnonce)+")"
        sql = text(quest)
        result = session.execute(sql)
        session.commit()
        print("Creation de votre Offre reussie !")



    def ResponseOffer(self):
        ReponseOK=False
        while ReponseOK == False :
            Reponse =int(input("Entrer l'identifiant de l'offre dont vous voulez changer l'etat"))
            string = "SELECT * from Offers WHERE Offers.IdUserVendeur ="+str(self.UserId)+" AND Offers.IdOffer ="+str(Reponse)
            sql = text(string)
            result = session.execute(sql)
            if result.rowcount == 0 :
                print("Entrée incorrect veuillez reesayer!")
            else :
                ReponseOK = True
        for offer in result :
            if offer.OfferAcceptation == 0 :
                string = "UPDATE Offers SET Offers.OfferAcceptation = True WHERE Offers.IdOffer ="+str(Reponse)
            else :
                string = "UPDATE Offers SET Offers.OfferAcceptation = False WHERE Offers.IdOffer ="+str(Reponse)
            sql = text(string)
            result = session.execute(sql)
            session.commit()
        self.ViewOffer()
            
        
    
    def ViewOffer(self):


    def create_announce(self):


