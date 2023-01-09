from tkinter import *
from tkinter import ttk
import tkinter as tk
from constructorClass import User, Account
import DBFunctions
import time

UID = None

def main_dash():
    
    global main_screen
    global tree
    main_screen = Tk()

    main_screen.geometry("1000x800")
    main_screen.title("OSPM 1.0")
    Label(text = "OSPM 1.0", bg = "grey", width = "300", height = "2", font = ("Times", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "30", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register User", height = "2", width = "30", command = register).pack()
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

    Button(text = "Add Account", height = "2", width = "30", command = create_account).pack()
    Label(text = "").pack()
    #Button(text="Delete Account", height = "2", width = "30", command = delete_account).pack()
    #Label(text = "").pack()
    Button(text="Update Data", height = "2", width = "30", command=fetch_accounts).pack()
    Label(text = "").pack()
    Button(text="Update Data (Encrypted)", height = "2", width = "30", command=fetch_encrypted).pack()
    #button1.pack(pady=10)

    main_screen.mainloop()

def create_account():

    if(UID == None): #if user has not logged in
        return None

    global account_screen
    account_screen = Toplevel(main_screen)
    account_screen.title("Add Account")
    account_screen.geometry("500x350")

    global acc_serName
    global acc_login
    global acc_password 
    global acc_note
    acc_serName = StringVar()
    acc_login = StringVar()
    acc_password = StringVar()
    acc_note = StringVar()
    
    Label(account_screen, text = "Please enter account details below:").pack()
    Label(account_screen, text = "").pack()
    
    Label(account_screen, text = "Service Name  ").pack()
    acc_serName_entry = Entry(account_screen, textvariable = acc_serName)
    acc_serName_entry.pack()
    
    Label(account_screen, text = "Login  ").pack()
    acc_login_entry = Entry(account_screen, textvariable = acc_login)
    acc_login_entry.pack()

    Label(account_screen, text = "Password  ").pack()
    acc_password_entry = Entry(account_screen, textvariable = acc_password)
    acc_password_entry.pack()

    Label(account_screen, text = "Note (Optional)  ").pack()
    acc_note_entry = Entry(account_screen, textvariable = acc_note)
    acc_note_entry.pack()
    
    Button(account_screen, text = "Add Account", width = 12, height = 2, command = add_account).pack()
    acc_note_entry.pack()
    acc_note_entry.pack()

    #Button(account_screen, text = "Random Password Generator", width = 12, height = 1, command = add_account).pack()



def add_account():


    #collects text field data
    serName_entry = acc_serName.get()
    login_entry = acc_login.get()
    password_entry = acc_password.get()
    note_entry = acc_note.get()

    '''
    print("1 = " + serName_entry)
    print("2 = " + login_entry)
    print("3 = " + password_entry)
    print("4 = " + note_entry)
    '''

    if(None in (serName_entry, login_entry, password_entry)):
        Label(account_screen, text = "Error, incorrect entry", fg = "red", font = ("Times", 11)).pack()
        account_screen.update()
        time.sleep(2)
        
        #account_screen.destroy()

    else:
        #constructs an account object
        account = Account(DBFunctions.iterateAccID(UID), UID, serName_entry, login_entry, password_entry.encode(), note_entry, DBFunctions.getKey(UID))
        #inserts object into database
        DBFunctions.insertAccount(account)
        Label(account_screen, text = "Account Added", fg = "green", font = ("Times", 11)).pack()

def fetch_accounts():

    if(UID == None): #if user has not logged in
        return None

    for item in tree.get_children(): #deletes data currently being displayed
        tree.delete(item)

    accounts = DBFunctions.selectDecoded(UID)

    for account in accounts: #displayed updated data
        tree.insert("", tk.END, values=account)
    
def fetch_encrypted():

    if(UID == None): #if user has not logged in
        return None

    for item in tree.get_children(): #deletes data currently being displayed
        tree.delete(item)

    accounts = DBFunctions.selectEncoded(UID)

    for account in accounts: #displayed updated data
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
        #print("success")
        Label(login_screen, text = "Login Successful!", fg = "green", font = ("Times", 11)).pack()
        UID = DBFunctions.getID(username_entry)
        main_screen.update()
        login_screen.destroy()
    else:
        #print("fail")
        Label(login_screen, text = "Incorrect credentials", fg = "red", font = ("Times", 11)).pack()

    #login_username_entry.delete(0,END)
    #login_password_entry.delete(0,END)

def register():
    global reg_screen
    reg_screen = Toplevel(main_screen)
    reg_screen.title("Register User")
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
    Button(reg_screen, text = "Register User", width = 12, height = 1, command = register_user).pack()

def register_user():
    reg_username_in = reg_username.get()
    reg_password_in = reg_password.get()

    user = User(DBFunctions.iterateID(), reg_username_in, reg_password_in.encode())
    DBFunctions.insertUser(user)

    reg_username_entry.delete(0,END)
    reg_password_entry.delete(0,END)

    Label(reg_screen, text = "User Added.", fg = "green", font = ("Times", 11)).pack()

'''
def delete_account():

    if(UID == None): #if user has not logged in
        return None

    global del_screen
    
    del_screen = Toplevel(main_screen)
    del_screen.title("Delete Account")
    del_screen.geometry("500x200")

    global del_serName
    del_serName = StringVar()

    Label(del_screen, text = "Please enter the service name of the account you wish to delete below:").pack()
    Label(del_screen, text = "").pack()
    del_serName_entry =  Entry(del_screen, textvariable = del_serName)
    del_serName_entry.pack()

    Button(del_screen, text = "Delete Account", width = 12, height = 1, command = delete).pack()

def delete():
    
    

    serName_in = del_serName.get()
    #print(serName_in)
    deleted = DBFunctions.deleteAccount(UID,serName_in)
    #print(deleted)
    
    if(deleted == True): 
        
        Label(del_screen, text = "Account Deleted, please update accounts on main window", fg = "blue", font = ("Times", 11)).pack()
        del_screen.update()

        time.sleep(2)
        del_screen.destroy()

    else:
        Label(del_screen, text = "Account not found, please try again", fg = "red", font = ("Times", 11)).pack()
        del_screen.update()
'''



main_dash()