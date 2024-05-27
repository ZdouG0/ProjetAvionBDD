from ClssUsers import * 
from createdatabase import *

class CPerson(object) :

    def __init__(self) :
        pass
    
    def signin(self):
        print("Inscription")
        nom = input("Entrez votre Nom d'utilisateur :")
        print("\n")
        phone = input("Entrez votre numero de telephone :")
        print("\n")
        EmailOK = False
        while EmailOK==False :
            email = input("Entrez votre email :")
            sql = text("SELECT * from Users WHERE Users.UserEmail ='"+email+"'") 
            result = session.execute(sql) 
            if result.rowcount == 0:
                EmailOK=True
            else :
                print("Un compte est deja associé a cette adresse email.\n")

        print("\n")
        PasswordOk = False
        while PasswordOk == False :
            password = input("Entrez votre mots de passe :")
            print("\n")
            password2 = input("Entrez a nouveau votre mots de passe :")
            if password == password2 :
                PasswordOk =True
                user=Users(UserName=nom,UserEmail=email,UserPassword=password,UserPhone=phone)
                session.add(user)
                session.commit()
                utilisateur = CUsers(email, password, phone,nom)
                print("Inscription reussi, entrez 1 pour vous connecter")
                print("\n")
                result=0;
                while(result!=1):
                    result = int(input())
                utilisateur = self.login()
            else :
                print ("Mots de passe different veuillez reesayer\n")
        return utilisateur
             


    def login(self):
        utilisateur=0
        print("Connexion\n")
        print("Pas de compte ?\n")
        print("Entrer 1 pour vous inscrire 0 sinon")
        reponse = int(input("Entrez la reponse ici :"))
        if reponse ==1 :
            utilisateur=self.signin()
        else:
            ConnexionOk=False
            while ConnexionOk==False :
                email = input("Veuillez entrer votre email :")
                print("\n")
                password = input("Veuillez entrer votre mots de passe :")
                #verfication de l'existence de l'utilisateur
                sql = text("SELECT * from Users WHERE Users.UserEmail ='"+email+"'") 
                result = session.execute(sql)
                if result.rowcount !=0 :
                    ConnexionOk=True
                    for param in result :
                        phone = param[4]
                        nom = param[2]
                        print ("phone :",phone,"\nnom :",nom)
                    utilisateur = CUsers(email, password, phone,nom)
                    print("Connexion reussie")
                else :
                    print("Erreur mots de passe ou email\n")
                    print("Veuillez reesayer\n")
        return utilisateur
                


    

