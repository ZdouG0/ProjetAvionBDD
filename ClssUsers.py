from createdatabase import Session, Client, Vol, Trajet, Billet,Ville, Prestataire, Categorie

class CUsers:

    def __init__(self, email='', password='', number=0, nom=''):
        session = Session()
        user = session.query(Client).filter_by(EmailClient=email, PasswordClient=password).first()
        if user:
            self.UserId = user.IdClient
            self.UserName = user.NomClient
            self.UserEmail = user.EmailClient
            self.UserPassword = user.PasswordClient
            self.UserNumber = user.TelephoneClient
        else:
            print("Email ou mot de passe incorrect.")
            # Gérer le cas où l'utilisateur n'est pas trouvé

    def search_trajet(self, depart, arrivee=None, prestataire=None, categorie=None, prix=None):
        with Session() as session:
            query = (
                session.query(Vol)
                .join(Trajet)
                .join(Ville, Trajet.VilleDepart == Ville.IdVille)
                .filter(Ville.NomVille == depart)
            )

            if arrivee:
                query = query.join(Ville, Trajet.VilleArrive == Ville.IdVille).filter(Ville.NomVille == arrivee)
            
            if prestataire:
                query = query.join(Prestataire, Vol.IdPrestataire == Prestataire.IdPrestataire).filter(Prestataire.NomPresta == prestataire)
            
            if categorie:
                query = query.join(Billet, Vol.IdVol == Billet.IdVol).join(Categorie, Billet.IdCategorie == Categorie.IdCategorie).filter(Categorie.NomCategorie == categorie)
            
            if prix:
                query = query.join(Billet, Vol.IdVol == Billet.IdVol).filter(Billet.PrixBillet <= prix)
            
            vols = query.all()
            print(vols)
            for vol in vols:
                trajet = session.query(Trajet).filter_by(IdTrajet=vol.IdTrajet).first()
                ville_depart = session.query(Ville).filter_by(IdVille=trajet.VilleDepart).first()
                ville_arrive = session.query(Ville).filter_by(IdVille=trajet.VilleArrive).first()
                print(f"Date: {vol.DateVol},  Trajet: {ville_depart.NomVille} -> {ville_arrive.NomVille}")
            session.close()

    



    def print_tickets(self, ville_depart, ville_arrivee=None, date_vol=None):
        with Session() as session:
            query = (
                session.query(Vol)
                .join(Trajet)
                .join(Ville, Trajet.VilleDepart == Ville.IdVille)
                .filter(Ville.NomVille == ville_depart)
            )

            if ville_arrivee:
                query = query.join(Ville, Trajet.VilleArrive == Ville.IdVille).filter(Ville.NomVille == ville_arrivee)
            
            if date_vol:
                query = query.filter(Vol.DateVol == date_vol)
            
            vols = query.all()

            if vols:
                print("Informations sur les vols correspondants:")
                for vol in vols:
                    trajet = session.query(Trajet).filter_by(IdTrajet=vol.IdTrajet).first()
                    ville_depart = session.query(Ville).filter_by(IdVille=trajet.VilleDepart).first()
                    ville_arrive = session.query(Ville).filter_by(IdVille=trajet.VilleArrive).first()
                    print(f"Date: {vol.DateVol}, Trajet: {ville_depart.NomVille} -> {ville_arrive.NomVille}")
            else:
                print("Aucun vol trouvé avec les informations spécifiées.")


    def book_ticket(self, vol_id, categorie_id=None):
        with Session() as session:
            # Vérifier si le vol existe
            vol = session.query(Vol).filter_by(IdVol=vol_id).first()
            if vol:
                # Créer un nouvel enregistrement de billet avec le prix existant de la catégorie
                if categorie_id:
                    billet = Billet(PrixBillet=vol.categorie.PrixCategorie, IdCategorie=categorie_id, IdClient=self.UserId, IdVol=vol_id)
                    session.add(billet)
                    session.commit()
                    print("Réservation de votre billet réussie !")
                else:
                    billet = Billet(PrixBillet=vol.categorie.PrixCategorie, IdClient=self.UserId, IdVol=vol_id)
                    session.add(billet)
                    session.commit()

            else:
                print("Le vol spécifié n'existe pas.")

    
    def get_reserved_tickets(self):
        with Session() as session:
            # Récupérer tous les billets réservés par l'utilisateur actuel
            billets = session.query(Billet).filter_by(IdClient=self.UserId).all()
            if billets:
                print("Billets réservés par vous :")
                for billet in billets:
                    print(f"Billet ID: {billet.IdBillet}, Prix: {billet.PrixBillet}, Catégorie: {billet.IdCategorie}, Vol: {billet.IdVol}")
            else:
                print("Vous n'avez réservé aucun billet.")