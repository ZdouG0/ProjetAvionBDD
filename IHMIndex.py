from tkinter import *
from tkinter import ttk
from tkinter import messagebox


from tkcalendar import Calendar, DateEntry
from IHMConnexion import Connexion
from IHMResultRecherche import ResultRecherche
from IHMmesReservation import mesReservation
from IHM_variable_glob import *
from createdatabase import *

def Index():
    
    #création de la fenetre
    rootwindow = Tk()
    #configuration de la fenetre 
    rootwindow.configure(bg="light goldenrod") #on definit la couleur du fond d'ecran de la fenetre
    rootwindow.geometry("500x650") #on definit la taille de la fenetre
    rootwindow.title("Accueil") #son titre

    def donnee_form():
        villeD = listeVilleD.get()
        villeA = listeVilleA.get()
        date = Calendrier.get_date()
        prix = entry_Prix.get()
        categorie = listeCat.get()
        prestataire = listeComboprest.get()
        #if (pas de compte):
            #messagebox.showinfo("Erreur","Une erreur est survenue : Mots de passe ou email incorrect")
        ResultRecherche(villeA,villeD,date,prix,categorie,prestataire)

    def redirect_connexion():
        
        Connexion()


    def redirect_mesReserv():
        
        if (getUserEmail()):
            mesReservation()
        else :
            messagebox.showinfo("Erreur","Une erreur est survenue : Vous n'etes aps connecte")
    
    # Si connecter voir ses reservation
    Reserv_button = Button(rootwindow, text="Voir mes reservations", command=redirect_mesReserv)
    Reserv_button.grid(row=1, column=4, pady=20)

    Titre_label = Label(rootwindow, text='Accueil',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 40)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=0, column=3, padx=10, pady=10) #on le place

    
    Connexion_button = Button(rootwindow, text="Se connecter", command=redirect_connexion)
    Connexion_button.grid(row=0, column=4, pady=20)

    Titre_label = Label(rootwindow, text='Recherche',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 20)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=1, column=3, padx=10, pady=10) #on le place

    sql = text("SELECT NomVille FRom ville;") 
    result = session.execute(sql)
    session.commit()
    listVille=[]
    for ville in result :
        listVille.append(ville.NomVille)

    
    label_villeD = Label(rootwindow, text="Ville de Départ")
    label_villeD.grid(row=2, column=2, padx=10, pady=10)
    listeVilleD = ttk.Combobox(rootwindow, values=listVille)
    listeVilleD.current(0)
    listeVilleD.grid(row=2, column=3, padx=10, pady=10)
    



    label_villeA = Label(rootwindow, text="Ville d'arrivée")
    label_villeA.grid(row=3, column=2, padx=10, pady=10)
    listeVilleA = ttk.Combobox(rootwindow, values=listVille)
    listeVilleA.current(0)
    listeVilleA.grid(row=3, column=3, padx=10, pady=10)



    sql = text("SELECT NomPresta FRom prestataire;") 
    result = session.execute(sql)
    session.commit()
    listePrest=[]
    for prest in result :
        listePrest.append(prest.NomPresta)

    label_Prestataire = Label(rootwindow, text="Prestataire")
    label_Prestataire.grid(row=4, column=2, padx=10, pady=10)

    listeComboprest = ttk.Combobox(rootwindow, values=listePrest)
    listeComboprest.current(0)
    listeComboprest.grid(row=4, column=3, padx=10, pady=10)


    label_Prix = Label(rootwindow, text="Prix minimum")
    label_Prix.grid(row=5, column=2, padx=10, pady=10)
    entry_Prix = Entry(rootwindow)
    entry_Prix.grid(row=5, column=3, padx=10, pady=10)




    label_Categorie = Label(rootwindow, text="Categorie")
    label_Categorie.grid(row=6, column=2, padx=10, pady=10)

    sql = text("SELECT NomCategorie FRom categorie;") 
    result = session.execute(sql)
    session.commit()
    listeProduits=[]
    for cat in result :
        listeProduits.append(cat.NomCategorie)

    
    listeCat = ttk.Combobox(rootwindow, values=listeProduits)
    listeCat.current(0)
    listeCat.grid(row=6, column=3, padx=10, pady=10)
    



    label_DateD = Label(rootwindow, text="Date depart")
    label_DateD.grid(row=7, column=2, padx=10, pady=10)
    Calendrier = Calendar(rootwindow, selectmode='day', year=2024, month=6, day=10)
    Calendrier.grid(row=7, column=3, padx=10, pady=10)
    # Bouton pour obtenir la date sélectionnée
    submit_button = Button(rootwindow, text="Recherche", command=donnee_form)
    submit_button.grid(row=8, column=3, padx=10, pady=10)



    

    rootwindow.mainloop()



Index()