from tkinter import ttk 
import tkinter as tk
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
       c.execute("INSERT INTO Accounts VALUES (:AccID, :UserID, :ServiceName, :Login, :Password, :Note)", {'AccID': account.accID, 'UserID': account.uid, 'ServiceName': account.serName, 'Login': account.login, 'Password': account.password, 'Note': account.note})

def selectAccounts(uid):
    with conn:
        c.execute("SELECT * FROM Accounts WHERE UserID=?",(uid,))
        list = c.fetchall()
        return list

def selectDecoded(uid):
    accID = 1
    tup = ()
    decoded_list = []
    
    while(accID <= pullNumber(uid)):
        with conn:
            c.execute("SELECT ServiceName FROM Accounts WHERE UserID=? AND AccID=?",(uid,accID))
            service_name = c.fetchone()[0]
        
            c.execute("SELECT Login FROM Accounts WHERE UserID=? AND AccID=?",(uid,accID))
            login = c.fetchone()[0]

            c.execute("SELECT Password FROM Accounts WHERE UserID=? AND AccID=?",(uid,accID))
            password = c.fetchone()[0]
            password = KDF.decode(password,getKey(uid)).decode()
        
            c.execute("SELECT Note FROM Accounts WHERE UserID=? AND AccID=?",(uid,accID))
            note = c.fetchone()[0]

            tup = tup + (service_name,login,password,note)
        
            print(tup)
            
            decoded_list.append(tup)
            
            tup = ()

            accID = accID + 1

    print(decoded_list)
    
        
    return decoded_list

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

            c.execute("SELECT Salt from Users WHERE Username=?",(uname,))
            output = c.fetchone()[0] 
            #print(output)

            attempt = KDF.deriveKey(pword,output)

        if attempt == password:
            return True

        else:
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
            

conn.commit()