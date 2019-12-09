import unittest
from tkinter import *
import sqlite3
import tkinter as tk
ADMINNAME="Admin"
ADMINPASSWORD="Admin"

def sign_upU_As_Admin():

    SignUpRoot = Tk()
    SignUpRoot.geometry('500x600')
    SignUpRoot.title("USER REGISTRATION - ADMIN")
    
    USERNAME = StringVar()
    PASSWORD = StringVar()
    FirstName = StringVar()
    LastName = StringVar()
    
    
    def DataBase():
        
        username = USERNAME.get()
        password = PASSWORD.get()
        first = FirstName.get()
        last = LastName.get()
        UserType = "User"

        if username == "" or password == "":
            Label(SignUpRoot, text = "נדרש לפחות שם משתמש וסיסמה", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 320)
        else:
            conn = sqlite3.connect("data1.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? ", (username, ))
            if cursor.fetchone() is not None:
                Label(SignUpRoot, text = "שם משתמש תפוס", fg = 'red',width=30).place(x=200,y=320)
            else:
                Label(SignUpRoot, text = "משתמש נוצר בהצלחה", font = ("ariel", 10), fg = 'green',width=30).place(x = 200, y = 320)
                conn = sqlite3.connect("data1.db")
                cursor = conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User_Name' TEXT, 'Password' TEXT, 'First_Name' TEXT, 'Last_Name' TEXT, 'User_Type' TEXT)")
                cursor.execute("INSERT INTO  Users ('User_Name', 'Password', 'First_Name', 'Last_Name', 'User_Type') VALUES (?,?,?,?,?)", (username, password, first, last, UserType))
                conn.commit()

    label_0 = Label(SignUpRoot, text = "מנהל - רישום משתמש", width = 20, font = ("bold", 20), bg = 'gold', fg = 'white')
    label_0.place(x = 90, y = 53)

    label_1 = Label(SignUpRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
    label_1.place(x = 280, y = 130)
    USERNAME = Entry(SignUpRoot)
    USERNAME.place(x = 185, y = 130)

    label_2 = Label(SignUpRoot, text = "סיסמה", width = 20, font = ("bold", 10))
    label_2.place(x = 280, y = 180)
    PASSWORD = Entry(SignUpRoot, show = "*")
    PASSWORD.place(x = 185, y = 180)

    label_3 = Label(SignUpRoot, text = "שם פרטי", width = 20, font = ("bold", 10))
    label_3.place(x = 280, y = 230)
    FirstName = Entry(SignUpRoot)
    FirstName.place(x = 185, y = 230)

    label_4 = Label(SignUpRoot, text = "שם משפחה", width = 20, font = ("bold", 10))
    label_4.place(x = 280, y = 280)
    LastName = Entry(SignUpRoot)
    LastName.place(x = 185, y = 280)

    Button(SignUpRoot, text = "צור משתמש", width = 20, bg = 'green', fg = 'white', command = DataBase).place(x = 185, y = 380)

    button = tk.Button(SignUpRoot, text="QUIT", fg="red",command=quit)
    button.place(x=250,y=500)

    SignUpRoot.mainloop()
