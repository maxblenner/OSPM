from tkinter import *
from constructorClass import User, Account
import DBFunctions

def register_user():
    uname_in = uname.get()
    pword_in = pword.get()

    user = User(DBFunctions.iterateID(), uname_in, pword_in.encode())
    DBFunctions.insertUser(user)

    uname_entry.delete(0,END)
    pword_entry.delete(0,END)

    Label(screen1, text = "User Added.", fg = "green", font = ("Times", 11)).pack()

    

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Create Account")
    screen1.geometry("300x250")

    global uname
    global pword
    global uname_entry
    global pword_entry
    uname = StringVar()
    pword = StringVar()

    Label(screen1, text = "Please enter new user details below:").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    uname_entry = Entry(screen1, textvariable = uname)
    uname_entry.pack()
    Label(screen1, text = "Password * ").pack()
    pword_entry = Entry(screen1, textvariable = pword)
    pword_entry.pack()
    Button(screen1, text = "Create Account", width = 12, height = 1, command = register_user).pack()

def login():
    print("Login")

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("OSPM 1.0")
    Label(text = "OSPM 1.0", bg = "grey", width = "300", height = "2", font = ("Times", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Create Account", height = "2", width = "30", command = register).pack()

    screen.mainloop()
main_screen()


