import unittest
from tkinter import *
import sqlite3
import tkinter as tk
ADMINNAME="Admin"
ADMINPASSWORD="Admin"


def RemoveUser():
   
    RemoveRoot = Tk()
    RemoveRoot.geometry('500x400')
    RemoveRoot.title("REMOVE USER - ADMIN")

    USERNAME = StringVar()

    def DeleteUser():
        username=USERNAME.get()
        if username == "" :
            Label(RemoveRoot, text = "לא הוזן שם משתמש", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 200)
        elif username==ADMINNAME:
            Label(RemoveRoot, text = "לא ניתן להסיר מנהל", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 200)
        else:
            conn = sqlite3.connect("data1.db")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? ", (username, ))
            if cursor.fetchone() is None:
                Label(RemoveRoot, text = "לא קיים שם משתמש", fg = 'red',width=30).place(x=200,y=200)
            else:
                Label(RemoveRoot, text = "משתמש נמחק בהצלחה", font = ("ariel", 10), fg = 'green',width=30).place(x = 200, y = 200)
                conn = sqlite3.connect("data1.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Users WHERE User_Name = ?", (username, ))
                conn.commit()
    label_0 = Label(RemoveRoot, text = "הזן את שם המשתמש \n אותו תרצה למחוק", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
    label_0.place(x = 75, y = 53)

    label_1 = Label(RemoveRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
    label_1.place(x = 280, y = 150)
    USERNAME = Entry(RemoveRoot)
    USERNAME.place(x = 185, y = 150)
    Button(RemoveRoot, text = "מחק משתמש", width = 20, bg = 'red', fg = 'white', command = DeleteUser).place(x = 200, y = 280)
    RemoveRoot.mainloop()
      