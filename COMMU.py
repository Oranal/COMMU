    import unittest
    from tkinter import *
    import sqlite3
    import tkinter as tk
    from tkinter import filedialog
    import BoardActive
    from BoardActive import CreateToolTip
    from datetime import datetime
    from datetime import date


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
    #####Settings_0

                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0, "הגדרות", r""+software_path+"Default/Tools/settings.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.01, "הוספ", r""+software_path+"Default/Tools/add.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.02, "מחיק", r""+software_path+"Default/Tools/delete.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.03, "התנתקות", r""+software_path+"Default/Tools/board log out.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.04, "שלח", r""+software_path+"Default/Tools/accept.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.05, "נקה", r""+software_path+"Default/Tools/free.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.06, "תצוגה מוגדלת", r""+software_path+"Default/Tools/bigger.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (0.07, "תצוגה מוקטנת", r""+software_path+"Default/Tools/smaller.png"))
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
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.01, "פוטבול", r""+software_path+"Default/Outdoor-Activities/american-football.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.02, "כדורגל", r""+software_path+"Default/Outdoor-Activities/soccer.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.03, "כדורסל", r""+software_path+"Default/Outdoor-Activities/basketball.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.04, "כדורעף", r""+software_path+"Default/Outdoor-Activities/volleyball.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.05, "חוף ים", r""+software_path+"Default/Outdoor-Activities/beach.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.06, "אופניים", r""+software_path+"Default/Outdoor-Activities/cycling.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.07, "דיג", r""+software_path+"Default/Outdoor-Activities/fishing.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.08, "החלקה על הקרח", r""+software_path+"Default/Outdoor-Activities/ice-skate.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.09, "עפיפון", r""+software_path+"Default/Outdoor-Activities/kite.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.10, "פיקניק", r""+software_path+"Default/Outdoor-Activities/picnic.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.11, "פינג פונג", r""+software_path+"Default/Outdoor-Activities/ping-pong.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.12, "גלגיליות", r""+software_path+"Default/Outdoor-Activities/roller-skate.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.13, "קורקינט", r""+software_path+"Default/Outdoor-Activities/scooter.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.14, "סקייטבורד", r""+software_path+"Default/Outdoor-Activities/skateboard.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.15, "בריכה", r""+software_path+"Default/Outdoor-Activities/swimming-pool.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.16, "מחנאות", r""+software_path+"Default/Outdoor-Activities/tent.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (3.17, "גשם", r""+software_path+"Default/Outdoor-Activities/umbrella.png"))
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
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.01, "אדום", r""+software_path+"Default/Colors/אדום.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.02, "כחול", r""+software_path+"Default/Colors/כחול.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.03, "צהוב", r""+software_path+"Default/Colors/צהוב.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.04, "ירוק", r""+software_path+"Default/Colors/ירוק.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.05, "כתום", r""+software_path+"Default/Colors/כתום.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.06, "סגול", r""+software_path+"Default/Colors/סגול.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.07, "ורוד", r""+software_path+"Default/Colors/ורוד.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.08, "טוקריז", r""+software_path+"Default/Colors/טורקיז.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.09, "תכלת", r""+software_path+"Default/Colors/תכלת.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.10, "בורדו", r""+software_path+"Default/Colors/בורדו.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.11, "לבן", r""+software_path+"Default/Colors/לבן.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.12, "חום", r""+software_path+"Default/Colors/חום.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.13, "אפור", r""+software_path+"Default/Colors/אפור.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (5.14, "שחור", r""+software_path+"Default/Colors/שחור.png"))
                    conn.commit()
    #
    #####Words_6
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6, "מילות קישור", r""+software_path+"Default/Words/מילות קישור.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.01, "אנחנו", r""+software_path+"Default/Words/אנחנו.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.02, "אני", r""+software_path+"Default/Words/אני.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.03, "את", r""+software_path+"Default/Words/את.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.04, "אתה", r""+software_path+"Default/Words/אתה.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.05, "די", r""+software_path+"Default/Words/די.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.06, "הוא", r""+software_path+"Default/Words/הוא.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.07, "היא", r""+software_path+"Default/Words/היא.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.08, "הם", r""+software_path+"Default/Words/הם.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.09, "הן", r""+software_path+"Default/Words/הן.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.10, "כן", r""+software_path+"Default/Words/כן.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.11, "לא", r""+software_path+"Default/Words/לא.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.12, "לה", r""+software_path+"Default/Words/לה.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.13, "להם", r""+software_path+"Default/Words/להם.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.14, "להן", r""+software_path+"Default/Words/להן.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.15, "לו", r""+software_path+"Default/Words/לו.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.16, "לי", r""+software_path+"Default/Words/לי.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.17, "צריך", r""+software_path+"Default/Words/צריך.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.18, "רוצה", r""+software_path+"Default/Words/רוצה.png"))
                    conn.commit()
                    cursor.execute("INSERT INTO  "  + ADMINNAME +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (6.19, "ללכת", r""+software_path+"Default/Words/ללכת.png"))
                    conn.commit()
    #

            conn = sqlite3.connect("Accounts.db")
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User_Name' TEXT, 'Password' TEXT, 'First_Name' TEXT, 'Last_Name' TEXT, 'User_Type' TEXT, 'Connect_To' TEXT)")
            cursor.execute("SELECT * FROM 'Users' WHERE `User_Name` = " + "'" + ADMINNAME + "'" + " AND `Password` = " + "'" + ADMINPASSWORD + "'")
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO  'Users' ('User_Name', 'Password', 'First_Name', 'Last_Name', 'User_Type') VALUES (?,?,?,?,?)", (ADMINNAME, ADMINPASSWORD, "Administrator","Administrator","Admin"))
                conn.commit()
                Board_Data()
            conn = sqlite3.connect("Reports.db")
            cursor = conn.cursor()
            

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
                        UserType=cursor.fetchone()
                        print(UserType)
                        if UserType is not None:
                            if UserType[4]=="User":
                                SignInRoot.destroy()
                                BoardActive.Board_Use(UserType[5], 20)
                            elif UserType[4]=="Parent/Gaurdian":
                                SignInRoot.destroy()
                                ParentWindow(UserType)
                                # BoardActive.Board_Edit(username) 
                        else:
                            Label(SignInRoot, text = "שם משתמש או סיסמה שגויים", fg = 'red',width=30).place(x=200,y=220)
                

                label_0 = Label(SignInRoot, text = "דף התחברות", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
                label_0.place(x = 90, y = 53)

                label_1 = Label(SignInRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
                label_1.place(x = 280, y = 130)
                USERNAME = Entry(SignInRoot)
                USERNAME.place(x = 155, y = 130)

                label_2 = Label(SignInRoot, text = "סיסמה", width = 20, font = ("bold", 10))
                label_2.place(x = 280, y = 180)
                PASSWORD = Entry(SignInRoot, show = "*")
                PASSWORD.place(x = 155, y = 180)

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
                    
                    username = USERNAME.get()
                    password = PASSWORD.get()
                    first = FirstName.get()
                    last = LastName.get()
                    connecuser = Connect.get()
                    UserType = "User"

                    if username == "" or password == "" or first == "" or last == "" or connecuser == "":
                        Label(SignUpRoot, text = "אנא מלא את כל הפרטים", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 370)
                    else:
                        conn = sqlite3.connect("Accounts.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? ", (username, ))
                        rowInData = cursor.fetchone()
                        if rowInData is not None:
                            Label(SignUpRoot, text = "שם משתמש תפוס", fg = 'red',width=30).place(x=200,y=370)
                        else:

                            cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? AND `User_Type` = 'Parent/Gaurdian'", (connecuser, ))
                            rowInData = cursor.fetchone()
                            if rowInData is not None:

                                Label(SignUpRoot, text = "משתמש נוצר בהצלחה", font = ("ariel", 10), fg = 'green',width=30).place(x = 200, y = 370)
                                conn = sqlite3.connect("Accounts.db")
                                cursor = conn.cursor()
                                cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User_Name' TEXT, 'Password' TEXT, 'First_Name' TEXT, 'Last_Name' TEXT, 'User_Type' TEXT, Connect_To TEXT)")
                                cursor.execute("INSERT INTO  Users ('User_Name', 'Password', 'First_Name', 'Last_Name', 'User_Type', 'Connect_To') VALUES (?,?,?,?,?,?)", (username, password, first, last, UserType, connecuser))
                                conn.commit()
                            else:
                                Label(SignUpRoot, text = "משתמש אחראי לא קיים", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 370)

                            # for i in admin_data:
                                # print (i)
                            # cursor.execute("INSERT INTO  " + "'" + username + "'" + " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (admin_data[0][0], admin_data[0][1], admin_data[0][2]))
                            # cursor.execute("SELECT * FROM 'Users' WHERE `User_Name` = " + "'" + ADMINNAME + "'" + " AND `Password` = " + "'" + ADMINPASSWORD + "'")
                            # if cursor.fetchone() is None:
                            #     print("yes")

                label_0 = Label(SignUpRoot, text = "רישום משתמש", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
                label_0.place(x = 90, y = 53)

                label_1 = Label(SignUpRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
                label_1.place(x = 280, y = 130)
                USERNAME = Entry(SignUpRoot)
                USERNAME.place(x = 155, y = 130)

                label_2 = Label(SignUpRoot, text = "סיסמה", width = 20, font = ("bold", 10))
                label_2.place(x = 280, y = 180)
                PASSWORD = Entry(SignUpRoot, show = "*")
                PASSWORD.place(x = 155, y = 180)

                label_3 = Label(SignUpRoot, text = "שם פרטי", width = 20, font = ("bold", 10))
                label_3.place(x = 280, y = 230)
                FirstName = Entry(SignUpRoot)
                FirstName.place(x = 155, y = 230)

                label_4 = Label(SignUpRoot, text = "שם משפחה", width = 20, font = ("bold", 10))
                label_4.place(x = 280, y = 280)
                LastName = Entry(SignUpRoot)
                LastName.place(x = 155, y = 280)

                label_5 = Label(SignUpRoot, text = "משתמש אחראי", width = 20, font = ("bold", 10))
                label_5.place(x = 280, y = 330)
                Connect = Entry(SignUpRoot)
                Connect.place(x = 155, y = 330)

                Button(SignUpRoot, text = "הירשם", width = 20, bg = 'green', fg = 'white', command = DataBase).place(x = 185, y = 400)

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

                            conn = sqlite3.connect("Boards.db")
                            cursor = conn.cursor()
                            cursor.execute("CREATE TABLE IF NOT EXISTS " + "'" + username + "'" + " ('Serial_number' FLOAT, 'Description' TEXT, 'Image_location' TEXT)")
                            if cursor.fetchone() is None:
                                for i in admin_data:
                                    cursor.execute("INSERT INTO  "  + username +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (i[0], i[1], i[2]))
                                    conn.commit()
                            conn = sqlite3.connect("Reports.db")
                            cursor = conn.cursor()
                            cursor.execute("CREATE TABLE IF NOT EXISTS " + "'" + username + "'" + " ('Date' TEXT, 'Day' INTEGER, 'Activity' TEXT)")

                label_0 = Label(SignUpRoot, text = "רישום הורה", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
                label_0.place(x = 90, y = 53)

                label_1 = Label(SignUpRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
                label_1.place(x = 280, y = 130)
                USERNAME = Entry(SignUpRoot)
                USERNAME.place(x = 155, y = 130)

                label_2 = Label(SignUpRoot, text = "סיסמה", width = 20, font = ("bold", 10))
                label_2.place(x = 280, y = 180)
                PASSWORD = Entry(SignUpRoot, show = "*")
                PASSWORD.place(x = 155, y = 180)

                label_3 = Label(SignUpRoot, text = "שם פרטי", width = 20, font = ("bold", 10))
                label_3.place(x = 280, y = 230)
                FirstName = Entry(SignUpRoot)
                FirstName.place(x = 155, y = 230)

                label_4 = Label(SignUpRoot, text = "שם משפחה", width = 20, font = ("bold", 10))
                label_4.place(x = 280, y = 280)
                LastName = Entry(SignUpRoot)
                LastName.place(x = 155, y = 280)

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

        
        def ParentWindow(parent_info):

            def ParentBoard():
        
                ParentRoot.destroy()
                BoardActive.Board_Edit(parent_info[0])

            def RemoveUser():
                
                def RemoveUserParentWindow():
                    RemoveRoot.destroy()
                    ParentWindow(parent_info)

                ParentRoot.destroy()

                RemoveRoot = Tk()
                RemoveRoot.geometry('500x400')
                RemoveRoot.title("REMOVE USER")

                USERNAME = StringVar()

                def DeleteUser():

                    username=parent_info[0]

                    conn = sqlite3.connect("Accounts.db")
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM `Users` WHERE `Connect_To` = ? ", (username, ))
                    user_to_delete = cursor.fetchone()
                    if user_to_delete is None:
                        Label(RemoveRoot, text = "לא קיים שם משתמש", fg = 'red',width=30).place(x=120,y=250)
                    else:
                        Label(RemoveRoot, text = "משתמש נמחק בהצלחה", font = ("ariel", 10), fg = 'green',width=30).place(x = 120, y = 250)
                        conn = sqlite3.connect("Accounts.db")
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM Users WHERE User_Name = ?", (user_to_delete[0], ))
                        conn.commit()
                        RemoveUserParentWindow()
                

                username=parent_info[0]

                conn = sqlite3.connect("Accounts.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM `Users` WHERE `Connect_To` = ? ", (username, ))
                user_to_delete = cursor.fetchone()
                if user_to_delete is None:
                    Label(RemoveRoot, text ="לא קיים משתמש מקושר",font = ('Ariel',12)).place(x=150,y=150)
                    # Button(RemoveRoot, text = "מחק משתמש", width = 20, bg = 'red', fg = 'white', command = DeleteUser).place(x = 150, y = 200)
                    Button(RemoveRoot, text = "אישור", width = 20, bg = 'gray', fg = 'white', command = RemoveUserParentWindow).place(x = 150, y = 290)
                else:
                    Label(RemoveRoot, text ="?האם אתה בטוח שברצונך למחוק את המשתמש המקושר אלייך").place(x=85,y=150)
                    Button(RemoveRoot, text = "מחק משתמש", width = 20, bg = 'red', fg = 'white', command = DeleteUser).place(x = 150, y = 200)
                    Button(RemoveRoot, text = "ביטול", width = 20, bg = 'gray', fg = 'white', command = RemoveUserParentWindow).place(x = 150, y = 290)

                # Label(RemoveRoot, text ="?האם אתה בטוח שברצונך למחוק את המשתמש המקושר אלייך").place(x=85,y=150)
                # Button(RemoveRoot, text = "מחק משתמש", width = 20, bg = 'red', fg = 'white', command = DeleteUser).place(x = 150, y = 200)
                # Button(RemoveRoot, text = "ביטול", width = 20, bg = 'gray', fg = 'white', command = RemoveUserParentWindow).place(x = 150, y = 290)

            def report_display():
                
                ParentRoot.destroy()

                def BackFromRep():

                    WeekRoot.destroy()
                    ParentWindow(parent_info)

                def ShowForDay(day_num):

                    dayActivity = []

                    conn = sqlite3.connect("Reports.db")
                    cursor = conn.cursor()
                    cursor.execute("SELECT * FROM " + parent_info[0] + " WHERE Day = ? ", (day_num, ))
                    dayrow = cursor.fetchall()
                    for specRow in dayrow:
                        dayActivity.append(specRow[2])
                    if dayActivity == [] :
                        Label(WeekRoot, text = "יום ריק", fg = 'red').place(x=440,y=70)
                        WeekRoot.update()
                    else:
                        ShowDayRoot = Tk()
                        Label(ShowDayRoot, text = dayrow[0][0], bg = "blue", fg = "white").grid()
                        for i in dayActivity:
                            Label(ShowDayRoot, text = i).grid()
                        Label(WeekRoot, text = "                ", fg = 'red').place(x=440,y=70)
                        WeekRoot.update()
                        ShowDayRoot.mainloop()

                WeekRoot = Tk()
                WeekRoot.geometry('937x200')
                WeekRoot.title("Weekly Report")
                Button(WeekRoot, text = "יום שבת", font = ('Ariel',20), command = lambda : ShowForDay(7)).grid(row = 0, column = 0)
                Button(WeekRoot, text = "יום שישי", font = ('Ariel',20), command = lambda : ShowForDay(6)).grid(row = 0, column = 1)
                Button(WeekRoot, text = "יום חמישי", font = ('Ariel',20), command = lambda : ShowForDay(5)).grid(row = 0, column = 2)
                Button(WeekRoot, text = "יום רביעי", font = ('Ariel',20), command = lambda : ShowForDay(4)).grid(row = 0, column = 3)
                Button(WeekRoot, text = "יום שלישי", font = ('Ariel',20), command = lambda : ShowForDay(3)).grid(row = 0, column = 4)
                Button(WeekRoot, text = "יום שני", font = ('Ariel',20), command = lambda : ShowForDay(2)).grid(row = 0, column = 5)
                Button(WeekRoot, text = "יום ראשון", font = ('Ariel',20), command = lambda : ShowForDay(1)).grid(row = 0, column = 6)
                
                Button(WeekRoot, text = "חזור", font = ('Ariel',20), command = BackFromRep).place(x=430,y=100)

                WeekRoot.mainloop()

            ParentRoot = Tk()
            ParentRoot.geometry("600x400")
            ParentRoot.title(parent_info[2]+" "+ parent_info[3])
            MainLabel=Label(ParentRoot,text="משתמש אחראי",bg="blue",width=15,font=("calibri",30))
            MainLabel.pack()
            
            b1=Button(ParentRoot,text="הסר משתמש",width=14,font=("bold",20),command=RemoveUser).place(x=320,y=200)
            b2=Button(ParentRoot,text="הצג דוח",width=14,font=("bold",20),command=report_display).place(x=0,y=200)
            b3=Button(ParentRoot,text="כניסה ללוח",width=20,font=("bold",20),command=ParentBoard).place(x=100,y=100)

            quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

            home_image = PhotoImage(file = r""+software_path+"Default/Tools/home.png")
            quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

            def ParentHome():
                    
                ParentRoot.destroy()
                start()

            Home = Button(ParentRoot, image = home_image,command=ParentHome)
            Home.place(x=110,y=300)
            CreateToolTip(Home, "התנתקות וחזרה למסך הראשי")

            Quit = Button(ParentRoot, image = quit_image,command=quit)
            Quit.place(x=20,y=300)
            CreateToolTip(Quit, "יציאה")

            ParentRoot.mainloop()



        def AdminWindow():

            def AdminBoard():

                AdminRoot.destroy()
                BoardActive.Board_Edit(ADMINNAME)

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
                            conn = sqlite3.connect("Boards.db")
                            cursor = conn.cursor()
                            cursor.execute("DROP TABLE " + username)
                            cursor = conn.cursor()

                            

                label_0 = Label(RemoveRoot, text = "הזן את שם המשתמש \n אותו תרצה למחוק", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
                label_0.place(x = 75, y = 53)

                label_1 = Label(RemoveRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
                label_1.place(x = 280, y = 150)
                USERNAME = Entry(RemoveRoot)
                USERNAME.place(x = 155, y = 150)
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
                            conn = sqlite3.connect("Boards.db")
                            cursor = conn.cursor()
                            cursor.execute("CREATE TABLE IF NOT EXISTS " + "'" + username + "'" + " ('Serial_number' FLOAT, 'Description' TEXT, 'Image_location' TEXT)")
                            if cursor.fetchone() is None:
                                for i in admin_data:
                                    cursor.execute("INSERT INTO  "  + username +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (i[0], i[1], i[2]))
                                    conn.commit()
                            conn = sqlite3.connect("Reports.db")
                            cursor = conn.cursor()
                            cursor.execute("CREATE TABLE IF NOT EXISTS " + "'" + username + "'" + " ('Date' TEXT, 'Day' INTEGER, 'Activity' TEXT)")

                label_0 = Label(SignUpRoot, text = "מנהל - רישום הורה", width = 20, font = ("bold", 20), bg = 'gold', fg = 'white')
                label_0.place(x = 90, y = 53)

                label_1 = Label(SignUpRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
                label_1.place(x = 280, y = 130)
                USERNAME = Entry(SignUpRoot)
                USERNAME.place(x = 155, y = 130)

                label_2 = Label(SignUpRoot, text = "סיסמה", width = 20, font = ("bold", 10))
                label_2.place(x = 280, y = 180)
                PASSWORD = Entry(SignUpRoot, show = "*")
                PASSWORD.place(x = 155, y = 180)

                label_3 = Label(SignUpRoot, text = "שם פרטי", width = 20, font = ("bold", 10))
                label_3.place(x = 280, y = 230)
                FirstName = Entry(SignUpRoot)
                FirstName.place(x = 155, y = 230)

                label_4 = Label(SignUpRoot, text = "שם משפחה", width = 20, font = ("bold", 10))
                label_4.place(x = 280, y = 280)
                LastName = Entry(SignUpRoot)
                LastName.place(x = 155, y = 280)

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
                    connecuser = Connect.get()

                    if username == "" or password == "" or connecuser == "":
                        Label(SignUpRoot, text = "נדרש שם משתמש, סיסמא ומשתמש אחראי", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 370)
                    else:
                        conn = sqlite3.connect("Accounts.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? ", (username, ))
                        rowInData = cursor.fetchone()
                        if rowInData is not None:
                            Label(SignUpRoot, text = "שם משתמש תפוס", fg = 'red',width=40).place(x=200,y=370)
                        else:

                            cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? AND `User_Type` = 'Parent/Gaurdian'", (connecuser, ))
                            rowInData = cursor.fetchone()
                            if rowInData is not None:

                                Label(SignUpRoot, text = "משתמש נוצר בהצלחה", font = ("ariel", 10), fg = 'green',width=30).place(x = 200, y = 370)
                                conn = sqlite3.connect("Accounts.db")
                                cursor = conn.cursor()
                                cursor.execute("CREATE TABLE IF NOT EXISTS 'Users' ('User_Name' TEXT, 'Password' TEXT, 'First_Name' TEXT, 'Last_Name' TEXT, 'User_Type' TEXT, Connect_To TEXT)")
                                cursor.execute("INSERT INTO  Users ('User_Name', 'Password', 'First_Name', 'Last_Name', 'User_Type', 'Connect_To') VALUES (?,?,?,?,?,?)", (username, password, first, last, UserType, connecuser))
                                conn.commit()
                            else:
                                Label(SignUpRoot, text = "משתמש אחראי לא קיים", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 370)

                label_0 = Label(SignUpRoot, text = "מנהל - רישום משתמש", width = 20, font = ("bold", 20), bg = 'gold', fg = 'white')
                label_0.place(x = 90, y = 53)

                label_1 = Label(SignUpRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
                label_1.place(x = 280, y = 130)
                USERNAME = Entry(SignUpRoot)
                USERNAME.place(x = 155, y = 130)

                label_2 = Label(SignUpRoot, text = "סיסמה", width = 20, font = ("bold", 10))
                label_2.place(x = 280, y = 180)
                PASSWORD = Entry(SignUpRoot, show = "*")
                PASSWORD.place(x = 155, y = 180)

                label_3 = Label(SignUpRoot, text = "שם פרטי", width = 20, font = ("bold", 10))
                label_3.place(x = 280, y = 230)
                FirstName = Entry(SignUpRoot)
                FirstName.place(x = 155, y = 230)

                label_4 = Label(SignUpRoot, text = "שם משפחה", width = 20, font = ("bold", 10))
                label_4.place(x = 280, y = 280)
                LastName = Entry(SignUpRoot)
                LastName.place(x = 155, y = 280)

                label_5 = Label(SignUpRoot, text = "משתמש אחראי", width = 20, font = ("bold", 10))
                label_5.place(x = 280, y = 330)
                Connect = Entry(SignUpRoot)
                Connect.place(x = 155, y = 330)

                Button(SignUpRoot, text = "צור משתמש", width = 20, bg = 'green', fg = 'white', command = DataBase).place(x = 185, y = 400)

                admin_image = PhotoImage(file = r""+software_path+"Default/Tools/admin.png")
                quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

                Admin = Button(SignUpRoot, image = admin_image,command=sign_upU_As_AdminAdminWindow)
                Admin.grid()
                CreateToolTip(Admin, "איזור מנהל")
                Quit = Button(SignUpRoot, image = quit_image,command=quit)
                Quit.grid()
                CreateToolTip(Quit, "יציאה")

                SignUpRoot.mainloop()

            def report():

                def reportAdminWindow():
                    ReportRoot.destroy()
                    AdminWindow()
                
                AdminRoot.destroy()

                ReportRoot = Tk()
                ReportRoot.geometry('500x400')
                ReportRoot.title("USER REPORT - ADMIN")

                USERNAME = StringVar()

                def report_display():
        
                    def BackFromRep():

                        WeekRoot.destroy()
                        AdminWindow()

                    def ShowForDay(day_num):

                        dayActivity = []

                        conn = sqlite3.connect("Reports.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM " + row[5] + " WHERE Day = ? ", (day_num, ))
                        dayrow = cursor.fetchall()
                        for specRow in dayrow:
                            dayActivity.append(specRow[2])
                        if dayActivity == [] :
                            Label(WeekRoot, text = "יום ריק", fg = 'red').place(x=440,y=70)
                            WeekRoot.update()
                        else:
                            ShowDayRoot = Tk()
                            Label(ShowDayRoot, text = dayrow[0][0], bg = "blue", fg = "white").grid()
                            for i in dayActivity:
                                Label(ShowDayRoot, text = i).grid()
                            Label(WeekRoot, text = "                ", fg = 'red').place(x=440,y=70)
                            WeekRoot.update()
                            ShowDayRoot.mainloop()

                    username = USERNAME.get()
                    if username == "" :
                        Label(ReportRoot, text = "לא הוזן שם משתמש", font = ("ariel", 10), fg = 'red',width=30).place(x = 200, y = 200)
                    else:
                        conn = sqlite3.connect("Accounts.db")
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM `Users` WHERE `User_Name` = ? ", (username, ))
                        row = cursor.fetchone()
                        if row is None or row[4] != "User":
                            Label(ReportRoot, text = "לא קיים שם משתמש", fg = 'red',width=30).place(x=200,y=200)
                        else:
        

                            ReportRoot.destroy()

                            WeekRoot = Tk()
                            WeekRoot.geometry('937x200')
                            WeekRoot.title("Weekly Report")
                            Button(WeekRoot, text = "יום שבת", font = ('Ariel',20), command = lambda : ShowForDay(7)).grid(row = 0, column = 0)
                            Button(WeekRoot, text = "יום שישי", font = ('Ariel',20), command = lambda : ShowForDay(6)).grid(row = 0, column = 1)
                            Button(WeekRoot, text = "יום חמישי", font = ('Ariel',20), command = lambda : ShowForDay(5)).grid(row = 0, column = 2)
                            Button(WeekRoot, text = "יום רביעי", font = ('Ariel',20), command = lambda : ShowForDay(4)).grid(row = 0, column = 3)
                            Button(WeekRoot, text = "יום שלישי", font = ('Ariel',20), command = lambda : ShowForDay(3)).grid(row = 0, column = 4)
                            Button(WeekRoot, text = "יום שני", font = ('Ariel',20), command = lambda : ShowForDay(2)).grid(row = 0, column = 5)
                            Button(WeekRoot, text = "יום ראשון", font = ('Ariel',20), command = lambda : ShowForDay(1)).grid(row = 0, column = 6)
                            
                            Button(WeekRoot, text = "חזור", font = ('Ariel',20), command = BackFromRep).place(x=430,y=100)

                            WeekRoot.mainloop()

                label_0 = Label(ReportRoot, text = "הזן את שם המשתמש \n עליו תרצה להציג דוח", width = 20, font = ("bold", 20), bg = 'blue', fg = 'white')
                label_0.place(x = 75, y = 53)

                label_1 = Label(ReportRoot, text = "שם משתמש", width = 20, font = ("bold", 10))
                label_1.place(x = 280, y = 150)
                USERNAME = Entry(ReportRoot)
                USERNAME.place(x = 155, y = 150)
                Button(ReportRoot, text = "הצג דוח", width = 20, bg = 'red', fg = 'white', command = report_display).place(x = 200, y = 280)

                admin_image = PhotoImage(file = r""+software_path+"Default/Tools/admin.png")
                quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

                Admin = Button(ReportRoot, image = admin_image,command=reportAdminWindow)
                Admin.grid()
                CreateToolTip(Admin, "איזור מנהל")
                Quit = Button(ReportRoot, image = quit_image,command=quit)
                Quit.grid()
                CreateToolTip(Quit, "יציאה")

                ReportRoot.mainloop()



                
    #########AdminPage

            AdminRoot = Tk()
            AdminRoot.geometry("600x400")
            AdminRoot.title("Administrator")
            MainLabel=Label(AdminRoot,text="ADMIN SECTION",bg="gold",width=20,font=("calibri",30))
            MainLabel.pack()


            b1=Button(AdminRoot,text="הסר משתמש",width=14,font=("bold",20),command=RemoveUser, bg = "coral1").place(x=330,y=100)
            b2=Button(AdminRoot,text="צור הורה",width=14,font=("bold",20),command=sign_upP_As_Admin).place(x=0,y=200)
            b3=Button(AdminRoot,text="צור משתמש",width=14,font=("bold",20),command=sign_upU_As_Admin).place(x=330,y=200)
            b4=Button(AdminRoot,text="כניסה ללוח",width=14,font=("bold",20),command=AdminBoard).place(x=330,y=300)
            b5=Button(AdminRoot,text="הצג דוח",width=14,font=("bold",20),command=report).place(x=0,y=100)

            home_image = PhotoImage(file = r""+software_path+"Default/Tools/home.png")
            quit_image = PhotoImage(file = r""+software_path+"Default/Tools/quit.png")

            def AdminHome():
                    
                AdminRoot.destroy()
                start()

            Home = Button(AdminRoot, image = home_image,command=AdminHome)
            Home.place(x=110,y=300)
            CreateToolTip(Home, "התנתקות וחזרה למסך הראשי")

            Quit = Button(AdminRoot, image = quit_image,command=quit)
            Quit.place(x=20,y=300)
            CreateToolTip(Quit, "יציאה")

            AdminRoot.mainloop()



        
        OpenData()
        Main_Window()

    start()
