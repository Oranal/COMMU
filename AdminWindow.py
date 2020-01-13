#
    def AdminWindow():

        def AdminBoard():

            AdminRoot.destroy()
            test.Board_Edit(ADMINNAME)

        def RemoveUser():
        
            def RemoveUserAdminWindow():
                RemoveRoot.destroy()
                AdminWindow()

            AdminRoot.destroy()

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
                    conn = sqlite3.connect("Accounts.db")
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? ", (username, ))
                    if cursor.fetchone() is None:
                        Label(RemoveRoot, text = "לא קיים שם משתמש", fg = 'red',width=30).place(x=200,y=200)
                    else:
                        Label(RemoveRoot, text = "משתמש נמחק בהצלחה", font = ("ariel", 10), fg = 'green',width=30).place(x = 200, y = 200)
                        conn = sqlite3.connect("Accounts.db")
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

            admin_image = PhotoImage(file = r""+software_path+"Default/Tools/admin.png")
            quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

            Admin = Button(RemoveRoot, image = admin_image,command=RemoveUserAdminWindow)
            Admin.grid()
            CreateToolTip(Admin, "איזור מנהל")
            Quit = Button(RemoveRoot, image = quit_image,command=quit)
            Quit.grid()
            CreateToolTip(Quit, "יציאה")

            RemoveRoot.mainloop()

        def sign_upP_As_Admin():

            def sign_upP_As_AdminAdminWindow():

                SignUpRoot.destroy()
                AdminWindow()

            AdminRoot.destroy()

            SignUpRoot = Tk()
            SignUpRoot.geometry('500x600')
            SignUpRoot.title("PARENT REGISTRATION - ADMIN")
            
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

                if username == "" or password == "":
                    Label(SignUpRoot, text = "נדרש לפחות שם משתמש וסיסמה", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 320)
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

            label_0 = Label(SignUpRoot, text = "מנהל - רישום הורה", width = 20, font = ("bold", 20), bg = 'gold', fg = 'white')
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

            Button(SignUpRoot, text = "צור הורה", width = 20, bg = 'green', fg = 'white', command = DataBase).place(x = 185, y = 380)

            admin_image = PhotoImage(file = r""+software_path+"Default/Tools/admin.png")
            quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

            Admin = Button(SignUpRoot, image = admin_image,command=sign_upP_As_AdminAdminWindow)
            Admin.grid()
            CreateToolTip(Admin, "איזור מנהל")
            Quit = Button(SignUpRoot, image = quit_image,command=quit)
            Quit.grid()
            CreateToolTip(Quit, "יציאה")

            SignUpRoot.mainloop()
        
        def sign_upU_As_Admin():

            def sign_upU_As_AdminAdminWindow():
    
                SignUpRoot.destroy()
                AdminWindow()

            AdminRoot.destroy()

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

            admin_image = PhotoImage(file = r""+software_path+"Default/Tools/admin.png")
            quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

            Admin = Button(SignUpRoot, image = admin_image,command=sign_upU_As_AdminAdminWindow)
            Admin.grid()
            CreateToolTip(Admin, "איזור מנהל")
            Quit = Button(SignUpRoot, image = quit_image,command=quit)
            Quit.grid()
            CreateToolTip(Quit, "יציאה")

            SignUpRoot.mainloop()
#########AdminPage

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
        b4=Button(AdminRoot,text="כניסה ללוח",width=14,font=("bold",20),command=AdminBoard).place(x=330,y=300)

        quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

        Quit = Button(AdminRoot, image = quit_image,command=quit)
        Quit.place(x=20,y=300)
        CreateToolTip(Quit, "יציאה")

        AdminRoot.mainloop()
#
