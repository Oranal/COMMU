from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import filedialog
import sqlite3


class CreateToolTip(object):
    
    def __init__(self, widget, text = "Fuck you all"):
        self.waittime = 500
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None
        
    def enter(self, event = None):
        self.schedule()
    
    def leave(self, event = None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)
    
    def showtip(self, event = None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text = self.text, justify = 'left', background = "white", relief = 'solid', borderwidth = 1, wraplength = self.wraplength)
        label.pack(ipadx = 1)


    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()






def Board_Edit(board_of):
    
######################_TKinter Root_#######################

    BoardEditRoot = Tk()
    BoardEditRoot.geometry("1920x1080")
    BoardEditRoot.title(board_of+"'s Board - EDIT MODE")

######################_Buttons_############################

##############_Category 0_###################
    c0=Button(BoardEditRoot)
    c0_B=[]
    b0_0=Button(BoardEditRoot)
    b0_1=Button(BoardEditRoot)
    b0_2=Button(BoardEditRoot)
    c0_B.append(b0_0)
    c0_B.append(b0_1)
    c0_B.append(b0_2)
##############_Category 1_###################
    c1=Button(BoardEditRoot)
    c1_B = []
    b1_0 = Button(BoardEditRoot)
    b1_1 = Button(BoardEditRoot)
    b1_2 = Button(BoardEditRoot)
    b1_3 = Button(BoardEditRoot)
    b1_4 = Button(BoardEditRoot)
    b1_5 = Button(BoardEditRoot)
    b1_6 = Button(BoardEditRoot)
    b1_7 = Button(BoardEditRoot)
    b1_8 = Button(BoardEditRoot)
    b1_9 = Button(BoardEditRoot)
    b1_10 = Button(BoardEditRoot)
    b1_11 = Button(BoardEditRoot)
    b1_12 = Button(BoardEditRoot)
    b1_13 = Button(BoardEditRoot)
    b1_14 = Button(BoardEditRoot)
    b1_15 = Button(BoardEditRoot)
    b1_16 = Button(BoardEditRoot)
    b1_17 = Button(BoardEditRoot)
    b1_18 = Button(BoardEditRoot)
    b1_19 = Button(BoardEditRoot)
    b1_20 = Button(BoardEditRoot)
    b1_21 = Button(BoardEditRoot)
    b1_22 = Button(BoardEditRoot)
    b1_23 = Button(BoardEditRoot)
    b1_24 = Button(BoardEditRoot)
    b1_25 = Button(BoardEditRoot)
    b1_26 = Button(BoardEditRoot)
    b1_27 = Button(BoardEditRoot)
    b1_28 = Button(BoardEditRoot)
    b1_29 = Button(BoardEditRoot)
    b1_30 = Button(BoardEditRoot)
    b1_31 = Button(BoardEditRoot)
    b1_32 = Button(BoardEditRoot)
    b1_33 = Button(BoardEditRoot)
    b1_34 = Button(BoardEditRoot)
    b1_35 = Button(BoardEditRoot)
    b1_36 = Button(BoardEditRoot)
    b1_37 = Button(BoardEditRoot)
    b1_38 = Button(BoardEditRoot)
    b1_39 = Button(BoardEditRoot)
    b1_40 = Button(BoardEditRoot)
    b1_41 = Button(BoardEditRoot)
    b1_42 = Button(BoardEditRoot)
    b1_43 = Button(BoardEditRoot)
    b1_44 = Button(BoardEditRoot)
    b1_45 = Button(BoardEditRoot)
    b1_46 = Button(BoardEditRoot)
    b1_47 = Button(BoardEditRoot)

    c1_B.append(b1_0)
    c1_B.append(b1_1)
    c1_B.append(b1_2)
    c1_B.append(b1_3)
    c1_B.append(b1_4)
    c1_B.append(b1_5)
    c1_B.append(b1_6)
    c1_B.append(b1_7)
    c1_B.append(b1_8)
    c1_B.append(b1_9)
    c1_B.append(b1_10)
    c1_B.append(b1_11)
    c1_B.append(b1_12)
    c1_B.append(b1_13)
    c1_B.append(b1_14)
    c1_B.append(b1_15)
    c1_B.append(b1_16)
    c1_B.append(b1_17)
    c1_B.append(b1_18)
    c1_B.append(b1_19)
    c1_B.append(b1_20)
    c1_B.append(b1_21)
    c1_B.append(b1_22)
    c1_B.append(b1_23)
    c1_B.append(b1_24)
    c1_B.append(b1_25)
    c1_B.append(b1_26)
    c1_B.append(b1_27)
    c1_B.append(b1_28)
    c1_B.append(b1_29)
    c1_B.append(b1_30)
    c1_B.append(b1_31)
    c1_B.append(b1_32)
    c1_B.append(b1_33)
    c1_B.append(b1_34)
    c1_B.append(b1_35)
    c1_B.append(b1_36)
    c1_B.append(b1_37)
    c1_B.append(b1_38)
    c1_B.append(b1_39)
    c1_B.append(b1_40)
    c1_B.append(b1_41)
    c1_B.append(b1_42)
    c1_B.append(b1_43)
    c1_B.append(b1_44)
    c1_B.append(b1_45)
    c1_B.append(b1_46)
    c1_B.append(b1_47)


##############_Category 2_###################


    c2=Button(BoardEditRoot)
    c2_B = []
    b2_0 = Button(BoardEditRoot)
    b2_1 = Button(BoardEditRoot)
    b2_2 = Button(BoardEditRoot)
    b2_3 = Button(BoardEditRoot)
    b2_4 = Button(BoardEditRoot)
    b2_5 = Button(BoardEditRoot)
    b2_6 = Button(BoardEditRoot)
    b2_7 = Button(BoardEditRoot)
    b2_8 = Button(BoardEditRoot)
    b2_9 = Button(BoardEditRoot)
    b2_10 = Button(BoardEditRoot)
    b2_11 = Button(BoardEditRoot)
    b2_12 = Button(BoardEditRoot)
    b2_13 = Button(BoardEditRoot)
    b2_14 = Button(BoardEditRoot)
    b2_15 = Button(BoardEditRoot)
    b2_16 = Button(BoardEditRoot)
    b2_17 = Button(BoardEditRoot)
    b2_18 = Button(BoardEditRoot)
    b2_19 = Button(BoardEditRoot)
    b2_20 = Button(BoardEditRoot)
    b2_21 = Button(BoardEditRoot)
    b2_22 = Button(BoardEditRoot)
    b2_23 = Button(BoardEditRoot)
    b2_24 = Button(BoardEditRoot)
    b2_25 = Button(BoardEditRoot)
    b2_26 = Button(BoardEditRoot)
    b2_27 = Button(BoardEditRoot)
    b2_28 = Button(BoardEditRoot)
    b2_29 = Button(BoardEditRoot)
    b2_30 = Button(BoardEditRoot)
    b2_31 = Button(BoardEditRoot)
    b2_32 = Button(BoardEditRoot)
    b2_33 = Button(BoardEditRoot)
    b2_34 = Button(BoardEditRoot)
    b2_35 = Button(BoardEditRoot)
    b2_36 = Button(BoardEditRoot)
    b2_37 = Button(BoardEditRoot)
    b2_38 = Button(BoardEditRoot)
    b2_39 = Button(BoardEditRoot)
    b2_40 = Button(BoardEditRoot)
    b2_41 = Button(BoardEditRoot)
    b2_42 = Button(BoardEditRoot)
    b2_43 = Button(BoardEditRoot)
    b2_44 = Button(BoardEditRoot)
    b2_45 = Button(BoardEditRoot)
    b2_46 = Button(BoardEditRoot)
    b2_47 = Button(BoardEditRoot)

    c2_B.append(b2_0)
    c2_B.append(b2_1)
    c2_B.append(b2_2)
    c2_B.append(b2_3)
    c2_B.append(b2_4)
    c2_B.append(b2_5)
    c2_B.append(b2_6)
    c2_B.append(b2_7)
    c2_B.append(b2_8)
    c2_B.append(b2_9)
    c2_B.append(b2_10)
    c2_B.append(b2_11)
    c2_B.append(b2_12)
    c2_B.append(b2_13)
    c2_B.append(b2_14)
    c2_B.append(b2_15)
    c2_B.append(b2_16)
    c2_B.append(b2_17)
    c2_B.append(b2_18)
    c2_B.append(b2_19)
    c2_B.append(b2_20)
    c2_B.append(b2_21)
    c2_B.append(b2_22)
    c2_B.append(b2_23)
    c2_B.append(b2_24)
    c2_B.append(b2_25)
    c2_B.append(b2_26)
    c2_B.append(b2_27)
    c2_B.append(b2_28)
    c2_B.append(b2_29)
    c2_B.append(b2_30)
    c2_B.append(b2_31)
    c2_B.append(b2_32)
    c2_B.append(b2_33)
    c2_B.append(b2_34)
    c2_B.append(b2_35)
    c2_B.append(b2_36)
    c2_B.append(b2_37)
    c2_B.append(b2_38)
    c2_B.append(b2_39)
    c2_B.append(b2_40)
    c2_B.append(b2_41)
    c2_B.append(b2_42)
    c2_B.append(b2_43)
    c2_B.append(b2_44)
    c2_B.append(b2_45)
    c2_B.append(b2_46)
    c2_B.append(b2_47)


