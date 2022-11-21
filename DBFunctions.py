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
       c.execute("INSERT INTO Accounts VALUES (:UserID, :ServiceName, :Login, :Password, :Note)", {'UserID': account.uid, 'ServiceName': account.serName, 'Login': account.login, 'Password': account.password, 'Note': account.note})

def selectAccounts(uid):
    with conn:
        c.execute("SELECT * FROM Accounts WHERE UserID=?",(uid,))
        list = c.fetchall()
        return list

def getKey(id):
    with conn:
        c.execute("SELECT Password FROM Users WHERE ID=?",(id,))
        key = c.fetchone()[0]
        return key

def getToken(uid,serName):
    with conn:
        c.execute("SELECT Password FROM Accounts WHERE UserID=? AND ServiceName=?",(uid,serName,))
        token = c.fetchone()[0]
        return token


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
    
def iterateID():
    c.execute("SELECT * FROM Users WHERE ID = (SELECT MAX(ID) FROM Users)") #selects largest ID from table
    pull = c.fetchone()[0]
    ID = pull + 1
    return ID



#user2 = User(iterateID(),'user2',b'letmein')
#insertUser(user2)

'''
account1_1 = Account(1,'Amazon','JohnDoe123',KDF.encode(b'pass1',getKey(1)),None)
account1_2 = Account(1,'YouTube','JohnDoeee123',KDF.encode(b'pass2',getKey(1)),None)
account2_1 = Account(2,'Zulu','ASmithyy',KDF.encode(b'secret1',getKey(1)),None)
account2_2 = Account(2,'eBay','ASmith221',KDF.encode(b'secret2',getKey(1)),None)
insertAccount(account1_1)
insertAccount(account1_2)
insertAccount(account2_1)
insertAccount(account2_2)
'''

#c.execute("DELETE FROM Users WHERE ID=2")

c.execute("SELECT * FROM Users")
print(c.fetchall())

list1 = selectAccounts(1)
list2 = selectAccounts(2)

print(list1,list2)

pw = KDF.decode(getToken(1,'Amazon'),getKey(1))
print(pw)

conn.commit()

#verifyLogin()

#IDEA= Automate id selection by selecting the IDs from table and choosing n+1



 
