from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def mesReservation():


    #création de la fenetre
    rootwindow = Tk()
    #configuration de la fenetre 
    rootwindow.configure(bg="light goldenrod") #on definit la couleur du fond d'ecran de la fenetre
    rootwindow.geometry("800x500") #on definit la taille de la fenetre
    rootwindow.title("Mes Reservations") #son titre

    def Annulation():
        pass
    

    def redirect_index():
        rootwindow.destroy()
    
    Index_button = Button(rootwindow, text="Accueil", command=redirect_index)
    Index_button.grid(row=9, column=3, pady=20)

    Titre_label = Label(rootwindow, text='Mes Reservations',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 20)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=1, column=2, padx=10, pady=10) #on le place

    label_Titre1 = Label(rootwindow, text="Ville Depart")
    label_Titre1.grid(row=2, column=2, padx=10, pady=10)

    label_Titre2 = Label(rootwindow, text="Ville Arrivée")
    label_Titre2.grid(row=2, column=3, padx=10, pady=10)

    label_Titre3 = Label(rootwindow, text="Categorie")
    label_Titre3.grid(row=2, column=4, padx=10, pady=10)

    label_Titre4 = Label(rootwindow, text="Date")
    label_Titre4.grid(row=2, column=5, padx=10, pady=10)

    label_Titre5 = Label(rootwindow, text="Prix")
    label_Titre5.grid(row=2, column=6, padx=10, pady=10)

    label_Titre5 = Label(rootwindow, text="Id Billet")
    label_Titre5.grid(row=2, column=7, padx=10, pady=10)


    for i in range (3,5) :
        label_Categorie = Label(rootwindow, text="Text a recup SQL")
        label_Categorie.grid(row=i, column=4, padx=10, pady=10)

        label_Prix = Label(rootwindow, text="Text a recup SQL")
        label_Prix.grid(row=i, column=6, padx=10, pady=10)

        label_date = Label(rootwindow, text="Text a recup SQL")
        label_date.grid(row=i, column=5, padx=10, pady=10)

        label_VilleD = Label(rootwindow, text="Text a recup SQL")
        label_VilleD.grid(row=i, column=2, padx=10, pady=10)
        
        label_VilleA = Label(rootwindow, text="Text a recup SQL")
        label_VilleA.grid(row=i, column=3, padx=10, pady=10)

        label_Idbillet= Label(rootwindow, text="Text a recup SQL")
        label_Idbillet.grid(row=i, column=7, padx=10, pady=10)

    

    label_IDReserv = Label(rootwindow, text="id reservation a annuler")
    label_IDReserv.grid(row=5, column=2, padx=10, pady=10)
    entry_IDReserv = Entry(rootwindow)
    entry_IDReserv.grid(row=5, column=3, padx=10, pady=10)

    reserv_button = Button(rootwindow, text="Annuler", command=Annulation)
    reserv_button.grid(row=8, column=3, pady=20)

    rootwindow.mainloop()