##############_Category 3_###################


    c3=Button(BoardEditRoot)
    c3_B = []
    b3_0 = Button(BoardEditRoot)
    b3_1 = Button(BoardEditRoot)
    b3_2 = Button(BoardEditRoot)
    b3_3 = Button(BoardEditRoot)
    b3_4 = Button(BoardEditRoot)
    b3_5 = Button(BoardEditRoot)
    b3_6 = Button(BoardEditRoot)
    b3_7 = Button(BoardEditRoot)
    b3_8 = Button(BoardEditRoot)
    b3_9 = Button(BoardEditRoot)
    b3_10 = Button(BoardEditRoot)
    b3_11 = Button(BoardEditRoot)
    b3_12 = Button(BoardEditRoot)
    b3_13 = Button(BoardEditRoot)
    b3_14 = Button(BoardEditRoot)
    b3_15 = Button(BoardEditRoot)
    b3_16 = Button(BoardEditRoot)
    b3_17 = Button(BoardEditRoot)
    b3_18 = Button(BoardEditRoot)
    b3_19 = Button(BoardEditRoot)
    b3_20 = Button(BoardEditRoot)
    b3_21 = Button(BoardEditRoot)
    b3_22 = Button(BoardEditRoot)
    b3_23 = Button(BoardEditRoot)
    b3_24 = Button(BoardEditRoot)
    b3_25 = Button(BoardEditRoot)
    b3_26 = Button(BoardEditRoot)
    b3_27 = Button(BoardEditRoot)
    b3_28 = Button(BoardEditRoot)
    b3_29 = Button(BoardEditRoot)
    b3_30 = Button(BoardEditRoot)
    b3_31 = Button(BoardEditRoot)
    b3_32 = Button(BoardEditRoot)
    b3_33 = Button(BoardEditRoot)
    b3_34 = Button(BoardEditRoot)
    b3_35 = Button(BoardEditRoot)
    b3_36 = Button(BoardEditRoot)
    b3_37 = Button(BoardEditRoot)
    b3_38 = Button(BoardEditRoot)
    b3_39 = Button(BoardEditRoot)
    b3_40 = Button(BoardEditRoot)
    b3_41 = Button(BoardEditRoot)
    b3_42 = Button(BoardEditRoot)
    b3_43 = Button(BoardEditRoot)
    b3_44 = Button(BoardEditRoot)
    b3_45 = Button(BoardEditRoot)
    b3_46 = Button(BoardEditRoot)
    b3_47 = Button(BoardEditRoot)

    c3_B.append(b3_0)
    c3_B.append(b3_1)
    c3_B.append(b3_2)
    c3_B.append(b3_3)
    c3_B.append(b3_4)
    c3_B.append(b3_5)
    c3_B.append(b3_6)
    c3_B.append(b3_7)
    c3_B.append(b3_8)
    c3_B.append(b3_9)
    c3_B.append(b3_10)
    c3_B.append(b3_11)
    c3_B.append(b3_12)
    c3_B.append(b3_13)
    c3_B.append(b3_14)
    c3_B.append(b3_15)
    c3_B.append(b3_16)
    c3_B.append(b3_17)
    c3_B.append(b3_18)
    c3_B.append(b3_19)
    c3_B.append(b3_20)
    c3_B.append(b3_21)
    c3_B.append(b3_22)
    c3_B.append(b3_23)
    c3_B.append(b3_24)
    c3_B.append(b3_25)
    c3_B.append(b3_26)
    c3_B.append(b3_27)
    c3_B.append(b3_28)
    c3_B.append(b3_29)
    c3_B.append(b3_30)
    c3_B.append(b3_31)
    c3_B.append(b3_32)
    c3_B.append(b3_33)
    c3_B.append(b3_34)
    c3_B.append(b3_35)
    c3_B.append(b3_36)
    c3_B.append(b3_37)
    c3_B.append(b3_38)
    c3_B.append(b3_39)
    c3_B.append(b3_40)
    c3_B.append(b3_41)
    c3_B.append(b3_42)
    c3_B.append(b3_43)
    c3_B.append(b3_44)
    c3_B.append(b3_45)
    c3_B.append(b3_46)
    c3_B.append(b3_47)


##############_Category 4_###################


    c4=Button(BoardEditRoot)
    c4_B = []
    b4_0 = Button(BoardEditRoot)
    b4_1 = Button(BoardEditRoot)
    b4_2 = Button(BoardEditRoot)
    b4_3 = Button(BoardEditRoot)
    b4_4 = Button(BoardEditRoot)
    b4_5 = Button(BoardEditRoot)
    b4_6 = Button(BoardEditRoot)
    b4_7 = Button(BoardEditRoot)
    b4_8 = Button(BoardEditRoot)
    b4_9 = Button(BoardEditRoot)
    b4_10 = Button(BoardEditRoot)
    b4_11 = Button(BoardEditRoot)
    b4_12 = Button(BoardEditRoot)
    b4_13 = Button(BoardEditRoot)
    b4_14 = Button(BoardEditRoot)
    b4_15 = Button(BoardEditRoot)
    b4_16 = Button(BoardEditRoot)
    b4_17 = Button(BoardEditRoot)
    b4_18 = Button(BoardEditRoot)
    b4_19 = Button(BoardEditRoot)
    b4_20 = Button(BoardEditRoot)
    b4_21 = Button(BoardEditRoot)
    b4_22 = Button(BoardEditRoot)
    b4_23 = Button(BoardEditRoot)
    b4_24 = Button(BoardEditRoot)
    b4_25 = Button(BoardEditRoot)
    b4_26 = Button(BoardEditRoot)
    b4_27 = Button(BoardEditRoot)
    b4_28 = Button(BoardEditRoot)
    b4_29 = Button(BoardEditRoot)
    b4_30 = Button(BoardEditRoot)
    b4_31 = Button(BoardEditRoot)
    b4_32 = Button(BoardEditRoot)
    b4_33 = Button(BoardEditRoot)
    b4_34 = Button(BoardEditRoot)
    b4_35 = Button(BoardEditRoot)
    b4_36 = Button(BoardEditRoot)
    b4_37 = Button(BoardEditRoot)
    b4_38 = Button(BoardEditRoot)
    b4_39 = Button(BoardEditRoot)
    b4_40 = Button(BoardEditRoot)
    b4_41 = Button(BoardEditRoot)
    b4_42 = Button(BoardEditRoot)
    b4_43 = Button(BoardEditRoot)
    b4_44 = Button(BoardEditRoot)
    b4_45 = Button(BoardEditRoot)
    b4_46 = Button(BoardEditRoot)
    b4_47 = Button(BoardEditRoot)

    c4_B.append(b4_0)
    c4_B.append(b4_1)
    c4_B.append(b4_2)
    c4_B.append(b4_3)
    c4_B.append(b4_4)
    c4_B.append(b4_5)
    c4_B.append(b4_6)
    c4_B.append(b4_7)
    c4_B.append(b4_8)
    c4_B.append(b4_9)
    c4_B.append(b4_10)
    c4_B.append(b4_11)
    c4_B.append(b4_12)
    c4_B.append(b4_13)
    c4_B.append(b4_14)
    c4_B.append(b4_15)
    c4_B.append(b4_16)
    c4_B.append(b4_17)
    c4_B.append(b4_18)
    c4_B.append(b4_19)
    c4_B.append(b4_20)
    c4_B.append(b4_21)
    c4_B.append(b4_22)
    c4_B.append(b4_23)
    c4_B.append(b4_24)
    c4_B.append(b4_25)
    c4_B.append(b4_26)
    c4_B.append(b4_27)
    c4_B.append(b4_28)
    c4_B.append(b4_29)
    c4_B.append(b4_30)
    c4_B.append(b4_31)
    c4_B.append(b4_32)
    c4_B.append(b4_33)
    c4_B.append(b4_34)
    c4_B.append(b4_35)
    c4_B.append(b4_36)
    c4_B.append(b4_37)
    c4_B.append(b4_38)
    c4_B.append(b4_39)
    c4_B.append(b4_40)
    c4_B.append(b4_41)
    c4_B.append(b4_42)
    c4_B.append(b4_43)
    c4_B.append(b4_44)
    c4_B.append(b4_45)
    c4_B.append(b4_46)
    c4_B.append(b4_47)


