from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog
import sqlite3
import os
import socket
import unittest
#import COMMU


#Main_Window
def Main_Window():

#login
    def login():

#loginHome
        def loginHome():

            SignInRoot.destroy()
            start()
#      
        StartRoot.destroy()
        SignInRoot = Tk()
        SignInRoot.geometry('500x400')
        SignInRoot.title("USER REGISTRATION - COMMU")
        
        USERNAME = StringVar()
        PASSWORD = StringVar()

#DataBase
        def DataBase():
#
            username = USERNAME.get()
            password = PASSWORD.get()
            if username == "" or password == "":
                Label(SignInRoot, text = "מלא את השדות", fg = 'red',width=30).place(x=200,y=220)
            elif username == ADMINNAME and password == ADMINPASSWORD:
                SignInRoot.destroy()
                AdminWindow()
            else:
                conn = sqlite3.connect("Accounts.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? AND `Password` = ?", (username, password))
                if cursor.fetchone() is not None:
                    Label(SignInRoot, text = "התחברת בהצלחה", fg = 'green',width=30).place(x=200,y=220)
                    SignInRoot.destroy()
                    test.Board_Edit(username)
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

        home_image = PhotoImage(file = r""+software_path+"Default/Tools/home.png")
        quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

        Home = Button(SignInRoot, image = home_image,command=loginHome)
        Home.grid()
        CreateToolTip(Home, "בית")
        Quit = Button(SignInRoot, image = quit_image,command=quit)
        Quit.grid()
        CreateToolTip(Quit, "יציאה")

        SignInRoot.mainloop()

#sign_upU
    def sign_upU():

#sign_upUHome
        def sign_upUHome():
            SignUpRoot.destroy()
            start()
#
        StartRoot.destroy()
        SignUpRoot = Tk()
        SignUpRoot.geometry('500x600')
        SignUpRoot.title("USER REGISTRATION - COMMU")
        
        USERNAME = StringVar()
        PASSWORD = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
    
#DataBase           
        def DataBase():

            conn = sqlite3.connect("Boards.db")
            s = conn.cursor()
            s.execute("SELECT * FROM 'Admin'")
            admin_data=[]
            for row in s.fetchall():
                admin_data.append(list(row))
            
            username = USERNAME.get()
            password = PASSWORD.get()
            first = FirstName.get()
            last = LastName.get()
            UserType = "User"

            if username == "" or password == "" or first == "" or last == "":
                Label(SignUpRoot, text = "אנא מלא את כל הפרטים", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 320)
            else:
                conn = sqlite3.connect("Accounts.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? ", (username, ))
                if cursor.fetchone() is not None:
                    Label(SignUpRoot, text = "שם משתמש תפוס", fg = 'red',width=30).place(x=200,y=320)
                else:
                    Label(SignUpRoot, text = "משתמש נוצר בהצלחה", font = ("ariel", 10), fg = 'green',width=30).place(x = 200, y = 320)
                    
                    # for i in admin_data:
                        # print (i)
                    # cursor.execute("INSERT INTO  " + "'" + username + "'" + " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (admin_data[0][0], admin_data[0][1], admin_data[0][2]))
                    # cursor.execute("SELECT * FROM 'Users' WHERE `User_Name` = " + "'" + ADMINNAME + "'" + " AND `Password` = " + "'" + ADMINPASSWORD + "'")
                    # if cursor.fetchone() is None:
                    #     print("yes")


                    conn = sqlite3.connect("Boards.db")
                    cursor = conn.cursor()
                    cursor.execute("CREATE TABLE IF NOT EXISTS " + "'" + username + "'" + " ('Serial_number' FLOAT, 'Description' TEXT, 'Image_location' TEXT)")
                    if cursor.fetchone() is None:
                        for i in admin_data:
                            cursor.execute("INSERT INTO  "  + username +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (i[0], i[1], i[2]))
                            conn.commit()

                    conn = sqlite3.connect("Accounts.db")
                    cursor = conn.cursor()
                    cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User_Name' TEXT, 'Password' TEXT, 'First_Name' TEXT, 'Last_Name' TEXT, 'User_Type' TEXT)")
                    cursor.execute("INSERT INTO  Users ('User_Name', 'Password', 'First_Name', 'Last_Name', 'User_Type') VALUES (?,?,?,?,?)", (username, password, first, last, UserType))
                    conn.commit()
