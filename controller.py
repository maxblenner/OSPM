from masterPass import *
from en_decrypt import *

masterPass = "hello".encode()
print(masterPass)
key = addSalt(masterPass,loadSalt("salt.txt")).encode()
print(key)
#create_key("key.txt",key)

newPW = input("Enter a password to be encrypted: ")
print(newPW)
EnPW = encrypt_password(newPW,key)
print(EnPW)

print("Decrypting...")
print(decrypt_password(EnPW,key))