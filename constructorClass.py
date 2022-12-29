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
    def __init__(self, accID, uid, serName, login, password, note, key):
        self.accID =    accID  
        self.uid =      uid
        self.serName =  serName 
        self.login =    login
        self.password = KDF.encode(password,key)
        self.note =     note