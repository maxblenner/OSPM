#file used to construct sqlite tables
import sqlite3


conn = sqlite3.connect('OSPM.db') #connects to or constructs the database
c = conn.cursor()

'''
c.execute("""CREATE TABLE Users (
            ID INTEGER PRIMARY KEY,
            Username TEXT NOT NULL,
            Password TEXT NOT NULL,
            Salt TEXT NOT NULL)
                                """)

#c.execute("""DROP TABLE Accounts""")

c.execute("""CREATE TABLE Accounts (
            AccID INTEGER NOT NULL,
            UserID INTEGER NOT NULL,
            ServiceName TEXT NOT NULL,
            Login TEXT NOT NULL,
            Password TEXT NOT NULL,
            Note TEXT NULL,
            FOREIGN KEY (UserID) REFERENCES Users (ID))
                                """)
'''

'''
c.execute("""DELETE FROM Accounts WHERE UserID = 1 AND AccID = 3""")
c.execute("""SELECT * FROM Accounts WHERE UserID = 1""")
show = c.fetchall()
print(show)
'''

conn.commit()