##############_Category 5_###################


    c5=Button(BoardEditRoot)
    c5_B = []
    b5_0 = Button(BoardEditRoot)
    b5_1 = Button(BoardEditRoot)
    b5_2 = Button(BoardEditRoot)
    b5_3 = Button(BoardEditRoot)
    b5_4 = Button(BoardEditRoot)
    b5_5 = Button(BoardEditRoot)
    b5_6 = Button(BoardEditRoot)
    b5_7 = Button(BoardEditRoot)
    b5_8 = Button(BoardEditRoot)
    b5_9 = Button(BoardEditRoot)
    b5_10 = Button(BoardEditRoot)
    b5_11 = Button(BoardEditRoot)
    b5_12 = Button(BoardEditRoot)
    b5_13 = Button(BoardEditRoot)
    b5_14 = Button(BoardEditRoot)
    b5_15 = Button(BoardEditRoot)
    b5_16 = Button(BoardEditRoot)
    b5_17 = Button(BoardEditRoot)
    b5_18 = Button(BoardEditRoot)
    b5_19 = Button(BoardEditRoot)
    b5_20 = Button(BoardEditRoot)
    b5_21 = Button(BoardEditRoot)
    b5_22 = Button(BoardEditRoot)
    b5_23 = Button(BoardEditRoot)
    b5_24 = Button(BoardEditRoot)
    b5_25 = Button(BoardEditRoot)
    b5_26 = Button(BoardEditRoot)
    b5_27 = Button(BoardEditRoot)
    b5_28 = Button(BoardEditRoot)
    b5_29 = Button(BoardEditRoot)
    b5_30 = Button(BoardEditRoot)
    b5_31 = Button(BoardEditRoot)
    b5_32 = Button(BoardEditRoot)
    b5_33 = Button(BoardEditRoot)
    b5_34 = Button(BoardEditRoot)
    b5_35 = Button(BoardEditRoot)
    b5_36 = Button(BoardEditRoot)
    b5_37 = Button(BoardEditRoot)
    b5_38 = Button(BoardEditRoot)
    b5_39 = Button(BoardEditRoot)
    b5_40 = Button(BoardEditRoot)
    b5_41 = Button(BoardEditRoot)
    b5_42 = Button(BoardEditRoot)
    b5_43 = Button(BoardEditRoot)
    b5_44 = Button(BoardEditRoot)
    b5_45 = Button(BoardEditRoot)
    b5_46 = Button(BoardEditRoot)
    b5_47 = Button(BoardEditRoot)

    c5_B.append(b5_0)
    c5_B.append(b5_1)
    c5_B.append(b5_2)
    c5_B.append(b5_3)
    c5_B.append(b5_4)
    c5_B.append(b5_5)
    c5_B.append(b5_6)
    c5_B.append(b5_7)
    c5_B.append(b5_8)
    c5_B.append(b5_9)
    c5_B.append(b5_10)
    c5_B.append(b5_11)
    c5_B.append(b5_12)
    c5_B.append(b5_13)
    c5_B.append(b5_14)
    c5_B.append(b5_15)
    c5_B.append(b5_16)
    c5_B.append(b5_17)
    c5_B.append(b5_18)
    c5_B.append(b5_19)
    c5_B.append(b5_20)
    c5_B.append(b5_21)
    c5_B.append(b5_22)
    c5_B.append(b5_23)
    c5_B.append(b5_24)
    c5_B.append(b5_25)
    c5_B.append(b5_26)
    c5_B.append(b5_27)
    c5_B.append(b5_28)
    c5_B.append(b5_29)
    c5_B.append(b5_30)
    c5_B.append(b5_31)
    c5_B.append(b5_32)
    c5_B.append(b5_33)
    c5_B.append(b5_34)
    c5_B.append(b5_35)
    c5_B.append(b5_36)
    c5_B.append(b5_37)
    c5_B.append(b5_38)
    c5_B.append(b5_39)
    c5_B.append(b5_40)
    c5_B.append(b5_41)
    c5_B.append(b5_42)
    c5_B.append(b5_43)
    c5_B.append(b5_44)
    c5_B.append(b5_45)
    c5_B.append(b5_46)
    c5_B.append(b5_47)


