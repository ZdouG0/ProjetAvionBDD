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


    def get_IdVol(self, ville_depart_nom, ville_arrivee_nom):
    
        with Session() as session:
            # Récupérer les IDs des villes de départ et d'arrivée à partir de leurs noms
            ville_depart = session.query(Ville).filter_by(NomVille=ville_depart_nom).first()
            ville_arrivee = session.query(Ville).filter_by(NomVille=ville_arrivee_nom).first()
            print("on est la")
            if not ville_depart or not ville_arrivee:
                # Vérifier si les villes existent
                return []

            # Récupérer les IdsVol pour les trajets ayant la ville de départ et la ville d'arrivée spécifiées
            vol_ids = (
                session.query(Vol.IdVol)
                .join(Trajet, Trajet.IdTrajet == Vol.IdTrajet)
                .join(Ville, Ville.IdVille == Trajet.VilleDepart)
                .join(Ville, Ville.IdVille == Trajet.VilleArrive)  
                .filter(Ville.NomVille == ville_depart_nom)
                .filter(Ville.NomVille == ville_arrivee_nom)
                .all()
            )
            # Extraire les IdsVol de la liste de tuples
            vol_ids = [vol[0] for vol in vol_ids]
            return vol_ids



    def print_ticket(self, vol_id):
        with Session() as session:
            # Récupérer le vol correspondant à vol_id
            vol = session.query(Vol).filter_by(IdVol=vol_id).first()
            if vol:
                # Récupérer les billets associés à ce vol
                billets = session.query(Billet).filter_by(IdVol=vol_id).all()

                if billets:
                    print("Informations sur le vol:")
                    print(f"Date du vol: {vol.DateVol}")
                    print(f"Avion: {vol.avion.NomAvion}")
                    print(f"Trajet: {vol.trajet.ville_depart.NomVille} -> {vol.trajet.ville_arrive.NomVille}")
                    print("Liste des billets réservés pour ce vol:")
                    
                    for billet in billets:
                        print(f"ID du billet: {billet.IdBillet}")
                        print(f"Prix du billet: {billet.PrixBillet}")
                        print(f"Catégorie: {billet.categorie.NomCategorie}")
                        print(f"Client: {billet.client.NomClient}")
                        print("--------------------")
                else:
                    print("Aucun billet trouvé pour ce vol.")
            else:
                print("Vol non trouvé.")


    def book_ticket(self, vol_id, categorie_id):
        with Session() as session:
            # Vérifier si le vol existe
            vol = session.query(Vol).filter_by(IdVol=vol_id).first()
            if vol:
                # Créer un nouvel enregistrement de billet avec le prix existant de la catégorie
                billet = Billet(PrixBillet=vol.categorie.PrixCategorie, IdCategorie=categorie_id, IdClient=self.UserId, IdVol=vol_id)
                session.add(billet)
                session.commit()
                print("Réservation de votre billet réussie !")
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