#open data base
import unittest
from tkinter import *
import sqlite3
import tkinter as tk
ADMINNAME="Admin"
ADMINPASSWORD="Admin"


def OpenData():

    conn = sqlite3.connect("data1.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User_Name' TEXT, 'Password' TEXT, 'First_Name' TEXT, 'Last_Name' TEXT, 'User_Type' TEXT)")
    cursor.execute("SELECT * FROM 'Users' WHERE `User_Name` = 'Admin' AND `Password` = 'Admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO  'Users' ('User_Name', 'Password', 'First_Name', 'Last_Name', 'User_Type') VALUES (?,?,?,?,?)", (ADMINNAME, ADMINPASSWORD, "Administrator","Administrator","Admin"))
        conn.commit()
 