##############_Category 6_###################


    c6=Button(BoardEditRoot)
    c6_B = []
    b6_0 = Button(BoardEditRoot)
    b6_1 = Button(BoardEditRoot)
    b6_2 = Button(BoardEditRoot)
    b6_3 = Button(BoardEditRoot)
    b6_4 = Button(BoardEditRoot)
    b6_5 = Button(BoardEditRoot)
    b6_6 = Button(BoardEditRoot)
    b6_7 = Button(BoardEditRoot)
    b6_8 = Button(BoardEditRoot)
    b6_9 = Button(BoardEditRoot)
    b6_10 = Button(BoardEditRoot)
    b6_11 = Button(BoardEditRoot)
    b6_12 = Button(BoardEditRoot)
    b6_13 = Button(BoardEditRoot)
    b6_14 = Button(BoardEditRoot)
    b6_15 = Button(BoardEditRoot)
    b6_16 = Button(BoardEditRoot)
    b6_17 = Button(BoardEditRoot)
    b6_18 = Button(BoardEditRoot)
    b6_19 = Button(BoardEditRoot)
    b6_20 = Button(BoardEditRoot)
    b6_21 = Button(BoardEditRoot)
    b6_22 = Button(BoardEditRoot)
    b6_23 = Button(BoardEditRoot)
    b6_24 = Button(BoardEditRoot)
    b6_25 = Button(BoardEditRoot)
    b6_26 = Button(BoardEditRoot)
    b6_27 = Button(BoardEditRoot)
    b6_28 = Button(BoardEditRoot)
    b6_29 = Button(BoardEditRoot)
    b6_30 = Button(BoardEditRoot)
    b6_31 = Button(BoardEditRoot)
    b6_32 = Button(BoardEditRoot)
    b6_33 = Button(BoardEditRoot)
    b6_34 = Button(BoardEditRoot)
    b6_35 = Button(BoardEditRoot)
    b6_36 = Button(BoardEditRoot)
    b6_37 = Button(BoardEditRoot)
    b6_38 = Button(BoardEditRoot)
    b6_39 = Button(BoardEditRoot)
    b6_40 = Button(BoardEditRoot)
    b6_41 = Button(BoardEditRoot)
    b6_42 = Button(BoardEditRoot)
    b6_43 = Button(BoardEditRoot)
    b6_44 = Button(BoardEditRoot)
    b6_45 = Button(BoardEditRoot)
    b6_46 = Button(BoardEditRoot)
    b6_47 = Button(BoardEditRoot)

    c6_B.append(b6_0)
    c6_B.append(b6_1)
    c6_B.append(b6_2)
    c6_B.append(b6_3)
    c6_B.append(b6_4)
    c6_B.append(b6_5)
    c6_B.append(b6_6)
    c6_B.append(b6_7)
    c6_B.append(b6_8)
    c6_B.append(b6_9)
    c6_B.append(b6_10)
    c6_B.append(b6_11)
    c6_B.append(b6_12)
    c6_B.append(b6_13)
    c6_B.append(b6_14)
    c6_B.append(b6_15)
    c6_B.append(b6_16)
    c6_B.append(b6_17)
    c6_B.append(b6_18)
    c6_B.append(b6_19)
    c6_B.append(b6_20)
    c6_B.append(b6_21)
    c6_B.append(b6_22)
    c6_B.append(b6_23)
    c6_B.append(b6_24)
    c6_B.append(b6_25)
    c6_B.append(b6_26)
    c6_B.append(b6_27)
    c6_B.append(b6_28)
    c6_B.append(b6_29)
    c6_B.append(b6_30)
    c6_B.append(b6_31)
    c6_B.append(b6_32)
    c6_B.append(b6_33)
    c6_B.append(b6_34)
    c6_B.append(b6_35)
    c6_B.append(b6_36)
    c6_B.append(b6_37)
    c6_B.append(b6_38)
    c6_B.append(b6_39)
    c6_B.append(b6_40)
    c6_B.append(b6_41)
    c6_B.append(b6_42)
    c6_B.append(b6_43)
    c6_B.append(b6_44)
    c6_B.append(b6_45)
    c6_B.append(b6_46)
    c6_B.append(b6_47)


##############_Category 7_###################


    c7=Button(BoardEditRoot)
    c7_B = []
    b7_0 = Button(BoardEditRoot)
    b7_1 = Button(BoardEditRoot)
    b7_2 = Button(BoardEditRoot)
    b7_3 = Button(BoardEditRoot)
    b7_4 = Button(BoardEditRoot)
    b7_5 = Button(BoardEditRoot)
    b7_6 = Button(BoardEditRoot)
    b7_7 = Button(BoardEditRoot)
    b7_8 = Button(BoardEditRoot)
    b7_9 = Button(BoardEditRoot)
    b7_10 = Button(BoardEditRoot)
    b7_11 = Button(BoardEditRoot)
    b7_12 = Button(BoardEditRoot)
    b7_13 = Button(BoardEditRoot)
    b7_14 = Button(BoardEditRoot)
    b7_15 = Button(BoardEditRoot)
    b7_16 = Button(BoardEditRoot)
    b7_17 = Button(BoardEditRoot)
    b7_18 = Button(BoardEditRoot)
    b7_19 = Button(BoardEditRoot)
    b7_20 = Button(BoardEditRoot)
    b7_21 = Button(BoardEditRoot)
    b7_22 = Button(BoardEditRoot)
    b7_23 = Button(BoardEditRoot)
    b7_24 = Button(BoardEditRoot)
    b7_25 = Button(BoardEditRoot)
    b7_26 = Button(BoardEditRoot)
    b7_27 = Button(BoardEditRoot)
    b7_28 = Button(BoardEditRoot)
    b7_29 = Button(BoardEditRoot)
    b7_30 = Button(BoardEditRoot)
    b7_31 = Button(BoardEditRoot)
    b7_32 = Button(BoardEditRoot)
    b7_33 = Button(BoardEditRoot)
    b7_34 = Button(BoardEditRoot)
    b7_35 = Button(BoardEditRoot)
    b7_36 = Button(BoardEditRoot)
    b7_37 = Button(BoardEditRoot)
    b7_38 = Button(BoardEditRoot)
    b7_39 = Button(BoardEditRoot)
    b7_40 = Button(BoardEditRoot)
    b7_41 = Button(BoardEditRoot)
    b7_42 = Button(BoardEditRoot)
    b7_43 = Button(BoardEditRoot)
    b7_44 = Button(BoardEditRoot)
    b7_45 = Button(BoardEditRoot)
    b7_46 = Button(BoardEditRoot)
    b7_47 = Button(BoardEditRoot)

    c7_B.append(b7_0)
    c7_B.append(b7_1)
    c7_B.append(b7_2)
    c7_B.append(b7_3)
    c7_B.append(b7_4)
    c7_B.append(b7_5)
    c7_B.append(b7_6)
    c7_B.append(b7_7)
    c7_B.append(b7_8)
    c7_B.append(b7_9)
    c7_B.append(b7_10)
    c7_B.append(b7_11)
    c7_B.append(b7_12)
    c7_B.append(b7_13)
    c7_B.append(b7_14)
    c7_B.append(b7_15)
    c7_B.append(b7_16)
    c7_B.append(b7_17)
    c7_B.append(b7_18)
    c7_B.append(b7_19)
    c7_B.append(b7_20)
    c7_B.append(b7_21)
    c7_B.append(b7_22)
    c7_B.append(b7_23)
    c7_B.append(b7_24)
    c7_B.append(b7_25)
    c7_B.append(b7_26)
    c7_B.append(b7_27)
    c7_B.append(b7_28)
    c7_B.append(b7_29)
    c7_B.append(b7_30)
    c7_B.append(b7_31)
    c7_B.append(b7_32)
    c7_B.append(b7_33)
    c7_B.append(b7_34)
    c7_B.append(b7_35)
    c7_B.append(b7_36)
    c7_B.append(b7_37)
    c7_B.append(b7_38)
    c7_B.append(b7_39)
    c7_B.append(b7_40)
    c7_B.append(b7_41)
    c7_B.append(b7_42)
    c7_B.append(b7_43)
    c7_B.append(b7_44)
    c7_B.append(b7_45)
    c7_B.append(b7_46)
    c7_B.append(b7_47)


