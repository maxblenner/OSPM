from cryptography.fernet import Fernet


def create_key(filename):   
    filepath = filename
    key = Fernet.generate_key()
    # Creates a new file
    with open(filepath, 'wb') as f:
        f.write(key)
    
#create_key("testKey.txt")

password = "hello".encode()



