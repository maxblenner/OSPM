#file for key derivation

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def genSalt():
    salt = os.urandom(16)
    return salt

def deriveKey(input,salt):
    
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    )

    key = base64.urlsafe_b64encode(kdf.derive(input)) #derives a key from the input and the salt
    
    return key

def encode(pw,key):
    f = Fernet(key)
    token = f.encrypt(pw)
    return token

def decode(token,key):
    f = Fernet(key)
    pw = f.decrypt(token)
    return pw



