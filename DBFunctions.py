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
            
'''
c.execute("DELETE FROM Accounts WHERE ServiceName=?",('test',))
print("returning accounts: ")
c.execute("SELECT * FROM Accounts WHERE UserID=?",(1,))
list1 = c.fetchall()u
print(list1)
conn.commit()
'''

#1 Verify Login
print("#1 Verify Login")
uname = input("Username: ")
pword = input("Password: ").encode()
if(verifyLogin(uname,pword) == True):
    print("Welcome " + uname + "!")
    UID = getID(uname)
else:
    print("Verification failed.")

#2 Encode
print("#2 Encode")
userIn = input("Enter something to encode: ").encode()
encoded = KDF.encode(userIn,getKey(UID))
print(encoded)

#3 Decode
print("#3 Decode")
print("Decoding...")
decoded = KDF.decode(encoded,getKey(UID))
print("The decoded message is: " + decoded.decode())

#4 Add Account
print("#4 Add Account")
print("Add account to your password manager: ")
serName_in = input("Service name: ") 
login_in = input("Login: ")
password_in = KDF.encode(input("Password: ").encode(),getKey(UID))
note_in = input("Note(optional): ")

acc = Account(pullNumber(UID)+1,UID,serName_in,login_in,password_in,note_in)
insertAccount(acc)

c.execute("SELECT * FROM Accounts WHERE UserID =? AND AccID=?",(UID,pullNumber(UID)))
account = c.fetchall()
print(account)

#5 Show Accounts
print("#5 Show Accounts")
print("returning accounts: ")
list1 = selectAccounts(UID)
print(list1)


#6 Decode Password and Delete Account
print("#6 Decode Password and Delete Account")
service_in = input("Select an account to return decoded password by enterting the service name: ")
decoded_password = KDF.decode(getToken(UID,service_in),getKey(UID)).decode()
print(decoded_password)

delete_in = input("Select an account to delete by entering the service name: ")
c.execute("DELETE FROM Accounts WHERE UserID=? AND ServiceName=?",(UID,delete_in))

print("returning accounts: ")
list1 = selectAccounts(UID)
print(list1)

conn.commit()