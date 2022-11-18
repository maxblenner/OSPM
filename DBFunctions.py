from constructorClass import User, Account
import sqlite3


conn = sqlite3.connect('OSPM.db') #connects to or constructs the database
c = conn.cursor()

def insertUser(user):
    with conn: 
       c.execute("INSERT INTO Users VALUES (:ID, :Username, :Password, :Salt)", {'ID': user.id, 'Username': user.username, 'Password': user.password, 'Salt': user.salt}) 

def insertAccount(account):
    with conn: 
       c.execute("INSERT INTO Accounts VALUES (:UserID, :ServiceName, :Login, :Password, :Note)", {'UserID': account.uid, 'ServiceName': account.serName, 'Login': account.login, 'Salt': account.salt, 'Note': account.note})