##############_Category 8_###################


    c8=Button(BoardEditRoot)
    c8_B = []
    b8_0 = Button(BoardEditRoot)
    b8_1 = Button(BoardEditRoot)
    b8_2 = Button(BoardEditRoot)
    b8_3 = Button(BoardEditRoot)
    b8_4 = Button(BoardEditRoot)
    b8_5 = Button(BoardEditRoot)
    b8_6 = Button(BoardEditRoot)
    b8_7 = Button(BoardEditRoot)
    b8_8 = Button(BoardEditRoot)
    b8_9 = Button(BoardEditRoot)
    b8_10 = Button(BoardEditRoot)
    b8_11 = Button(BoardEditRoot)
    b8_12 = Button(BoardEditRoot)
    b8_13 = Button(BoardEditRoot)
    b8_14 = Button(BoardEditRoot)
    b8_15 = Button(BoardEditRoot)
    b8_16 = Button(BoardEditRoot)
    b8_17 = Button(BoardEditRoot)
    b8_18 = Button(BoardEditRoot)
    b8_19 = Button(BoardEditRoot)
    b8_20 = Button(BoardEditRoot)
    b8_21 = Button(BoardEditRoot)
    b8_22 = Button(BoardEditRoot)
    b8_23 = Button(BoardEditRoot)
    b8_24 = Button(BoardEditRoot)
    b8_25 = Button(BoardEditRoot)
    b8_26 = Button(BoardEditRoot)
    b8_27 = Button(BoardEditRoot)
    b8_28 = Button(BoardEditRoot)
    b8_29 = Button(BoardEditRoot)
    b8_30 = Button(BoardEditRoot)
    b8_31 = Button(BoardEditRoot)
    b8_32 = Button(BoardEditRoot)
    b8_33 = Button(BoardEditRoot)
    b8_34 = Button(BoardEditRoot)
    b8_35 = Button(BoardEditRoot)
    b8_36 = Button(BoardEditRoot)
    b8_37 = Button(BoardEditRoot)
    b8_38 = Button(BoardEditRoot)
    b8_39 = Button(BoardEditRoot)
    b8_40 = Button(BoardEditRoot)
    b8_41 = Button(BoardEditRoot)
    b8_42 = Button(BoardEditRoot)
    b8_43 = Button(BoardEditRoot)
    b8_44 = Button(BoardEditRoot)
    b8_45 = Button(BoardEditRoot)
    b8_46 = Button(BoardEditRoot)
    b8_47 = Button(BoardEditRoot)

    c8_B.append(b8_0)
    c8_B.append(b8_1)
    c8_B.append(b8_2)
    c8_B.append(b8_3)
    c8_B.append(b8_4)
    c8_B.append(b8_5)
    c8_B.append(b8_6)
    c8_B.append(b8_7)
    c8_B.append(b8_8)
    c8_B.append(b8_9)
    c8_B.append(b8_10)
    c8_B.append(b8_11)
    c8_B.append(b8_12)
    c8_B.append(b8_13)
    c8_B.append(b8_14)
    c8_B.append(b8_15)
    c8_B.append(b8_16)
    c8_B.append(b8_17)
    c8_B.append(b8_18)
    c8_B.append(b8_19)
    c8_B.append(b8_20)
    c8_B.append(b8_21)
    c8_B.append(b8_22)
    c8_B.append(b8_23)
    c8_B.append(b8_24)
    c8_B.append(b8_25)
    c8_B.append(b8_26)
    c8_B.append(b8_27)
    c8_B.append(b8_28)
    c8_B.append(b8_29)
    c8_B.append(b8_30)
    c8_B.append(b8_31)
    c8_B.append(b8_32)
    c8_B.append(b8_33)
    c8_B.append(b8_34)
    c8_B.append(b8_35)
    c8_B.append(b8_36)
    c8_B.append(b8_37)
    c8_B.append(b8_38)
    c8_B.append(b8_39)
    c8_B.append(b8_40)
    c8_B.append(b8_41)
    c8_B.append(b8_42)
    c8_B.append(b8_43)
    c8_B.append(b8_44)
    c8_B.append(b8_45)
    c8_B.append(b8_46)
    c8_B.append(b8_47)


##############_Category 9_###################


    c9=Button(BoardEditRoot)
    c9_B = []
    b9_0 = Button(BoardEditRoot)
    b9_1 = Button(BoardEditRoot)
    b9_2 = Button(BoardEditRoot)
    b9_3 = Button(BoardEditRoot)
    b9_4 = Button(BoardEditRoot)
    b9_5 = Button(BoardEditRoot)
    b9_6 = Button(BoardEditRoot)
    b9_7 = Button(BoardEditRoot)
    b9_8 = Button(BoardEditRoot)
    b9_9 = Button(BoardEditRoot)
    b9_10 = Button(BoardEditRoot)
    b9_11 = Button(BoardEditRoot)
    b9_12 = Button(BoardEditRoot)
    b9_13 = Button(BoardEditRoot)
    b9_14 = Button(BoardEditRoot)
    b9_15 = Button(BoardEditRoot)
    b9_16 = Button(BoardEditRoot)
    b9_17 = Button(BoardEditRoot)
    b9_18 = Button(BoardEditRoot)
    b9_19 = Button(BoardEditRoot)
    b9_20 = Button(BoardEditRoot)
    b9_21 = Button(BoardEditRoot)
    b9_22 = Button(BoardEditRoot)
    b9_23 = Button(BoardEditRoot)
    b9_24 = Button(BoardEditRoot)
    b9_25 = Button(BoardEditRoot)
    b9_26 = Button(BoardEditRoot)
    b9_27 = Button(BoardEditRoot)
    b9_28 = Button(BoardEditRoot)
    b9_29 = Button(BoardEditRoot)
    b9_30 = Button(BoardEditRoot)
    b9_31 = Button(BoardEditRoot)
    b9_32 = Button(BoardEditRoot)
    b9_33 = Button(BoardEditRoot)
    b9_34 = Button(BoardEditRoot)
    b9_35 = Button(BoardEditRoot)
    b9_36 = Button(BoardEditRoot)
    b9_37 = Button(BoardEditRoot)
    b9_38 = Button(BoardEditRoot)
    b9_39 = Button(BoardEditRoot)
    b9_40 = Button(BoardEditRoot)
    b9_41 = Button(BoardEditRoot)
    b9_42 = Button(BoardEditRoot)
    b9_43 = Button(BoardEditRoot)
    b9_44 = Button(BoardEditRoot)
    b9_45 = Button(BoardEditRoot)
    b9_46 = Button(BoardEditRoot)
    b9_47 = Button(BoardEditRoot)

    c9_B.append(b9_0)
    c9_B.append(b9_1)
    c9_B.append(b9_2)
    c9_B.append(b9_3)
    c9_B.append(b9_4)
    c9_B.append(b9_5)
    c9_B.append(b9_6)
    c9_B.append(b9_7)
    c9_B.append(b9_8)
    c9_B.append(b9_9)
    c9_B.append(b9_10)
    c9_B.append(b9_11)
    c9_B.append(b9_12)
    c9_B.append(b9_13)
    c9_B.append(b9_14)
    c9_B.append(b9_15)
    c9_B.append(b9_16)
    c9_B.append(b9_17)
    c9_B.append(b9_18)
    c9_B.append(b9_19)
    c9_B.append(b9_20)
    c9_B.append(b9_21)
    c9_B.append(b9_22)
    c9_B.append(b9_23)
    c9_B.append(b9_24)
    c9_B.append(b9_25)
    c9_B.append(b9_26)
    c9_B.append(b9_27)
    c9_B.append(b9_28)
    c9_B.append(b9_29)
    c9_B.append(b9_30)
    c9_B.append(b9_31)
    c9_B.append(b9_32)
    c9_B.append(b9_33)
    c9_B.append(b9_34)
    c9_B.append(b9_35)
    c9_B.append(b9_36)
    c9_B.append(b9_37)
    c9_B.append(b9_38)
    c9_B.append(b9_39)
    c9_B.append(b9_40)
    c9_B.append(b9_41)
    c9_B.append(b9_42)
    c9_B.append(b9_43)
    c9_B.append(b9_44)
    c9_B.append(b9_45)
    c9_B.append(b9_46)
    c9_B.append(b9_47)


