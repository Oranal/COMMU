from tkinter import *
import sqlite3

    

def sign_up():
    
    SignUpRoot = Tk()
    SignUpRoot.geometry('500x600')
    SignUpRoot.title("REGISTRATION - COMMU")
    
    USERNAME = StringVar()
    PASSWORD = StringVar()
    FirstName = StringVar()
    LastName = StringVar()
    var = StringVar()

    def DataBase():
        username = USERNAME.get()
        password = PASSWORD.get()
        first = FirstName.get()
        last = LastName.get()
        UserType = var.get()

        conn = sqlite3.connect("data1.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User Name' TEXT, 'Password' TEXT, 'First Name' TEXT, 'Last Name' TEXT, 'User Type' TEXT)")
        #cursorc.execute("SELECT * FROM `Users` WHERE `User Name` = ? AND `Password` = ? AND 'First Name' = ? AND 'Last Name' = ? AND 'User Type' = ?", (USERNAME.get(), PASSWORD.get(), FirstName.get(), LastName.get(), var.get()))
        cursor.execute("INSERT INTO  Users ('User Name', 'Password', 'First Name', 'Last Name', 'User Type') VALUES (?,?,?,?,?)", (username, password, first, last, UserType))
        conn.commit()

    label_0 = Label(SignUpRoot, text = "REGISTRATION", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
    label_0.place(x = 90, y = 53)

    label_1 = Label(SignUpRoot, text = "Username", width = 20, font = ("bold", 10))
    label_1.place(x = 70, y = 130)
    entry_1 = Entry(SignUpRoot, textvar=USERNAME)
    entry_1.place(x = 240, y = 130)

    label_2 = Label(SignUpRoot, text = "Password", width = 20, font = ("bold", 10))
    label_2.place(x = 70, y = 180)
    entry_2 = Entry(SignUpRoot, textvar=PASSWORD, show = "*")
    entry_2.place(x = 240, y = 180)

    label_3 = Label(SignUpRoot, text = "First Name", width = 20, font = ("bold", 10))
    label_3.place(x = 70, y = 230)
    entry_3 = Entry(SignUpRoot, textvar=FirstName)
    entry_3.place(x = 240, y = 230)

    label_4 = Label(SignUpRoot, text = "Last Name", width = 20, font = ("bold", 10))
    label_4.place(x = 70, y = 280)
    entry_4 = Entry(SignUpRoot, textvar=LastName)
    entry_4.place(x = 240, y = 280)

    label_5 = Label(SignUpRoot, text = "User Type", width = 20, font = ("bold", 10))
    label_5.place(x = 70, y = 330)
    Radiobutton(SignUpRoot, text = "User", padx = 5, variable = var, value = "User").place(x = 235, y = 330)
    Radiobutton(SignUpRoot, text = "Parent/Guardian", padx = 20, variable = var, value = "Parent/Guardian").place(x = 290, y = 330)
    
    Button(SignUpRoot, text = "Submit", width = 20, bg = 'green', fg = 'white', command = DataBase).place(x = 200, y = 380)

    SignUpRoot.mainloop()


def start():
    StartRoot = Tk()
    StartRoot.geometry("600x400")
    StartRoot.title("Communication-Board")
    MainLabel=Label(StartRoot,text="COMMU by BRON.",bg="blue",width=20,font=("calibri",30))
    MainLabel.pack()
    Label(text="\n\n").pack()

    b1=Button(StartRoot,text="Login",width=20,font=("bold",20))
    b1.pack()
    Label(text="").pack()
    b2=Button(StartRoot,text="Register",width=20,font=("bold",20),command=sign_up)
    b2.pack()

    StartRoot.mainloop()

#start()
sign_up()