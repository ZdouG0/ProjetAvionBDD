
global glob_userEmail
glob_userEmail = None

def setUserEmail(email):
    global glob_userEmail
    glob_userEmail = email

def printUserEmail():
    print(glob_userEmail)

def getUserEmail():
    return glob_userEmail