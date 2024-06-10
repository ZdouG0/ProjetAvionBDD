from IHM_variable_glob import *



def Connexion() :
    def donnee_form():
        password = entry_password.get()
        email = entry_email.get()
        #if (pas de compte):
            #messagebox.showinfo("Erreur","Une erreur est survenue : Mots de passe ou email incorrect")

    def redirect_inscrip():
        pass
    Titre_label = Label(rootwindow, text='Connexion',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 40)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=0, column=3, padx=10, pady=10) #on le place

    label_email = Label(rootwindow, text="Email")
    label_email.grid(row=4, column=2, padx=10, pady=10)
    entry_email = Entry(rootwindow)
    entry_email.grid(row=4, column=3, padx=10, pady=10)

    label_password = Label(rootwindow, text="Password")
    label_password.grid(row=5, column=2, padx=10, pady=10)
    entry_password = Entry(rootwindow)
    entry_password.grid(row=5, column=3, padx=10, pady=10)


    submit_button = Button(rootwindow, text="Connexion", command=donnee_form)
    submit_button.grid(row=7, column=3, pady=20)
    

    inscrip_button = Button(rootwindow, text="Pas de compte ? Inscription", command=redirect_inscrip)
    inscrip_button.grid(row=8, column=3, pady=20)
    rootwindow.mainloop()

Connexion()