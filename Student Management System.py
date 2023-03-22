#################################################################################Connection of Database
def connectdb():
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('student3_118006.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='blue')
    # -------------------------------------Connectdb Labels

    hostlabel = Label(dbroot, text="Enter Host :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Enter User :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password :", bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    # ---------------------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    # ------------------------------------------ConnectDB to Button
    submitbutton = Button(dbroot, text='Submit', font=('roman', 15, 'bold'), bg='red', bd=5, width=20,
                          activebackground='Blue', activeforeground='white')
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()


#####################################################################################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    data_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' + data_string + "\n" + "Time :" + time_string)
    clock.after(200, tick)


#####################################################################################INTRO SLIDER
import random

colors = ['red', 'green', 'blue', 'yellow', 'pink', 'red2', 'gold2']


def introlabelcolortick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, introlabelcolortick)


def introlabeltick():
    global count, text
    if count >= len(ss):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, introlabeltick)


#############################################################################################################

from tkinter import *
from tkinter import Toplevel
import time

root = Tk()
root.title('Student Managemt System')
root.config(bg='gold2')
root.geometry('1174x600+150+30')
root.iconbitmap('student3_118006.ico')
root.resizable(False, False)
################################################################################# Frames
DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=500)
####################################################################################### Data entry frame

frontLabel = Label(DataEntryFrame, text='------------------Welcome------------------', width=30,
                   font=('arial', 22, 'italic bold'), bg='gold2')
frontLabel.pack(side=TOP, expand=True)

ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=600, y=80, width=550, height=500)
################################################################################## Slider
ss = "Welcome to Student Management System"
count = 0
text = ''
######################################################################################
SliderLabel = Label(root, text=ss, font=('chiller', 30, 'italic bold'), relief=GROOVE, borderwidth=5, width=35,
                    bg='cyan')
SliderLabel.place(x=260, y=0)
introlabeltick()
introlabelcolortick()
#################################################################################Clock
clock = Label(root, font=('times', 14, ' bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0, y=0)
tick()
######################################################################### ConnectDatabaseButton
connectbutton = Button(root, text="Connect To Database", width=23, font=('chiller', 19, 'italic bold'), relief=RIDGE,
                       borderwidth=4, bg='green2',
                       activebackground='Blue', activeforeground='white', command=connectdb)
connectbutton.place(x=930, y=0)

root.mainloop()
