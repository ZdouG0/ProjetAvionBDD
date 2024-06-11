from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from IHM_variable_glob import *
from createdatabase import *

def mesReservation():

    #création de la fenetre
    rootwindow = Tk()
    #configuration de la fenetre 
    rootwindow.configure(bg="light goldenrod") #on definit la couleur du fond d'ecran de la fenetre
    rootwindow.geometry("800x500") #on definit la taille de la fenetre
    rootwindow.title("Mes Reservations") #son titre
    sql = text("SELECT IdClient from Client where EmailClient='"+getUserEmail()+"';") 
    result = session.execute(sql)
    for Client in result:
        idClient= Client.IdClient
    stringMaQuery ="SELECT VilleDepart, VilleArrive, NomCategorie AS Categorie, DateVol AS Date,PrixBillet AS Prix,NomPresta, IdBillet FROM Billet  JOIN Vol  ON Vol.IdVol = Billet.IdVol JOIN Prestataire ON Prestataire.IdPrestataire = Vol.IdPrestataire JOIN Trajet  ON Vol.IdTrajet = Trajet.IdTrajet JOIN Categorie  ON Billet.IdCategorie = Categorie.IdCategorie WHERE Billet.IdClient = "+str(idClient)+";"
    sql = text(stringMaQuery) 
    result = session.execute(sql)


    def Annulation():
        Idbillet = listeCombo.get()
        
        sql = text("SELECT IdClient from Client where EmailClient='"+getUserEmail()+"';") 
        result = session.execute(sql)
        for Client in result:
            idclient= Client.IdClient
        sql = text("UPDATE Billet SET IdClient = 1 WHERE IdBillet ="+str(Idbillet)+";") 
        result = session.execute(sql)
        session.commit()
        messagebox.showinfo("Annulation","annulation effectué !")
        rootwindow.destroy()
        mesReservation()
    

    def redirect_index():
        rootwindow.destroy()
    



    Titre_label = Label(rootwindow, text='Resultat',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 20)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=1, column=2, padx=10, pady=10) #on le place

    label_Titre1 = Label(rootwindow, text="Ville Depart")
    label_Titre1.grid(row=2, column=3, padx=10, pady=10)

    label_Titre2 = Label(rootwindow, text="Ville Arrivée")
    label_Titre2.grid(row=2, column=4, padx=10, pady=10)

    label_Titre3 = Label(rootwindow, text="Categorie")
    label_Titre3.grid(row=2, column=6, padx=10, pady=10)

    label_Titre4 = Label(rootwindow, text="Date")
    label_Titre4.grid(row=2, column=5, padx=10, pady=10)

    label_Titre5 = Label(rootwindow, text="Prix")
    label_Titre5.grid(row=2, column=8, padx=10, pady=10)

    label_Titre5 = Label(rootwindow, text="Id Billet")
    label_Titre5.grid(row=2, column=2, padx=10, pady=10)

    label_Titre6 = Label(rootwindow, text="Prestataire")
    label_Titre6.grid(row=2, column=7, padx=10, pady=10)
                      
    i=3
    global IdbilletList
    IdbilletList=[]
    for info in result:
        IdbilletList.append(info.IdBillet)
        label_Categorie = Label(rootwindow, text=info.Categorie)
        label_Categorie.grid(row=i, column=6, padx=10, pady=10)

        label_Prix = Label(rootwindow, text=info.Prix)
        label_Prix.grid(row=i, column=8, padx=10, pady=10)

        label_date = Label(rootwindow, text=info.Date)
        label_date.grid(row=i, column=5, padx=10, pady=10)

        label_VilleD = Label(rootwindow, text=info.VilleDepart)
        label_VilleD.grid(row=i, column=3, padx=10, pady=10)
        
        label_VilleA = Label(rootwindow, text=info.VilleArrive)
        label_VilleA.grid(row=i, column=4, padx=10, pady=10)

        label_Idbillet= Label(rootwindow, text=info.IdBillet)
        label_Idbillet.grid(row=i, column=2, padx=10, pady=10)

        label_NomPresta= Label(rootwindow, text=info.NomPresta)
        label_NomPresta.grid(row=i, column=7, padx=10, pady=10)
        i+=1

    
    label_IDReserv = Label(rootwindow, text="id du billet a annuler")
    label_IDReserv.grid(row=i +1, column=2, padx=10, pady=10)
    

     
    listeCombo = ttk.Combobox(rootwindow, values=IdbilletList)
    listeCombo.current(0)
    listeCombo.grid(row=i +2, column=3, padx=10, pady=10)

    reserv_button = Button(rootwindow, text="Annuler", command=Annulation)
    reserv_button.grid(row = i+3, column=3, pady=20)

    Index_button = Button(rootwindow, text="Accueil", command=redirect_index)
    Index_button.grid(row=i+4, column=3, pady=20)

    rootwindow.mainloop()