import tkinter as tk
from tkinter import *
from tkinter import ttk
from functools import *

colorA = "#fae8da"
colorB = "#cfd3ca"
colorC = "#9db3b4"
colorD = "#587983"
colorE = "#344b52"

#def date_query(mon_entry, day_entry):

#def booking_insertion(room_id, date,):

def list_available(fr):
    file = open("rooms.txt", "r")
    text = file.read()
    rooms_ls = text.split(';')
    for i in range(len(rooms_ls)-1):
        print(rooms_ls[i])
        rm = Label(fr, text="("+str(i+1)+") "+rooms_ls[i])
        rm.pack(side=TOP, fill=BOTH, padx=10, pady=10)
    

main = tk.Tk()
main.title("Customer Booking Interface")
main.resizable(0,0)
#Main input frame
i = Frame(main)
i.pack(side=RIGHT, fill=BOTH)
i['background']=colorE
#Display frame
d = Frame(main)
d.pack(side=LEFT)
d['background']="white"
#User enters start MM/DD date
lbl = Label(i, text="Start Date",background=colorD, foreground="white")
lbl.pack(side=TOP,fill=X)
inpt = Frame(i)
inpt.pack(side=TOP,anchor=N)
inpt['background']=colorB
ml = Label(inpt, text="MM",background=colorC)
ml.pack(side=LEFT)
mm = Entry(inpt, width=4, background=colorA)
mm.pack(side=LEFT)
dl = Label(inpt, text="DD",background=colorC)
dl.pack(side=LEFT)
dd = Entry(inpt, width=4, background=colorA)
dd.pack(side=LEFT)
#User enters end MM/DD date
lblB = Label(i, text="End Date",background=colorD, foreground="white")
lblB.pack(side=TOP,fill=X)
inptB = Frame(i)
inptB.pack(side=TOP,anchor=N)
inptB['background']=colorB
ml = Label(inptB, text="MM",background=colorC)
ml.pack(side=LEFT)
mm = Entry(inptB, width=4, background=colorA)
mm.pack(side=LEFT)
dl = Label(inptB, text="DD",background=colorC)
dl.pack(side=LEFT)
dd = Entry(inptB, width=4, background=colorA)
dd.pack(side=LEFT)
#Input Number of People
inptP = Frame(i)
inptP.pack(side=TOP,anchor=N)
inptP['background']=colorB
numL = Label(inptP,text="# Of People:  ",background=colorD, foreground="white")
numL.pack(side=LEFT,fill=X)
numE = Entry(inptP, width=4, background=colorA)
numE.pack(side=LEFT)
#Confirm Dates

#Generate List of rooms available in the date selected
#make function that cycles confirm and list button pack
bl = Button(i, text="Show Rooms", command=partial(list_available, d))
bl.pack(side=TOP)
#Confirm selection

            
            

    
    

