from base64 import encodebytes
from encodings import utf_8
import bcrypt
import hashlib

def genSalt(): #using bcrypt to generate a random salt
    salt = bcrypt.gensalt()
    return salt

def hashInput(userIn): #hashing input
    hashed = hashlib.md5(userIn).hexdigest().encode()
    return hashed

def addSalt(userIn, salt): #concatenate user in with salt    
    salted = userIn + salt 
    hashed = hashInput(salted) #.encode()
    return hashed.decode('ascii')

def genSaltFile(filename): #writing salt to a file for persistence
    filepath = filename
    salt = genSalt()
    # Creates a new file
    with open(filepath, 'wb') as f:
        f.write(salt)

def loadSalt(filename): #loads the local salt (key)
    try:
        filename =  filename 
        with open(filename, 'rb') as f:
            salt = f.read()
            return salt
        
    except:        
        print("No local key file found!, key created")        
        return None

def checkPassword(userIn, storedPW, salt): #checks user input against stored salted password by salting the password with the same salt and comparing the results
    saltedIn = addSalt(userIn, salt)
    
    if saltedIn == storedPW:
        print("Correct Password!")
        return True
    else:
        print("Incorrect Password.")
        return False


#genSaltFile("salt.txt")

masterPass = input("Enter Password Master Password: ").encode()
print(masterPass)



hashed = addSalt(masterPass,loadSalt("salt.txt"))
print(hashed)

