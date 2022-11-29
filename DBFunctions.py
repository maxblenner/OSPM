from constructorClass import User, Account
import sqlite3
import KDF


conn = sqlite3.connect('OSPM.db') #connects to or constructs the database
c = conn.cursor()

def insertUser(user):
    #salt = KDF.genSalt()
    with conn: 
       c.execute("INSERT INTO Users VALUES (:ID, :Username, :Password, :Salt)", {'ID': user.id, 'Username': user.username, 'Password': user.password, 'Salt': user.salt}) 

def insertAccount(account):
    with conn: 
       c.execute("INSERT INTO Accounts VALUES (:AccID, :UserID, :ServiceName, :Login, :Password, :Note)", {'AccID': account.accID, 'UserID': account.uid, 'ServiceName': account.serName, 'Login': account.login, 'Password': account.password, 'Note': account.note})

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

def getID(username):
    with conn:
        c.execute("SELECT ID FROM Users WHERE Username=?",(username,))
        UID = c.fetchone()[0]
        return UID

def verifyLogin(uname, pword):
   
    #c = conn.cursor()
    try:
        with conn:
            c.execute("SELECT Password from Users WHERE Username=?",(uname,))
            password = c.fetchone()[0]
            #print(password)

            c.execute("SELECT Salt from Users WHERE Username=?",(uname,))
            output = c.fetchone()[0] 
            #print(output)

            attempt = KDF.deriveKey(pword,output)

        if attempt == password:
            #print("Correct password!")
            return True

        else:
            #print("Incorrect credentials.")
            return False
    
    except:
        print("Error!")
        return False
    
def iterateID():
    with conn:    
        c.execute("SELECT * FROM Users WHERE ID = (SELECT MAX(ID) FROM Users)") #selects largest ID from table
        pull = c.fetchone()[0]
        ID = pull + 1
        return ID

def pullNumber(uid):
    with conn:
        c.execute("SELECT COUNT(*) FROM Accounts WHERE UserID =?",(uid,))
        i = c.fetchone()[0]
        return i

def pullAccounts(uid,i):
    x = 1
    with conn:
            while(x < 4):
                c.execute("SELECT * FROM Accounts WHERE UserID =?",(uid,))
                pullRow = c.fetchall()
                print(pullRow[x][i])
            
    
        
            


#user2 = User(iterateID(),'user2',b'letmein')
#insertUser(user2)

'''
c.execute("DELETE FROM Accounts WHERE UserID =2")
c.execute("DELETE FROM Accounts WHERE UserID =1")
c.execute("SELECT * FROM Accounts")
print(c.fetchall())
conn.commit()
'''

'''
account1_1 = Account((pullNumber(1)+1),1,'Amazon','JohnDoe123',KDF.encode(b'pass1',getKey(1)),None)
insertAccount(account1_1)
account1_2 = Account((pullNumber(1)+1),1,'YouTube','JohnDoeee123',KDF.encode(b'pass2',getKey(1)),None)
insertAccount(account1_2)
account2_1 = Account((pullNumber(2)+1),2,'Zulu','ASmithyy',KDF.encode(b'secret1',getKey(1)),None)
insertAccount(account2_1)
account2_2 = Account((pullNumber(2)+1),2,'eBay','ASmith221',KDF.encode(b'secret2',getKey(1)),None)
insertAccount(account2_2)


list1 = selectAccounts(1)
list2 = selectAccounts(2)
print(list1,list2)
'''


#print(list1,list2)

#pw = KDF.decode(getToken(1,'Amazon'),getKey(1))
#print(pw)

#pullAccounts(1,pullNumber(1))

conn.commit()

#verifyLogin()

#IDEA= Automate id selection by selecting the IDs from table and choosing n+1



 
