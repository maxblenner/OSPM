import bcrypt

from masterPass import genSalt

password = b"hello"

#hashed = bcrypt.hashpw(password,bcrypt.gensalt(rounds=12))

def store_hashed(filename,password):   
    filepath = filename
    hashed = bcrypt.hashpw(password,bcrypt.gensalt(rounds=12))
    # Creates a new file
    with open(filepath, 'wb') as f:
        f.write(hashed)

def load_hashed(filename): #loads the local salt (key)
    try:
        filename =  filename 
        with open(filename, 'rb') as f:
            hashed = f.read()
            return hashed
    except:        
        print("No hash file found!")        
        return None

#store_hashed("hashedTest.txt",password)

#hashed = load_hashed("hashedTest.txt")


userIn = input("Enter password: ").encode()
if bcrypt.checkpw(userIn,load_hashed("hashedTest.txt")):
    print("Correct password")
else:
    print("Incorrect credentials")

#print(hashed)