import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = b"password"


#b'$2b$12$WK1KTrdX/njjDlhAJ9Oese'

def genSalt():
    salt = os.urandom(16)
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

'''
def saveKey(key):
    with open("testKey.txt", 'wb') as f:
        f.write(key)

def loadKey():
    try:
        with open("testKey.txt", 'rb') as f:
            key = f.read()
            return key
    except:        
        print("No key file found!")        
        return None
'''

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=loadSalt(),
    iterations=100000,
)

#genSalt()

key = base64.urlsafe_b64encode(kdf.derive(password))

#saveKey(key)

#key = loadKey()
f = Fernet(key)

print(loadSalt())


#using encryption/decryption

token = f.encrypt(b"Secret message!")
token2 = f.encrypt(b"password2")
#token
#b'...'
print(f.decrypt(token).decode())
print(f.decrypt(token2).decode())
#b'Secret message!'
print(token)
print(token2)





print("\nTesting...")

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=loadSalt(),
    iterations=100000,
)

print(loadSalt())

userIn = b'password' #input("Enter password...")#.encode()

pw = base64.urlsafe_b64encode(kdf.derive(password))

print(pw)
print(key)



#print()
#print(key)

#if user