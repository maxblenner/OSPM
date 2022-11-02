import bcrypt

from masterPass import genSalt

password = b"hello"

hashed = bcrypt.hashpw(password,bcrypt.gensalt(rounds=14))

userIn = input("Enter password: ").encode()
if bcrypt.checkpw(userIn,hashed):
    print("Correct password")
else:
    print("Incorrect credentials")

print(hashed)