##############_Category 10_###################


    c10=Button(BoardEditRoot)
    c10_B = []
    b10_0 = Button(BoardEditRoot)
    b10_1 = Button(BoardEditRoot)
    b10_2 = Button(BoardEditRoot)
    b10_3 = Button(BoardEditRoot)
    b10_4 = Button(BoardEditRoot)
    b10_5 = Button(BoardEditRoot)
    b10_6 = Button(BoardEditRoot)
    b10_7 = Button(BoardEditRoot)
    b10_8 = Button(BoardEditRoot)
    b10_9 = Button(BoardEditRoot)
    b10_10 = Button(BoardEditRoot)
    b10_11 = Button(BoardEditRoot)
    b10_12 = Button(BoardEditRoot)
    b10_13 = Button(BoardEditRoot)
    b10_14 = Button(BoardEditRoot)
    b10_15 = Button(BoardEditRoot)
    b10_16 = Button(BoardEditRoot)
    b10_17 = Button(BoardEditRoot)
    b10_18 = Button(BoardEditRoot)
    b10_19 = Button(BoardEditRoot)
    b10_20 = Button(BoardEditRoot)
    b10_21 = Button(BoardEditRoot)
    b10_22 = Button(BoardEditRoot)
    b10_23 = Button(BoardEditRoot)
    b10_24 = Button(BoardEditRoot)
    b10_25 = Button(BoardEditRoot)
    b10_26 = Button(BoardEditRoot)
    b10_27 = Button(BoardEditRoot)
    b10_28 = Button(BoardEditRoot)
    b10_29 = Button(BoardEditRoot)
    b10_30 = Button(BoardEditRoot)
    b10_31 = Button(BoardEditRoot)
    b10_32 = Button(BoardEditRoot)
    b10_33 = Button(BoardEditRoot)
    b10_34 = Button(BoardEditRoot)
    b10_35 = Button(BoardEditRoot)
    b10_36 = Button(BoardEditRoot)
    b10_37 = Button(BoardEditRoot)
    b10_38 = Button(BoardEditRoot)
    b10_39 = Button(BoardEditRoot)
    b10_40 = Button(BoardEditRoot)
    b10_41 = Button(BoardEditRoot)
    b10_42 = Button(BoardEditRoot)
    b10_43 = Button(BoardEditRoot)
    b10_44 = Button(BoardEditRoot)
    b10_45 = Button(BoardEditRoot)
    b10_46 = Button(BoardEditRoot)
    b10_47 = Button(BoardEditRoot)

    c10_B.append(b10_0)
    c10_B.append(b10_1)
    c10_B.append(b10_2)
    c10_B.append(b10_3)
    c10_B.append(b10_4)
    c10_B.append(b10_5)
    c10_B.append(b10_6)
    c10_B.append(b10_7)
    c10_B.append(b10_8)
    c10_B.append(b10_9)
    c10_B.append(b10_10)
    c10_B.append(b10_11)
    c10_B.append(b10_12)
    c10_B.append(b10_13)
    c10_B.append(b10_14)
    c10_B.append(b10_15)
    c10_B.append(b10_16)
    c10_B.append(b10_17)
    c10_B.append(b10_18)
    c10_B.append(b10_19)
    c10_B.append(b10_20)
    c10_B.append(b10_21)
    c10_B.append(b10_22)
    c10_B.append(b10_23)
    c10_B.append(b10_24)
    c10_B.append(b10_25)
    c10_B.append(b10_26)
    c10_B.append(b10_27)
    c10_B.append(b10_28)
    c10_B.append(b10_29)
    c10_B.append(b10_30)
    c10_B.append(b10_31)
    c10_B.append(b10_32)
    c10_B.append(b10_33)
    c10_B.append(b10_34)
    c10_B.append(b10_35)
    c10_B.append(b10_36)
    c10_B.append(b10_37)
    c10_B.append(b10_38)
    c10_B.append(b10_39)
    c10_B.append(b10_40)
    c10_B.append(b10_41)
    c10_B.append(b10_42)
    c10_B.append(b10_43)
    c10_B.append(b10_44)
    c10_B.append(b10_45)
    c10_B.append(b10_46)
    c10_B.append(b10_47)
   

##############_Category 11_###################


    c11=Button(BoardEditRoot)
    c11_B = []
    b11_0 = Button(BoardEditRoot)
    b11_1 = Button(BoardEditRoot)
    b11_2 = Button(BoardEditRoot)
    b11_3 = Button(BoardEditRoot)
    b11_4 = Button(BoardEditRoot)
    b11_5 = Button(BoardEditRoot)
    b11_6 = Button(BoardEditRoot)
    b11_7 = Button(BoardEditRoot)
    b11_8 = Button(BoardEditRoot)
    b11_9 = Button(BoardEditRoot)
    b11_11 = Button(BoardEditRoot)
    b11_11 = Button(BoardEditRoot)
    b11_12 = Button(BoardEditRoot)
    b11_13 = Button(BoardEditRoot)
    b11_14 = Button(BoardEditRoot)
    b11_15 = Button(BoardEditRoot)
    b11_16 = Button(BoardEditRoot)
    b11_17 = Button(BoardEditRoot)
    b11_18 = Button(BoardEditRoot)
    b11_19 = Button(BoardEditRoot)
    b11_20 = Button(BoardEditRoot)
    b11_21 = Button(BoardEditRoot)
    b11_22 = Button(BoardEditRoot)
    b11_23 = Button(BoardEditRoot)
    b11_24 = Button(BoardEditRoot)
    b11_25 = Button(BoardEditRoot)
    b11_26 = Button(BoardEditRoot)
    b11_27 = Button(BoardEditRoot)
    b11_28 = Button(BoardEditRoot)
    b11_29 = Button(BoardEditRoot)
    b11_30 = Button(BoardEditRoot)
    b11_31 = Button(BoardEditRoot)
    b11_32 = Button(BoardEditRoot)
    b11_33 = Button(BoardEditRoot)
    b11_34 = Button(BoardEditRoot)
    b11_35 = Button(BoardEditRoot)
    b11_36 = Button(BoardEditRoot)
    b11_37 = Button(BoardEditRoot)
    b11_38 = Button(BoardEditRoot)
    b11_39 = Button(BoardEditRoot)
    b11_40 = Button(BoardEditRoot)
    b11_41 = Button(BoardEditRoot)
    b11_42 = Button(BoardEditRoot)
    b11_43 = Button(BoardEditRoot)
    b11_44 = Button(BoardEditRoot)
    b11_45 = Button(BoardEditRoot)
    b11_46 = Button(BoardEditRoot)
    b11_47 = Button(BoardEditRoot)

    c11_B.append(b11_0)
    c11_B.append(b11_1)
    c11_B.append(b11_2)
    c11_B.append(b11_3)
    c11_B.append(b11_4)
    c11_B.append(b11_5)
    c11_B.append(b11_6)
    c11_B.append(b11_7)
    c11_B.append(b11_8)
    c11_B.append(b11_9)
    c11_B.append(b11_11)
    c11_B.append(b11_11)
    c11_B.append(b11_12)
    c11_B.append(b11_13)
    c11_B.append(b11_14)
    c11_B.append(b11_15)
    c11_B.append(b11_16)
    c11_B.append(b11_17)
    c11_B.append(b11_18)
    c11_B.append(b11_19)
    c11_B.append(b11_20)
    c11_B.append(b11_21)
    c11_B.append(b11_22)
    c11_B.append(b11_23)
    c11_B.append(b11_24)
    c11_B.append(b11_25)
    c11_B.append(b11_26)
    c11_B.append(b11_27)
    c11_B.append(b11_28)
    c11_B.append(b11_29)
    c11_B.append(b11_30)
    c11_B.append(b11_31)
    c11_B.append(b11_32)
    c11_B.append(b11_33)
    c11_B.append(b11_34)
    c11_B.append(b11_35)
    c11_B.append(b11_36)
    c11_B.append(b11_37)
    c11_B.append(b11_38)
    c11_B.append(b11_39)
    c11_B.append(b11_40)
    c11_B.append(b11_41)
    c11_B.append(b11_42)
    c11_B.append(b11_43)
    c11_B.append(b11_44)
    c11_B.append(b11_45)
    c11_B.append(b11_46)
    c11_B.append(b11_47)
   

