from constructorClass import User, Account
import sqlite3
import KDF


conn = sqlite3.connect('OSPM.db') #connects to or constructs the database
c = conn.cursor()

def insertUser(user):
    salt = KDF.genSalt()
    with conn: 
       c.execute("INSERT INTO Users VALUES (:ID, :Username, :Password, :Salt)", {'ID': user.id, 'Username': user.username, 'Password': user.password, 'Salt': user.salt}) 

def insertAccount(account):
    with conn: 
       c.execute("INSERT INTO Accounts VALUES (:UserID, :ServiceName, :Login, :Password, :Note)", {'UserID': account.uid, 'ServiceName': account.serName, 'Login': account.login, 'Salt': account.salt, 'Note': account.note})

def verifyLogin():
    userIn = input("Username: ")
    print(userIn)
    userIn2 = input("Password: ").encode()
    print("Verifying...")

    #c = conn.cursor()
    try:
        c.execute("SELECT Password from Users WHERE Username=?",(userIn,))
        password = c.fetchone()[0]
        print(password)

        c.execute("SELECT Salt from Users WHERE Username=?",(userIn,))
        output = c.fetchone()[0] 
        print(output)

        attempt = KDF.deriveKey(userIn2,output)

        if attempt == password:
            print("Correct password!")
            return True

        else:
            print("Incorrect credentials.")
            return False
    
    except:
        print("Error!")
        return False


#this is a test addition
'''
salt = KDF.genSalt()
user1 = User(1,'user1',KDF.deriveKey(b'hello',salt),salt)
insertUser(user1)
'''

#test addition with decoding added
'''
salt = KDF.genSalt()
pw = KDF.deriveKey(b'hello',salt)
user2 = User(2,'user1',pw.decode('unicode_escape'),salt.decode('unicode_escape'))
insertUser(user2)
'''

c.execute("SELECT * FROM Users")
print(c.fetchall())

verifyLogin()


#user2 = User(2,'user2',userIn)
#IDEA= Automate id selection by selecting the IDs from table and choosing n+1



 
