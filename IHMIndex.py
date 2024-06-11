from tkinter import *
from tkinter import ttk
from tkinter import messagebox


from tkcalendar import Calendar, DateEntry
from IHMConnexion import Connexion
from IHMResultRecherche import ResultRecherche
from IHMmesReservation import mesReservation

def Index():
    
    #création de la fenetre
    rootwindow = Tk()
    #configuration de la fenetre 
    rootwindow.configure(bg="light goldenrod") #on definit la couleur du fond d'ecran de la fenetre
    rootwindow.geometry("500x650") #on definit la taille de la fenetre
    rootwindow.title("Accueil") #son titre

    def donnee_form():
        villeD = entry_villeD.get()
        villeA = entry_villeA.get()
        date = Calendrier.get_date()
        prix = entry_Prix.get()
        categorie = listeCombo.get()
        prestataire = entry_Prestataire.get()
        #if (pas de compte):
            #messagebox.showinfo("Erreur","Une erreur est survenue : Mots de passe ou email incorrect")
        ResultRecherche(villeA,villeD,date,prix,categorie,prestataire)

    def redirect_connexion():
        Connexion()


    def redirect_mesReserv():
        mesReservation()
    
    # Si connecter voir ses reservation
    Reserv_button = Button(rootwindow, text="Voir mes reservations", command=redirect_mesReserv)
    Reserv_button.grid(row=1, column=4, pady=20)

    Titre_label = Label(rootwindow, text='Accueil',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 40)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=0, column=3, padx=10, pady=10) #on le place

    Connexion_button = Button(rootwindow, text="Se connecter", command=redirect_connexion)
    Connexion_button.grid(row=0, column=4, pady=20)

    Titre_label = Label(rootwindow, text='Recherche',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 20)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=1, column=3, padx=10, pady=10) #on le place

    label_villeD = Label(rootwindow, text="Ville de Départ")
    label_villeD.grid(row=2, column=2, padx=10, pady=10)
    entry_villeD = Entry(rootwindow)
    entry_villeD.grid(row=2, column=3, padx=10, pady=10)

    label_villeA = Label(rootwindow, text="Ville d'arrivée")
    label_villeA.grid(row=3, column=2, padx=10, pady=10)
    entry_villeA = Entry(rootwindow)
    entry_villeA.grid(row=3, column=3, padx=10, pady=10)

    label_Prestataire = Label(rootwindow, text="Prestataire")
    label_Prestataire.grid(row=4, column=2, padx=10, pady=10)
    entry_Prestataire = Entry(rootwindow)
    entry_Prestataire.grid(row=4, column=3, padx=10, pady=10)

    label_Prix = Label(rootwindow, text="Prix")
    label_Prix.grid(row=5, column=2, padx=10, pady=10)
    entry_Prix = Entry(rootwindow)
    entry_Prix.grid(row=5, column=3, padx=10, pady=10)




    label_Categorie = Label(rootwindow, text="Categorie")
    label_Categorie.grid(row=6, column=2, padx=10, pady=10)

    # 2) - créer la liste Python contenant les éléments de la liste Combobox
    listeProduits=["Business", "economique","premium"]

    # 3) - Création de la Combobox via la méthode ttk.Combobox()
    listeCombo = ttk.Combobox(rootwindow, values=listeProduits)
    
    # 4) - Choisir l'élément qui s'affiche par défaut
    listeCombo.current(0)

    listeCombo.grid(row=6, column=3, padx=10, pady=10)
    



    label_DateD = Label(rootwindow, text="Date depart")
    label_DateD.grid(row=7, column=2, padx=10, pady=10)
    Calendrier = Calendar(rootwindow, selectmode='day', year=2024, month=6, day=10)
    Calendrier.grid(row=7, column=3, padx=10, pady=10)
    # Bouton pour obtenir la date sélectionnée
    submit_button = Button(rootwindow, text="Recherche", command=donnee_form)
    submit_button.grid(row=8, column=3, padx=10, pady=10)



    

    rootwindow.mainloop()



Index()