class User:
    
    #user object constructor
    def __init__(self, id, username, password, salt):
        self.id =       id
        self.username = username 
        self.password = password
        self.salt =     salt

class Account:

    #account object constructor
    def __init__(self, uid, serName, login, password, note):
        self.uid =      uid
        self.serName =  serName 
        self.login =    login
        self.password = password
        self.note =     note