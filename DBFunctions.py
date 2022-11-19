from constructorClass import User, Account
import sqlite3
import KDF


conn = sqlite3.connect('OSPM.db') #connects to or constructs the database
c = conn.cursor()

def insertUser(user):
    with conn: 
       c.execute("INSERT INTO Users VALUES (:ID, :Username, :Password, :Salt)", {'ID': user.id, 'Username': user.username, 'Password': user.password, 'Salt': user.salt}) 

def insertAccount(account):
    with conn: 
       c.execute("INSERT INTO Accounts VALUES (:UserID, :ServiceName, :Login, :Password, :Note)", {'UserID': account.uid, 'ServiceName': account.serName, 'Login': account.login, 'Salt': account.salt, 'Note': account.note})

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



print("Verify password for user1...")
c.execute("SELECT Salt from Users WHERE ID=1")
output = c.fetchone()[0]
conn.commit()
userIn = input("password = ").encode()

attempt = KDF.deriveKey(userIn,output)

c.execute("SELECT Password from Users WHERE ID=1")
output = c.fetchone()[0]

if attempt == output:
    print("Correct password!")

else:
    print("Incorrect credentials")




 