##############_Category 12_###################


    c12=Button(BoardEditRoot)
    c12_B = []
    b12_0 = Button(BoardEditRoot)
    b12_1 = Button(BoardEditRoot)
    b12_2 = Button(BoardEditRoot)
    b12_3 = Button(BoardEditRoot)
    b12_4 = Button(BoardEditRoot)
    b12_5 = Button(BoardEditRoot)
    b12_6 = Button(BoardEditRoot)
    b12_7 = Button(BoardEditRoot)
    b12_8 = Button(BoardEditRoot)
    b12_9 = Button(BoardEditRoot)
    b12_12 = Button(BoardEditRoot)
    b12_12 = Button(BoardEditRoot)
    b12_12 = Button(BoardEditRoot)
    b12_13 = Button(BoardEditRoot)
    b12_14 = Button(BoardEditRoot)
    b12_15 = Button(BoardEditRoot)
    b12_16 = Button(BoardEditRoot)
    b12_17 = Button(BoardEditRoot)
    b12_18 = Button(BoardEditRoot)
    b12_19 = Button(BoardEditRoot)
    b12_20 = Button(BoardEditRoot)
    b12_21 = Button(BoardEditRoot)
    b12_22 = Button(BoardEditRoot)
    b12_23 = Button(BoardEditRoot)
    b12_24 = Button(BoardEditRoot)
    b12_25 = Button(BoardEditRoot)
    b12_26 = Button(BoardEditRoot)
    b12_27 = Button(BoardEditRoot)
    b12_28 = Button(BoardEditRoot)
    b12_29 = Button(BoardEditRoot)
    b12_30 = Button(BoardEditRoot)
    b12_31 = Button(BoardEditRoot)
    b12_32 = Button(BoardEditRoot)
    b12_33 = Button(BoardEditRoot)
    b12_34 = Button(BoardEditRoot)
    b12_35 = Button(BoardEditRoot)
    b12_36 = Button(BoardEditRoot)
    b12_37 = Button(BoardEditRoot)
    b12_38 = Button(BoardEditRoot)
    b12_39 = Button(BoardEditRoot)
    b12_40 = Button(BoardEditRoot)
    b12_41 = Button(BoardEditRoot)
    b12_42 = Button(BoardEditRoot)
    b12_43 = Button(BoardEditRoot)
    b12_44 = Button(BoardEditRoot)
    b12_45 = Button(BoardEditRoot)
    b12_46 = Button(BoardEditRoot)
    b12_47 = Button(BoardEditRoot)

    c12_B.append(b12_0)
    c12_B.append(b12_1)
    c12_B.append(b12_2)
    c12_B.append(b12_3)
    c12_B.append(b12_4)
    c12_B.append(b12_5)
    c12_B.append(b12_6)
    c12_B.append(b12_7)
    c12_B.append(b12_8)
    c12_B.append(b12_9)
    c12_B.append(b12_12)
    c12_B.append(b12_12)
    c12_B.append(b12_12)
    c12_B.append(b12_13)
    c12_B.append(b12_14)
    c12_B.append(b12_15)
    c12_B.append(b12_16)
    c12_B.append(b12_17)
    c12_B.append(b12_18)
    c12_B.append(b12_19)
    c12_B.append(b12_20)
    c12_B.append(b12_21)
    c12_B.append(b12_22)
    c12_B.append(b12_23)
    c12_B.append(b12_24)
    c12_B.append(b12_25)
    c12_B.append(b12_26)
    c12_B.append(b12_27)
    c12_B.append(b12_28)
    c12_B.append(b12_29)
    c12_B.append(b12_30)
    c12_B.append(b12_31)
    c12_B.append(b12_32)
    c12_B.append(b12_33)
    c12_B.append(b12_34)
    c12_B.append(b12_35)
    c12_B.append(b12_36)
    c12_B.append(b12_37)
    c12_B.append(b12_38)
    c12_B.append(b12_39)
    c12_B.append(b12_40)
    c12_B.append(b12_41)
    c12_B.append(b12_42)
    c12_B.append(b12_43)
    c12_B.append(b12_44)
    c12_B.append(b12_45)
    c12_B.append(b12_46)
    c12_B.append(b12_47)
   

######################_Data-Base_##########################

    conn = sqlite3.connect("Boards.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM " + "'" + board_of + "'" )
    user_data=[]
    for row in cursor.fetchall():
        user_data.append(list(row))

######################_user_data = all the data_###########

    cat=[]
    for i in user_data:
        if i[0] == int(i[0]):
            button_image = PhotoImage(file= r""+i[2])
            temp=[]
            temp.append(i[0])
            temp.append(i[1])
            temp.append(button_image)
            cat.append(temp)

######################_cat = all the categories_###########

    for cat_row in cat:
        newtemp=[]
        for row in user_data:
            if row[0]>cat_row[0] and row[0]<cat_row[0]+1:
                button_image = PhotoImage(file= r""+row[2])
                temp=[]
                temp.append(row[0])
                temp.append(row[1])
                temp.append(button_image)
                newtemp.append(temp)
        cat_row.append(newtemp)

    print("\ncat :\n", cat, "\n\n")

