import os
import base64
import bcrypt
#import random
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC #key derivation function
from cryptography.hazmat.backends import default_backend


#salt = os.urandom(16)
#print(salt)

password = 'hello'



def genSalt():
    salt = bcrypt.gensalt()
    with open("testSalt.txt", 'wb') as f:
        f.write(salt)

def loadSalt():
    try:
        with open("testSalt.txt", 'rb') as f:
            salt = f.read()
            return salt
    except:        
        print("No salt file found!")        
        return None

def KDF(): 
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt = bcrypt.gensalt(),
    iterations=100000,
    backend=default_backend()
    )
    return kdf

def load_key(filename): #loads the local salt (key)
    try:
        filename =  filename 
        with open(filename, 'rb') as f:
            hashed = f.read()
            return hashed
    except:        
        print("No key file found!")        
        return None

#genSalt()

kdf = KDF()  

key = base64.urlsafe_b64decode(kdf.derive(password))
with open("fernetKey.txt", 'wb') as f:
        f.write(key)

#key = kdf.derive(password)

try: 
    kdf.verify(password,load_key('fernetKey.txt'))
    print("Verified...")
except:
    print("Incorrect")


#userIn = input("enter password: ")




#print("this is ...",key)



#key = load_key('fernetKey.txt')





#f = Fernet(key)
