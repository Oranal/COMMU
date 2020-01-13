import unittest
from tkinter import *
import sqlite3
import tkinter as tk
from tkinter import filedialog
import Board
from Board import CreateToolTip


ADMINNAME="Admin"
ADMINPASSWORD="Admin"
software_path = ""


def start():

    def OpenData():

        def Board_Data():

            conn = sqlite3.connect("Boards.db")
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS " + "'" + ADMINNAME + "'" + " ('Serial_number' FLOAT, 'Description' TEXT, 'Image_location' TEXT)")
            if cursor.fetchone() is None:
                global software_path
                while software_path[-8:]!="COMMU.py":
                    software_path = filedialog.askopenfilename(initialdir=r"C:\Desktop\Com", title = "בחר קובץ התקנה", filetypes = (("installation", "*COMMU.py"), ))
                software_path=software_path[:-8]
#####Settings_1

                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0, "הגדרות", r""+software_path+"Default/Tools/settings.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.01, "הוספ", r""+software_path+"Default/Tools/add.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.02, "מחיק", r""+software_path+"Default/Tools/delete.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.03, "התנתקות", r""+software_path+"Default/Tools/board log out.png"))
                conn.commit()
#
#####Emotions_1
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1, "רגשות", r""+software_path+"Default/Emotions/emotions.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.01, "עצבני", r""+software_path+"Default/Emotions/angry.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.02, "כועס", r""+software_path+"Default/Emotions/angry1.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.03, "משועמם", r""+software_path+"Default/Emotions/bored.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.04, "עצוב", r""+software_path+"Default/Emotions/crying.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.05, "בוכה", r""+software_path+"Default/Emotions/crying1.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.06, "חמוד", r""+software_path+"Default/Emotions/cute.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.07, "נבוך", r""+software_path+"Default/Emotions/embarrassed.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.08, "שמח", r""+software_path+"Default/Emotions/happy.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.09, "צוחק", r""+software_path+"Default/Emotions/happy1.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.10, "מאושר", r""+software_path+"Default/Emotions/happy2.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.11, "מחייך", r""+software_path+"Default/Emotions/happy3.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.12, "מאוהב", r""+software_path+"Default/Emotions/in-love.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.13, "נשיקה", r""+software_path+"Default/Emotions/kiss.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.14, "מתפקע", r""+software_path+"Default/Emotions/laughing.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.15, "מדוכדך", r""+software_path+"Default/Emotions/sad.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.16, "רוגז", r""+software_path+"Default/Emotions/sad1.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.17, "חולה", r""+software_path+"Default/Emotions/sick.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.18, "ישנוני", r""+software_path+"Default/Emotions/sleepy.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.19, "שובב", r""+software_path+"Default/Emotions/tongue.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (1.20, "קורץ", r""+software_path+"Default/Emotions/wink.png"))
                conn.commit()
#
#####Food_2
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2, "אוכל", r""+software_path+"Default/Food/food.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.01, "תפוח", r""+software_path+"Default/Food/apple.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.02, "בננות", r""+software_path+"Default/Food/bananas.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.03, "גזר", r""+software_path+"Default/Food/carrot.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.04, "דובדבן", r""+software_path+"Default/Food/cherry.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.05, "שוק עוף", r""+software_path+"Default/Food/chicken-leg.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.06, "שוקולד", r""+software_path+"Default/Food/chocolate.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.07, "עוגיה", r""+software_path+"Default/Food/cookie.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.08, "תירס", r""+software_path+"Default/Food/corn.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.09, "קרואסון", r""+software_path+"Default/Food/croissant.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.10, "קאפקייק", r""+software_path+"Default/Food/cupcake.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.11, "דונאט", r""+software_path+"Default/Food/donut.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.12, "צ'יפס", r""+software_path+"Default/Food/french-fries.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.13, "ביצת עין", r""+software_path+"Default/Food/fried-egg.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.14, "ענבים", r""+software_path+"Default/Food/grapes.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.15, "המבורגר", r""+software_path+"Default/Food/hamburger.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.16, "נקניקיה בלחמניה", r""+software_path+"Default/Food/hot-dog.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.17, "גלידה", r""+software_path+"Default/Food/ice-cream.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.18, "קטשופ", r""+software_path+"Default/Food/ketchup.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.19, "מילקשייק", r""+software_path+"Default/Food/milkshake.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.20, "תפוז", r""+software_path+"Default/Food/orange.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.21, "אפרסק", r""+software_path+"Default/Food/peach.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.22, "אגס", r""+software_path+"Default/Food/pear.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.23, "פיצה", r""+software_path+"Default/Food/pizza.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.24, "ארטיק", r""+software_path+"Default/Food/popsicle.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.25, "משקה מוגז", r""+software_path+"Default/Food/soda.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.26, "תות", r""+software_path+"Default/Food/strawberry.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.27, "צנים", r""+software_path+"Default/Food/toast.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (2.28, "אבטיח", r""+software_path+"Default/Food/watermelon.png"))
                conn.commit()
#
#####Outdoor_Activities_3                
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3, "פעילויות חוץ", r""+software_path+"Default/Outdoor-Activities/outdoor-activities.png"))
                conn.commit()
#
#####Home_4                
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4, "פעילויות בית", r""+software_path+"Default/Home/home.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.01, "מסרק", r""+software_path+"Default/Home/comb.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.02, "מחשב", r""+software_path+"Default/Home/computer.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.03, "ברווז אמבט", r""+software_path+"Default/Home/duck.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.04, "מנורה", r""+software_path+"Default/Home/light-bulb.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.05, "סמארטפון", r""+software_path+"Default/Home/mobile-phone.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.06, "מקלחת", r""+software_path+"Default/Home/shower.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.07, "קירור", r""+software_path+"Default/Home/temperature.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.08, "חימום", r""+software_path+"Default/Home/temperature-hot.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.09, "אסלה", r""+software_path+"Default/Home/toilet.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.10, "לצחצח שיניים", r""+software_path+"Default/Home/toothbrush.png"))
                conn.commit()
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (4.11, "חלון", r""+software_path+"Default/Home/window.png"))
                conn.commit()
#
#####Colors_5                
                cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5, "צבעים", r""+software_path+"Default/Colors/colors.png"))
                conn.commit()
#
                
        conn = sqlite3.connect("Accounts.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User_Name' TEXT, 'Password' TEXT, 'First_Name' TEXT, 'Last_Name' TEXT, 'User_Type' TEXT)")
        cursor.execute("SELECT * FROM 'Users' WHERE `User_Name` = " + "'" + ADMINNAME + "'" + " AND `Password` = " + "'" + ADMINPASSWORD + "'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO  'Users' ('User_Name', 'Password', 'First_Name', 'Last_Name', 'User_Type') VALUES (?,?,?,?,?)", (ADMINNAME, ADMINPASSWORD, "Administrator","Administrator","Admin"))
            conn.commit()
            Board_Data()

    def Main_Window():
       
        def login():

            def loginHome():

                SignInRoot.destroy()
                start()
            
            StartRoot.destroy()
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

        def sign_upU():

            def sign_upUHome():
                SignUpRoot.destroy()
                start()

            StartRoot.destroy()
            SignUpRoot = Tk()
            SignUpRoot.geometry('500x600')
            SignUpRoot.title("USER REGISTRATION - COMMU")
            
            USERNAME = StringVar()
            PASSWORD = StringVar()
            FirstName = StringVar()
            LastName = StringVar()
        
            
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


      
    OpenData()
    Main_Window()

start()
