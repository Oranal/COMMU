import unittest
from tkinter import *
import sqlite3
import tkinter as tk
ADMINNAME="Admin"
ADMINPASSWORD="Admin"

def AdminWindow():

    AdminRoot = Tk()
    AdminRoot.geometry("600x400")
    AdminRoot.title("Administrator")
    MainLabel=Label(AdminRoot,text="ADMIN SECTION",bg="gold",width=20,font=("calibri",30))
    MainLabel.pack()
    Label(text="\n\n").pack()

    b1=Button(AdminRoot,text="הסר משתמש",width=20,font=("bold",20),command=RemoveUser).place(x=140,y=100)
    Label(text="").pack()
    b2=Button(AdminRoot,text="צור הורה",width=14,font=("bold",20),command=sign_upP_As_Admin).place(x=55,y=200)
    b3=Button(AdminRoot,text="צור משתמש",width=14,font=("bold",20),command=sign_upU_As_Admin).place(x=330,y=200)

    button = tk.Button(AdminRoot, text="QUIT", fg="red",command=quit)
    button.place(x=270,y=300)


    AdminRoot.mainloop()