######################_Board print_#####################


    def Board_Start():
        column_index=0
        for cat_num in cat:
            if cat_num[0] == 0:
                c0=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(0))
                c0.grid(column = column_index, row = 0)
                CreateToolTip(c0,cat_num[1])
                column_index+=1
            if cat_num[0] == 1:
                c1=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(1))
                c1.grid(column = column_index, row = 0)
                CreateToolTip(c1,cat_num[1])
                column_index+=1
            if cat_num[0] == 2:
                c2=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(2))
                c2.grid(column = column_index, row = 0)
                CreateToolTip(c2,cat_num[1])
                column_index+=1
            if cat_num[0] == 3:
                c3=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(3))
                c3.grid(column = column_index, row = 0)
                CreateToolTip(c3,cat_num[1])
                column_index+=1
            if cat_num[0] == 4:
                c4=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(4))
                c4.grid(column = column_index, row = 0)
                CreateToolTip(c4,cat_num[1])
                column_index+=1
            if cat_num[0] == 5:
                c5=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(5))
                c5.grid(column = column_index, row = 0)
                CreateToolTip(c5,cat_num[1])
                column_index+=1
            if cat_num[0] == 6:
                c6=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(6))
                c6.grid(column = column_index, row = 0)
                CreateToolTip(c6,cat_num[1])
                column_index+=1
            if cat_num[0] == 7:
                c7=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(7))
                c7.grid(column = column_index, row = 0)
                CreateToolTip(c7,cat_num[1])
                column_index+=1
            if cat_num[0] == 8:
                c8=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(8))
                c8.grid(column = column_index, row = 0)
                CreateToolTip(c8,cat_num[1])
                column_index+=1
            if cat_num[0] == 9:
                c9=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(9))
                c9.grid(column = column_index, row = 0)
                CreateToolTip(c9,cat_num[1])
                column_index+=1
            if cat_num[0] == 10:
                c10=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(10))
                c10.grid(column = column_index, row = 0)
                CreateToolTip(c10,cat_num[1])
                column_index+=1
            if cat_num[0] == 11:
                c11=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(11))
                c11.grid(column = column_index, row = 0)
                CreateToolTip(c11,cat_num[1])
                column_index+=1
            if cat_num[0] == 12:
                c12=Button(BoardEditRoot, image = cat_num[2],command = lambda: category(12))
                c12.grid(column = column_index, row = 0)
                CreateToolTip(c12,cat_num[1])
                column_index+=1


            # Button(BoardEditRoot, image = cat_num[2],command = lambda: category(cat_num)).grid(column = column_index, row = 0)
            # column_index +=1


    def category(cat_info):
        print(cat_info)
        frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
        frame.place(x=0, y=135)
        # print("\n",cat_info,"\n")
            # print(i)
        
        row_index, col_index = 1, 1
        if cat_info==0:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(0))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ת קטגוריה")
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = lambda: Remove(0))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ת קטגוריה")
            c0_B[2] = Button(frame, image = cat[0][3][2][2], command = quit)
            c0_B[2].grid(row = 3, column = 0)
            CreateToolTip(c0_B[2],cat[0][3][2][1])



        if cat_info==1:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(1))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[1][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(1))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[1][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c1_B[i]=Button(frame,image = temp[i][2])
                c1_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c1_B[i],temp[i][1])

        
        if cat_info==2:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(2))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[2][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(2))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[2][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c2_B[i]=Button(frame,image = temp[i][2])
                c2_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c2_B[i],temp[i][1])
                        
        if cat_info==3:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(3))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[3][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(3))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[3][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c3_B[i]=Button(frame,image = temp[i][2])
                c3_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c3_B[i],temp[i][1])
        
        if cat_info==4:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(4))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[4][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(4))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[4][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c4_B[i]=Button(frame,image = temp[i][2])
                c4_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c4_B[i],temp[i][1])
                
        if cat_info==5:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(5))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[5][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(5))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[5][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c5_B[i]=Button(frame,image = temp[i][2])
                c5_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c5_B[i],temp[i][1])
                
        if cat_info==6:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(6))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[6][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(6))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[6][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c6_B[i]=Button(frame,image = temp[i][2])
                c6_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c6_B[i],temp[i][1])
                
        if cat_info==7:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(7))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[7][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(7))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[7][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c7_B[i]=Button(frame,image = temp[i][2])
                c7_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c7_B[i],temp[i][1])
                
        if cat_info==8:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(8))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[8][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(8))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[8][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c8_B[i]=Button(frame,image = temp[i][2])
                c8_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c8_B[i],temp[i][1])
                        
        if cat_info==9:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(9))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[9][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(9))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[9][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c9_B[i]=Button(frame,image = temp[i][2])
                c9_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index += 1
                CreateToolTip(c9_B[i],temp[i][1])
                
        if cat_info==10:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(10))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[10][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(10))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[10][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c10_B[i]=Button(frame,image = temp[i][2])
                c10_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index += 1
                CreateToolTip(c10_B[i],temp[i][1])

        if cat_info==11:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(11))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[11][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(11))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[11][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c11_B[i]=Button(frame,image = temp[i][2])
                c11_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c11_B[i],temp[i][1])

        if cat_info==12:
            frame = Canvas(BoardEditRoot, width=1792, height=555, bg = "SlateGray1")
            frame.place(x=0, y=135)
            temp=[]
            c0_B[0] = Button(frame, image = cat[0][3][0][2], command = lambda: Add(12))
            c0_B[0].grid(row = 1, column = 0)
            CreateToolTip(c0_B[0],cat[0][3][0][1]+"ה ל"+cat[12][1])
            c0_B[1] = Button(frame, image = cat[0][3][1][2], command = print(12))
            c0_B[1].grid(row = 2, column = 0)
            CreateToolTip(c0_B[1],cat[0][3][1][1]+"ה מ"+cat[12][1])
            for i in cat:
                if i[0]==cat_info:
                    temp=i[3]
            for i in range(len(temp)):
                c12_B[i]=Button(frame,image = temp[i][2])
                c12_B[i].grid(row = row_index, column = col_index)
                if col_index == 12:
                    col_index = 1
                    row_index += 1
                else: col_index +=1
                CreateToolTip(c12_B[i],temp[i][1])
        


            # print(87i[3])
        # print("\ncat_info :\n",cat_info[1])
        # def Category_Start():
        #     row_index=0
        #     column_index=0
        #     print("\ncat_info[3] :\n",cat_info[3])
        #     for action in cat_info[3]:
        #         print("\naction[2] :\n",action[2])
        #         Button(frame, image = action[2]).grid(column = column_index, row = row_index)
        #         column_index +=1
        #         if column_index > 8:
        #             column_index = 0
        #             row_index += 1
        # Category_Start()











        # Category_Start()
        # def Category_Start():
        #     for i in specific_cat:
        #         Button(BoardEditRoot, image = i[1]).grid()

        # for row in user_data:
        #     if row[0]>cat_info[0] and row[0]<cat_info[0]+1:
        #         button_image = PhotoImage(file= r""+row[2])
        #         temp=[]
        #         # temp.append(row[0])
        #         temp.append(row[1])
        #         temp.append(button_image)
        #         specific_cat.append(temp)

    
    def Add(cat_info):

        if cat_info == 0:
            if len(cat) == 13:
                messagebox.showerror("שגיאה", "הגעת לכמות קטגוריות מקסימלית")
            else:
                def return_desE():

                    addFile.append(desE.get())
                    conn = sqlite3.connect("Boards.db")
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO  "  + board_of +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (addFile[0], addFile[2], r"" + addFile[1]))
                    conn.commit()
                    descriptionRoot.destroy()
                    BoardEditRoot.destroy()
                    Board_Edit(board_of)

                addFile = []
                addFile.append(len(cat))
                fileAddress = filedialog.askopenfilename(initialdir=r"C:\Users\USER\Desktop\images", title = "בחר תמונה", filetypes = (("png files", "*.png"), ("gif files", "*.gif")))
                addFile.append(fileAddress)
                descriptionRoot = Tk()
                descriptionRoot.geometry("300x100")
                descriptionRoot.title("הכנס תיאור")
                
                desE = Entry(descriptionRoot)
                Label(descriptionRoot).grid(row = 1, column = 2)
                Label(descriptionRoot,width = 7).grid(row = 2, column = 0)
                desE.grid(row = 2, column = 2)
                description = ""
                desB = Button(descriptionRoot, text = "אישור", command = return_desE)
                desB.grid(row = 3, column = 2)
                
                descriptionRoot.mainloop()

        else:

            if len(cat[cat_info][3]) == 48:

                messagebox.showerror("שגיאה", "הגעת לכמות כפתורי ביטוי מקסימלית")

            else:
                def return_desE(): 
                    addFile.append(desE.get())
                    conn = sqlite3.connect("Boards.db")
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO  "  + board_of +  " ('Serial_number', 'Description', 'Image_location') VALUES (?,?,?)", (addFile[0], addFile[2], r"" + addFile[1]))
                    conn.commit()
                    descriptionRoot.destroy()
                    BoardEditRoot.destroy()
                    Board_Edit(board_of)
                
                addFile = []
                addFile.append((len(cat[cat_info][3])+1)*0.01+cat[cat_info][0])
                print(addFile)
                fileAddress = filedialog.askopenfilename(initialdir=r"C:\Users\USER\Desktop\images", title = "בחר תמונה", filetypes = (("png files", "*.png"), ("gif files", "*.gif")))
                addFile.append(fileAddress)
                descriptionRoot = Tk()
                descriptionRoot.geometry("300x100")
                descriptionRoot.title("הכנס תיאור")
                
                desE = Entry(descriptionRoot)
                Label(descriptionRoot).grid(row = 1, column = 2)
                Label(descriptionRoot,width = 7).grid(row = 2, column = 0)
                desE.grid(row = 2, column = 2)
                description = ""
                desB = Button(descriptionRoot, text = "אישור", command = return_desE)
                desB.grid(row = 3, column = 2)
                
                descriptionRoot.mainloop()

    #def Remove(cat_info):



    # def add():
    #     filename = filedialog.askopenfilename(initialdir=r"C:\Users\USER\Desktop\images", title = "Select an image", filetypes = (("png files", "*.png"), ("gif files", "*.gif")))

    # def delete():
    #     return

    # def settings():

    #     column_index=0

    #     frame = Frame(BoardEditRoot, width=1500, height=980)
    #     frame.place(x=0, y=139)
    #     label = Label(frame, width = 0).pack(padx = 1000, pady = 300)
    #     Label(BoardEditRoot).grid()
    #     for i in user_data:
    #         if i[0] > int(i[0]):
    #             print(i[1])
    #             button_image = PhotoImage(file= r""+i[2])
    #             Button(BoardEditRoot,image=button_image).grid(column = column_index, row = 1)
    #             column_index+=1

    Board_Start()
    BoardEditRoot.mainloop()


#Board_Edit("raz")