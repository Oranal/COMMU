import unittest
from tkinter import *
import sqlite3
import tkinter as tk
ADMINNAME="Admin"
ADMINPASSWORD="Admin"

def login():
        
    SignInRoot = Tk()
    SignInRoot.geometry('500x400')
    SignInRoot.title("USER REGISTRATION - COMMU")
    
    USERNAME = StringVar()
    PASSWORD = StringVar()

    def DataBase():

        username = USERNAME.get()
        password = PASSWORD.get()
        if username == "" or password == "":
            Label(SignInRoot, text = "מלא את השדות", fg = 'red',width=30).place(x=200,y=220)
        elif username == ADMINNAME and password == ADMINPASSWORD:
            Label(SignInRoot, text = "התחברת כמנהל", fg = 'red',width=30).place(x=200,y=220)
            AdminWindow()
        else:
            conn = sqlite3.connect("data1.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? AND `Password` = ?", (username, password))
            if cursor.fetchone() is not None:
                Label(SignInRoot, text = "התחברת בהצלחה", fg = 'green',width=30).place(x=200,y=220)
            else:
                Label(SignInRoot, text = "שם משתמש או סיסמה שגויים", fg = 'red',width=30).place(x=200,y=220)
    

    label_0 = Label(SignInRoot, text = "דף התחברות", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
    label_0.place(x = 90, y = 53)

    label_1 = Label(SignInRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
    label_1.place(x = 280, y = 130)
    USERNAME = Entry(SignInRoot)
    USERNAME.place(x = 185, y = 130)

    label_2 = Label(SignInRoot, text = "סיסמה", width = 20, font = ("bold", 10))
    label_2.place(x = 280, y = 180)
    PASSWORD = Entry(SignInRoot, show = "*")
    PASSWORD.place(x = 185, y = 180)

    Button(SignInRoot, text = "התחבר", width = 20, bg = 'green', fg = 'white', command = DataBase).place(x = 200, y = 280)

    button = tk.Button(SignInRoot, text="QUIT", fg="red",command=quit)
    button.place(x=250,y=320)

    SignInRoot.mainloop()
