from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from IHMInscription import Inscription
from createdatabase import *
from IHM_variable_glob import*

def Connexion() :

    


    #création de la fenetre
    rootwindow = Tk()
    #configuration de la fenetre 
    rootwindow.configure(bg="light goldenrod") #on definit la couleur du fond d'ecran de la fenetre
    rootwindow.geometry("450x350") #on definit la taille de la fenetre
    rootwindow.title("Connexion") #son titre

    def donnee_form():
        global glob_userEmail
        password = entry_password.get()
        email = entry_email.get()
        session = Session()
        sql = text("SELECT * from Client WHERE Client.EmailClient ='"+email+"'") 
        result = session.execute(sql)
        if result.rowcount ==0 :
            messagebox.showinfo("Erreur","Une erreur est survenue : Mots de passe ou email incorrect")
        else : 
            setUserEmail(email)
            
            messagebox.showinfo("Connexion","Connexion reussie !")

    def redirect_inscrip():
        Inscription()

    def redirect_index():
        rootwindow.destroy()
        


    Titre_label = Label(rootwindow, text='Connexion',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 40)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=0, column=3, padx=10, pady=10) #on le place

    Index_button = Button(rootwindow, text="Accueil", command=redirect_index)
    Index_button.grid(row=1, column=4, pady=20)

    label_email = Label(rootwindow, text="Email")
    label_email.grid(row=1, column=2, padx=10, pady=10)
    entry_email = Entry(rootwindow)
    entry_email.grid(row=1, column=3, padx=10, pady=10)

    label_password = Label(rootwindow, text="Password")
    label_password.grid(row=2, column=2, padx=10, pady=10)
    entry_password = Entry(rootwindow)
    entry_password.grid(row=2, column=3, padx=10, pady=10)


    submit_button = Button(rootwindow, text="Connexion", command=donnee_form)
    submit_button.grid(row=3, column=3, pady=20)
    

    inscrip_button = Button(rootwindow, text="Pas de compte ? Inscription", command=redirect_inscrip)
    inscrip_button.grid(row=4, column=3, pady=20)
    rootwindow.mainloop()
