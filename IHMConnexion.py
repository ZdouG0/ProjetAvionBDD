from tkinter import *
from tkinter import ttk

#création de la fenetre
rootwindow = Tk()
#configuration de la fenetre 
rootwindow.configure(bg="light goldenrod") #on definit la couleur du fond d'ecran de la fenetre
rootwindow.geometry("720x480") #on definit la taille de la fenetre
rootwindow.title("Login") #son titre

Titre_label = Label(rootwindow, text='Login',fg="black",bg="light goldenrod", font=('Berlin Sans FB Demi', 40)) #création du label qui affichera le nom du jeu 
Titre_label.place(x=270, y=25) #on le place

# Fonction pour récupérer les valeurs des zones de texte
def get_text():
    text1 = text_box1.get("1.0", END).strip()
    text2 = text_box2.get("1.0", END).strip()
    print(f"Texte 1: {text1}")
    print(f"Texte 2: {text2}")

# Création du premier label et de la première zone de texte
label1 = Label(rootwindow,bg="light goldenrod",text="Email :",font=('Berlin Sans FB Demi', 15))
label1.place(x=60, y=180)

text_box1 = Text(rootwindow, height=2, width=50)
text_box1.place(x=140, y=175)

# Création du deuxième label et de la deuxième zone de texte
label2 = Label(rootwindow,bg="light goldenrod", text="Password :",font=('Berlin Sans FB Demi', 15))
label2.place(x=30, y=277)

text_box2 = Text(rootwindow, height=2, width=50)
text_box2.place(x=140, y=280)

# Création d'un bouton pour récupérer les valeurs des zones de texte
submit_button = Button(rootwindow, text="Connexion", command=get_text)
submit_button.place(x=300, y=370)



rootwindow.mainloop()