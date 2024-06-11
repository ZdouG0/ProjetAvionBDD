# main.py

from createdatabase import Session
from ClssUsers import *
from ClssPerson import *

def main():
    # Tester l'initialisation de l'utilisateur
    email = input("Entrez votre email: ")
    password = input("Entrez votre mot de passe: ")
    user = CUsers(email=email, password=password)

    if not hasattr(user, 'UserId'):
        print("Échec de la connexion. Terminaison du programme.")
        return

    while True:
        print("\nMenu:")
        print("1. Chercher un trajet")
        print("2. Imprimer les billets")
        print("3. Réserver un billet")
        print("4. Voir les billets réservés")
        print("5. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '1':
            depart = input("Entrez la ville de départ: ")
            arrivee = input("Entrez la ville d'arrivée (optionnel): ")
            prestataire = input("Entrez le nom du prestataire (optionnel): ")
            categorie = input("Entrez la catégorie (optionnel): ")
            prix = input("Entrez le prix maximum (optionnel): ")
            prix = float(prix) if prix else None
            user.search_trajet(depart, arrivee, prestataire, categorie, prix)
        
        elif choice == '2':
            ville_depart = input("Entrez la ville de départ: ")
            ville_arrivee = input("Entrez la ville d'arrivée: (optionnel)")
            date = input("date : (optionnel)")
            user.print_ticket(ville_depart,ville_arrivee,date)
            
        
        elif choice == '3':
            vol_id = input("Entrez l'ID du vol: ")
        elif choice == '4':
            user.get_reserved_tickets()
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
