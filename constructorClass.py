import KDF

class User:
    
    #user object constructor
    def __init__(self, ID, username, password):
        self.id =       ID
        self.username = username 
        self.salt =     KDF.genSalt()
        self.password = KDF.deriveKey(password,self.salt)

class Account:

    #account object constructor
    def __init__(self, uid, serName, login, password, note):
        self.uid =      uid
        self.serName =  serName 
        self.login =    login
        self.password = password
        self.note =     note