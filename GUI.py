from tkinter import *
from tkinter import ttk
import tkinter as tk
from constructorClass import User, Account
import DBFunctions

UID = None

def main_dash():
    
    global main_screen
    global tree
    main_screen = Tk()

    main_screen.geometry("1500x1000")
    main_screen.title("OSPM 1.0")
    Label(text = "OSPM 1.0", bg = "grey", width = "300", height = "2", font = ("Times", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Create Account", height = "2", width = "30", command = register).pack()
    Label(text = "").pack()
    Label(text = "").pack()

    tree = ttk.Treeview(main_screen, column=("c1", "c2", "c3","c4"), show='headings')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Service Name")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Login")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Password")
    tree.column("#4", anchor=tk.CENTER)
    tree.heading("#4", text="Note")
    tree.pack()
    Label(text = "").pack()
    Label(text = "").pack()

    button1 = tk.Button(text="Update data", command=fetch_accounts)

    button1.pack(pady=10)



    main_screen.mainloop()

def fetch_accounts():

    accounts = DBFunctions.selectDecoded(UID)

    for account in accounts:
        #print(account) 

        tree.insert("", tk.END, values=account)
    

def login():
    
    global login_screen
    login_screen = Toplevel(main_screen)
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

def login_user():
    username_entry = login_username.get()
    password_entry = login_password.get()
    global UID

    if DBFunctions.verifyLogin(username_entry, password_entry.encode()) == True:
        print("success")
        Label(login_screen, text = "Login Successful!", fg = "green", font = ("Times", 11)).pack()
        UID = DBFunctions.getID(username_entry)
        main_screen.update()
        login_screen.destroy()
    else:
        print("fail")
        Label(login_screen, text = "Incorrect credentials", fg = "red", font = ("Times", 11)).pack()

    #login_username_entry.delete(0,END)
    #login_password_entry.delete(0,END)

def register():
    global reg_screen
    reg_screen = Toplevel(main_screen)
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
    Label(reg_screen, text = "Username ").pack()
    reg_username_entry = Entry(reg_screen, textvariable = reg_username)
    reg_username_entry.pack()
    Label(reg_screen, text = "Password ").pack()
    reg_password_entry = Entry(reg_screen, textvariable = reg_password)
    reg_password_entry.pack()
    Button(reg_screen, text = "Create Account", width = 12, height = 1, command = register_user).pack()

def register_user():
    reg_username_in = reg_username.get()
    reg_password_in = reg_password.get()

    user = User(DBFunctions.iterateID(), reg_username_in, reg_password_in.encode())
    DBFunctions.insertUser(user)

    reg_username_entry.delete(0,END)
    reg_password_entry.delete(0,END)

    Label(reg_screen, text = "User Added.", fg = "green", font = ("Times", 11)).pack()

main_dash()