#
        label_0 = Label(SignUpRoot, text = "רישום משתמש", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
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

        Button(SignUpRoot, text = "הירשם", width = 20, bg = 'green', fg = 'white', command = DataBase).place(x = 185, y = 380)

        home_image = PhotoImage(file = r""+software_path+"Default/Tools/home.png")
        quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

        Home = Button(SignUpRoot, image = home_image,command=sign_upUHome)
        Home.grid()
        CreateToolTip(Home, "בית")
        Quit = Button(SignUpRoot, image = quit_image,command=quit)
        Quit.grid()
        CreateToolTip(Quit, "יציאה")

        SignUpRoot.mainloop()

#sign_upP
    def sign_upP():

        def sign_upPHome():
            SignUpRoot.destroy()
            start()
            
        StartRoot.destroy()
        SignUpRoot = Tk()
        SignUpRoot.geometry('500x600')
        SignUpRoot.title("PARENT REGISTRATION - COMMU")
        
        USERNAME = StringVar()
        PASSWORD = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
        
        
        def DataBase():
            
            username = USERNAME.get()
            password = PASSWORD.get()
            first = FirstName.get()
            last = LastName.get()
            UserType = "Parent/Gaurdian"

            if username == "" or password == "" or first == "" or last == "":
                Label(SignUpRoot, text = "אנא מלא את כל הפרטים", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 320)
            else:
                conn = sqlite3.connect("Accounts.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? ", (username, ))
                if cursor.fetchone() is not None:
                    Label(SignUpRoot, text = "שם משתמש תפוס", fg = 'red',width=30).place(x=200,y=320)
                else:
                    Label(SignUpRoot, text = "משתמש נוצר בהצלחה", font = ("ariel", 10), fg = 'green',width=30).place(x = 200, y = 320)
                    conn = sqlite3.connect("Accounts.db")
                    cursor = conn.cursor()
                    cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User_Name' TEXT, 'Password' TEXT, 'First_Name' TEXT, 'Last_Name' TEXT, 'User_Type' TEXT)")
                    cursor.execute("INSERT INTO  Users ('User_Name', 'Password', 'First_Name', 'Last_Name', 'User_Type') VALUES (?,?,?,?,?)", (username, password, first, last, UserType))
                    conn.commit()

        label_0 = Label(SignUpRoot, text = "רישום הורה", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
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

        Button(SignUpRoot, text = "הירשם", width = 20, bg = 'green', fg = 'white', command = DataBase).place(x = 185, y = 380)

        home_image = PhotoImage(file = r""+software_path+"Default/Tools/home.png")
        quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

        Home = Button(SignUpRoot, image = home_image,command=sign_upPHome)
        Home.grid()
        CreateToolTip(Home, "בית")
        Quit = Button(SignUpRoot, image = quit_image,command=quit)
        Quit.grid()
        CreateToolTip(Quit, "יציאה")

        SignUpRoot.mainloop()
########HomePage
    StartRoot = Tk()
    StartRoot.geometry("600x400")
    StartRoot.configure(background = '#81DAF5')
    StartRoot.title("Communication-Board")
    MainLabel=Label(StartRoot,text="COMMU by BRON.",bg="blue",width=20,font=("calibri",30))
    MainLabel.pack()
    b1=Button(StartRoot,text="התחברות",width=20,font=("bold",20),command=login).place(x=140,y=100)
    b2=Button(StartRoot,text="הירשם כהורה",width=13,font=("bold",20),command=sign_upP).place(x=55,y=200)
    b3=Button(StartRoot,text="הירשם כמשתמש",width=13,font=("bold",20),command=sign_upU).place(x=330,y=200)

    quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

    Quit = Button(StartRoot, image = quit_image, command=quit)
    Quit.place(x=270,y=300)
    CreateToolTip(Quit,"יציאה")


    StartRoot.mainloop()


