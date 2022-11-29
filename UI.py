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

    Label(reg_screen, text = "User Added.", fg = "green", font = ("Times", 11)).pack()



def register():
    global reg_screen
    reg_screen = Toplevel(screen)
    reg_screen.title("Create Account")
    reg_screen.geometry("300x250")

    global reg_username
    global reg_password
    global reg_username_entry
    global reg_password_entry
    reg_username = StringVar()
    reg_password = StringVar()

    Label(reg_screen, text = "Please enter new user details below:").pack()
    Label(reg_screen, text = "").pack()
    Label(reg_screen, text = "Username * ").pack()
    reg_username_entry = Entry(reg_screen, textvariable = reg_username)
    reg_username_entry.pack()
    Label(reg_screen, text = "Password * ").pack()
    reg_password_entry = Entry(reg_screen, textvariable = reg_password)
    reg_password_entry.pack()
    Button(reg_screen, text = "Create Account", width = 12, height = 1, command = register_user).pack()


def login_user():
    username_entry = login_username.get()
    password_entry = login_password.get()
    global UID

    if DBFunctions.verifyLogin(username_entry, password_entry.encode()) == True:
        Label(login_screen, text = "Login Successful!", fg = "green", font = ("Times", 11)).pack()
        UID =  DBFunctions.getID(username_entry)
        #user_dash
    else:
        Label(login_screen, text = "Incorrect credentials", fg = "red", font = ("Times", 11)).pack()

    login_username_entry.delete(0,END)
    login_password_entry.delete(0,END)

    #Label(screen1, text = "User Added.", fg = "green", font = ("Times", 11)).pack()

def login():
    global login_screen
    login_screen = Toplevel(screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")

    global login_username
    global login_password
    global login_username_entry
    global login_password_entry
    login_username = StringVar()
    login_password = StringVar()

    Label(login_screen, text = "Please enter user details below:").pack()
    Label(login_screen, text = "").pack()
    
    Label(login_screen, text = "Username  ").pack()
    login_username_entry = Entry(login_screen, textvariable = login_username)
    login_username_entry.pack()
    
    Label(login_screen, text = "Password  ").pack()
    login_password_entry = Entry(login_screen, textvariable = login_password)
    login_password_entry.pack()
    
    Button(login_screen, text = "Login", width = 12, height = 1, command = login_user).pack()


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

def add_account():
    add_serName_in = add_serName.get()
    add_login_in = add_serName.get()
    add_password_in = add_password.get()
    add_note_in = add_note.get()

    acc = Account((DBFunctions.pullNumber(UID)+1),UID,add_serName_in,add_login_in,add_password_in,add_note_in)
    DBFunctions.insertAccount(acc)

    add_serName_entry.delete(0,END)
    add_login_entry.delete(0,END)
    add_password_entry.delete(0,END)
    add_note_entry.delete(0,END)

    Label(add_account_screen, text = "Account Added.", fg = "green", font = ("Times", 11)).pack()

def account_entry():
    global add_account_screen
    add_account_screen = Toplevel(screen)
    add_account_screen.title("Add Account")
    add_account_screen.geometry("300x250")

    global add_serName
    global add_login
    global add_password
    global add_note
    global add_serName_entry
    global add_login_entry
    global add_password_entry
    global add_note_entry
    add_serName = StringVar()
    add_login = StringVar()
    add_password = StringVar()
    add_note = StringVar()

    Label(add_account_screen, text = "Please enter new account details below:").pack()
    Label(add_account_screen, text = "").pack()
    
    Label(add_account_screen, text = "Service Name ").pack()
    add_serName_entry = Entry(add_account_screen, textvariable = add_serName)
    add_serName_entry.pack()
    
    Label(add_account_screen, text = "Login ").pack()
    add_login_entry = Entry(add_account_screen, textvariable = add_login)
    add_login_entry.pack()

    Label(add_account_screen, text = "Password ").pack()
    add_password_entry = Entry(add_account_screen, textvariable = add_password)
    add_password_entry.pack()

    Label(add_account_screen, text = "Note (Optional) ").pack()
    add_note_entry = Entry(add_account_screen, textvariable = add_note)
    add_note_entry.pack()

    
    Button(add_account_screen, text = "Add Account", width = 12, height = 1, command = add_account).pack()

def user_dash():
    global user_screen
    i = 0
    user_screen = Toplevel(screen)
    user_screen.title("Your Dashboard")
    user_screen.geometry("500x420")
    
    Label(text = "OSPM 1.0", bg = "grey", width = "300", height = "2", font = ("Times", 13)).pack()
    
    while(i < DBFunctions.pullNumber(UID)):
        
        Label(text = "").pack()
        Button(text = "Add Account", height = "2", width = "30", command = account_entry).pack()
        Label(text = "").pack()
    
main_screen()


