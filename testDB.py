import sqlite3
from test_acc import test_account

conn = sqlite3.connect('testDB.db')

c = conn.cursor()

def insert_account(acc):
    with conn:
        c.execute("INSERT INTO accounts VALUES (:user_name, :password)", {'user_name': acc.user_name, 'password': acc.password})

acc1 = test_account('testuser3','testpassword3')
insert_account(acc1)

'''
c.execute("""CREATE TABLE accounts (
            user_name text,
            password text)
        """)
'''
#c.execute("INSERT INTO accounts VALUES ('testuser2','testpassword2')")




c.execute("SELECT * FROM accounts")

print(c.fetchall())

conn.commit() #submits transaction

conn.close()
