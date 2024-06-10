from ClssUsers import *

def main():
    print("Veuillez vous connecter en donnant votre mail")
    email = input("Email: ")
    print("Password:")
    password = input()

    # Création de l'objet utilisateur
    user = CUsers(email, password)

    if not user.UserId:
        print("Échec de la connexion. Veuillez réessayer.")
        return

    while True:
        print("\nChoisissez une option:")
        print("1. Rechercher des trajets")
        print("2. Quitter")
        choix = input("Votre choix: ")

        if choix == '1':
            print("Connaissez-vous la ville de retour ?")
            print("1. Oui")
            print("2. Non")
            choix_ville = input(">> ")
            if choix_ville == '1':
                depart = input("Ville de départ: ")
                arrivee = input("Ville d'arrivée: ")
                user.search_trajet(depart, arrivee)
            else:
                depart = input("Ville de départ: ")
                user.search_trajet(depart)

            print("Voulez vous voir les billets proposés pour ces vol ?")
            print("1. Oui")
            print("2. Non")

            choixd = input(">> ")
            if choixd == '1' or choix_ville == 2:
                print("Veuillez indiquer votre ville de retour: ")
                arrivee = input("Ville d'arrive du vol: ")

            
            user.search_trajet(depart,arrivee)
            ids =  user.get_IdVol(depart,arrivee)
            for id in ids :
                user.print_ticket(id)

        else:
            print("Au revoir!")
            break

if __name__ == "__main__":
    main()
