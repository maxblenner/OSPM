from tkinter import *
from constructorClass import User, Account
import DBFunctions

def register_user():
    reg_username_in = reg_username.get()
    reg_password_in = reg_password.get()

    user = User(DBFunctions.iterateID(), reg_username_in, reg_password_in.encode())
    DBFunctions.insertUser(user)

    reg_username_entry.delete(0,END)
    reg_password_entry.delete(0,END)

    Label(screen1, text = "User Added.", fg = "green", font = ("Times", 11)).pack()

    

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Create Account")
    screen1.geometry("300x250")

    global reg_username
    global reg_password
    global reg_username_entry
    global reg_password_entry
    reg_username = StringVar()
    reg_password = StringVar()

    Label(screen1, text = "Please enter new user details below:").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    reg_username_entry = Entry(screen1, textvariable = reg_username)
    reg_username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    reg_password_entry = Entry(screen1, textvariable = reg_password)
    reg_password_entry.pack()
    Button(screen1, text = "Create Account", width = 12, height = 1, command = register_user).pack()

def login_user():
    username_entry = login_username.get()
    password_entry = login_password.get()

    if DBFunctions.verifyLogin(username_entry, password_entry.encode()) == True:
        Label(userScreen, text = "Login Successful!", fg = "green", font = ("Times", 11)).pack()
    else:
        Label(userScreen, text = "Incorrect credentials", fg = "red", font = ("Times", 11)).pack()

    login_username_entry.delete(0,END)
    login_password_entry.delete(0,END)

    #Label(screen1, text = "User Added.", fg = "green", font = ("Times", 11)).pack()

def login():
    global userScreen
    userScreen = Toplevel(screen)
    userScreen.title("Login")
    userScreen.geometry("300x250")

    global login_username
    global login_password
    global login_username_entry
    global login_password_entry
    login_username = StringVar()
    login_password = StringVar()

    Label(userScreen, text = "Please enter user details below:").pack()
    Label(userScreen, text = "").pack()
    Label(userScreen, text = "Username  ").pack()
    login_username_entry = Entry(userScreen, textvariable = login_username)
    login_username_entry.pack()
    Label(userScreen, text = "Password  ").pack()
    login_password_entry = Entry(userScreen, textvariable = login_password)
    login_password_entry.pack()
    Button(userScreen, text = "Login", width = 12, height = 1, command = login_user).pack()



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


