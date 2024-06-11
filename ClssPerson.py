from ClssUsers import * 
from createdatabase import *

class CPerson(object) :

    def __init__(self) :
        pass
    
    def signin(self, nom,prenom,email,password):
        print("Inscription")
        CUsers(email,password,None,prenom+nom)

             


    def login(self,mail,password):
        utilisateur=0
        print("Connexion\n")
        print("Pas de compte ?\n")
        print("Entrer 1 pour vous inscrire 0 sinon")
        reponse = int(input("Entrez la reponse ici :"))
        if reponse ==1 :
            print("Veuillez entrer votre nom")
            nom = input(">>")
            print("Veuillez entrer votre prenom")
            prenom = input(">>")
            utilisateur=self.signin(nom,prenom,mail,password)
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
                


    

