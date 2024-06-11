from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from createdatabase import *



def Inscription():
    #création de la fenetre
    rootwindow = Tk()
    #configuration de la fenetre 
    rootwindow.configure(bg="light goldenrod") #on definit la couleur du fond d'ecran de la fenetre
    rootwindow.geometry("500x600") #on definit la taille de la fenetre
    rootwindow.title("Inscription") #son titre


    def redirect_index():
        rootwindow.destroy()
        

    Titre_label = Label(rootwindow, text='Inscription',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 40)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=0, column=3, padx=10, pady=10) #on le place


    Index_button = Button(rootwindow, text="Accueil", command=redirect_index)
    Index_button.grid(row=1, column=4, pady=20)


    def donnee_form():
        session = Session()
        name = entry_name.get()
        adresse = entry_adresse.get()
        tel = entry_tel.get()
        nationalite = entry_nationalite.get()
        age = entry_age.get()
        email = entry_email.get()
        password = entry_password.get()
        password2 = entry_password2.get()

        if (password !=password2):
            messagebox.showinfo("Erreur","Une erreur est survenue : les mots de passes sont different")
        else:
            sql = text("SELECT * from Client WHERE Client.EmailClient ='"+email+"'") 
            result = session.execute(sql)
            if result.rowcount ==0 :
                
                sql = text("Insert into Client(NomClient,AgeClient,Nationalite,EmailClient,PasswordClient,TelephoneClient,Adresse) Values('"+name+"',"+str(age)+",'"+nationalite+"','"+email+"','"+password+"',"+str(tel)+",'"+adresse+"');") 
                result = session.execute(sql)
                session.commit()
                messagebox.showinfo("Inscription","Inscription validée veuillez vous connecter !")
                rootwindow.destroy()
            else :
                messagebox.showinfo("Erreur","Une erreur est survenue : cette email est deja liée a un compte")
        #si email existe deja le notifier !!



    label_name = Label(rootwindow, text="Nom")
    label_name.grid(row=1, column=2, padx=10, pady=10)
    entry_name = Entry(rootwindow)
    entry_name.grid(row=1, column=3, padx=10, pady=10)


    label_nationalite = Label(rootwindow, text="Nationalite")
    label_nationalite.grid(row=2, column=2, padx=10, pady=10)
    entry_nationalite = Entry(rootwindow)
    entry_nationalite.grid(row=2, column=3, padx=10, pady=10)

    label_adresse = Label(rootwindow, text="Adresse")
    label_adresse.grid(row=3, column=2, padx=10, pady=10)
    entry_adresse = Entry(rootwindow)
    entry_adresse.grid(row=3, column=3, padx=10, pady=10)

    label_tel = Label(rootwindow, text="Telephone")
    label_tel.grid(row=4, column=2, padx=10, pady=10)
    entry_tel = Entry(rootwindow)
    entry_tel.grid(row=4, column=3, padx=10, pady=10)

    label_age = Label(rootwindow, text="Age")
    label_age.grid(row=5, column=2, padx=10, pady=10)
    entry_age = Entry(rootwindow)
    entry_age.grid(row=5, column=3, padx=10, pady=10)

    label_email = Label(rootwindow, text="Email")
    label_email.grid(row=6, column=2, padx=10, pady=10)
    entry_email = Entry(rootwindow)
    entry_email.grid(row=6, column=3, padx=10, pady=10)

    label_password = Label(rootwindow, text="Password")
    label_password.grid(row=7, column=2, padx=10, pady=10)
    entry_password = Entry(rootwindow)
    entry_password.grid(row=7, column=3, padx=10, pady=10)

    label_password2 = Label(rootwindow, text="Confirmer Password")
    label_password2.grid(row=8, column=2, padx=10, pady=10)
    entry_password2 = Entry(rootwindow)
    entry_password2.grid(row=8, column=3, padx=10, pady=10)


    # Bouton de soumission
    submit_button = Button(rootwindow, text="Inscription", command=donnee_form)
    submit_button.grid(row=9, columnspan=5, pady=20)
    rootwindow.mainloop()

