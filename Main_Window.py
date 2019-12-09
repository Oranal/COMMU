import unittest
from tkinter import *
import sqlite3
import tkinter as tk
ADMINNAME="Admin"
ADMINPASSWORD="Admin"

def Main_Window():

    StartRoot = Tk()
    StartRoot.geometry("600x400")
    StartRoot.configure(background = '#81DAF5')
    StartRoot.title("Communication-Board")
    MainLabel=Label(StartRoot,text="COMMU by BRON.",bg="blue",width=20,font=("calibri",30))
    MainLabel.pack()

    b1=Button(StartRoot,text="התחברות",width=20,font=("bold",20),command=login).place(x=140,y=100)
    b2=Button(StartRoot,text="הירשם כהורה",width=13,font=("bold",20),command=sign_upP).place(x=55,y=200)
    b3=Button(StartRoot,text="הירשם כמשתמש",width=13,font=("bold",20),command=sign_upU).place(x=330,y=200)

    button = tk.Button(StartRoot, text="QUIT", fg="red",command=quit)
    button.place(x=270,y=300)

    StartRoot.mainloop()