import os
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC #key derivation function
from cryptography.hazmat.backends import default_backend

#salt = os.urandom(16)
#print(salt)

password = b'hello'

def KDF(): 
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt = os.urandom(16),
    iterations=100000,
    backend=default_backend()
    )
    return kdf

kdf = KDF()  

#key = kdf.derive(password)
key = base64.urlsafe_b64decode(kdf.derive(password))


print("this is ...",key)

#userIn = input("enter password: ")
kdf.verify(password,key)

f = Fernet(key)
