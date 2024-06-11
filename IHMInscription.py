from tkinter import *
from tkinter import ttk
from tkinter import messagebox




def Inscription():
    #création de la fenetre
    rootwindow = Tk()
    #configuration de la fenetre 
    rootwindow.configure(bg="light goldenrod") #on definit la couleur du fond d'ecran de la fenetre
    rootwindow.geometry("500x400") #on definit la taille de la fenetre
    rootwindow.title("Inscription") #son titre


    def redirect_index():
        rootwindow.destroy()
        

    Titre_label = Label(rootwindow, text='Inscription',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 40)) #création du label qui affichera le nom du jeu 
    Titre_label.grid(row=0, column=3, padx=10, pady=10) #on le place


    Index_button = Button(rootwindow, text="Accueil", command=redirect_index)
    Index_button.grid(row=1, column=4, pady=20)


    def donnee_form():
        name = entry_name.get()
        prenom = entry_prenom.get()
        print(prenom)
        print(name)
        password = entry_password.get()
        password2 = entry_password2.get()
        if (password !=password2):
            messagebox.showinfo("Erreur","Une erreur est survenue : les mots de passes sont different")
        #si email existe deja le notifier !!



    label_name = Label(rootwindow, text="Nom")
    label_name.grid(row=1, column=2, padx=10, pady=10)
    entry_name = Entry(rootwindow)
    entry_name.grid(row=1, column=3, padx=10, pady=10)

    label_prenom = Label(rootwindow, text="Prenom")
    label_prenom.grid(row=2, column=2, padx=10, pady=10)
    entry_prenom = Entry(rootwindow)
    entry_prenom.grid(row=2, column=3, padx=10, pady=10)


    label_email = Label(rootwindow, text="Email")
    label_email.grid(row=3, column=2, padx=10, pady=10)
    entry_email = Entry(rootwindow)
    entry_email.grid(row=3, column=3, padx=10, pady=10)

    label_password = Label(rootwindow, text="Password")
    label_password.grid(row=4, column=2, padx=10, pady=10)
    entry_password = Entry(rootwindow)
    entry_password.grid(row=4, column=3, padx=10, pady=10)

    label_password2 = Label(rootwindow, text="Confirmer Password")
    label_password2.grid(row=5, column=2, padx=10, pady=10)
    entry_password2 = Entry(rootwindow)
    entry_password2.grid(row=5, column=3, padx=10, pady=10)


    # Bouton de soumission
    submit_button = Button(rootwindow, text="Inscription", command=donnee_form)
    submit_button.grid(row=6, columnspan=5, pady=20)
    rootwindow.mainloop()

