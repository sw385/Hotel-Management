import tkinter as tk
from tkinter import *
#from tkinter import ttk
from functools import *

colorA = "#587795"
colorB = "#ffffff"

def cancel_book(entry):
    nm = entry.get()
    print(nm)
    #delete from Bookings where CustomerIDNum=(select CustomerIDNum from Customers where Name=NAME);
    #delete from Customers where Name=NAME;

#def update_booking():
    #Same as new booking but overrides columns corresponding to primary key from name

def monthly(cnvs, lst, lclst):
    cnvs.delete("all")
    cnvs.create_text(250,10,text="Monthly Earnings")
    cnvs.create_line(20,180,480,180)
    cnvs.create_line(20,20,20,180)
    for i in range(len(lst)):
        x = (40 * (i))+40
        color = "#82bfde"
        if(lst[i]==min(lst)):
            color = "#e48377"
        if(lst[i]==max(lst)):
            color = "#70e854"
        cnvs.create_text(x, 190, text=str(i+1))
        cnvs.create_rectangle(x-10, 180, x+10, 180-(lst[i]/20), fill=color)
        cnvs.create_text(x, 172-(lst[i]/20), text=str(lst[i]))
    for i in range(len(lclst)):
        x = (40 * (i))+40
        color = "#ff551a"
        cnvs.create_rectangle(x, 180, x+10, 180-(lclst[i]/20), fill=color)

def quarterly(cnvs, lst, lclst):
    #Add query for cost by quarter and add half column over top of revenue bars
    cnvs.delete("all")
    cnvs.create_text(250,10,text="Quarterly Earnings")
    cnvs.create_line(20,180,480,180)
    cnvs.create_line(20,20,20,180)
    for i in range(len(lst)):
        x = (120 * (i))+70
        color = "#82bfde"
        if(lst[i]==min(lst)):
            color = "#e48377"
        if(lst[i]==max(lst)):
            color = "#70e854"
        cnvs.create_text(x, 190, text=str(i+1))
        r = cnvs.create_rectangle(x-40, 180, x+40, 180-(lst[i]/30), fill=color)
        cnvs.create_text(x, 172-(lst[i]/30), text=str(lst[i]))
    for i in range(len(lst)):
        x = (120 * (i))+70
        color = "#ff551a"
        r = cnvs.create_rectangle(x, 180, x+40, 180-(lclst[i]/30), fill=color)
       

def earnings():
    g = Tk()
    g.title("Earnings")
    #g.resizeable(0,0)
    c = Canvas(g, width=500, height=200)
    c['background']=colorB
    c.pack(side=LEFT)
    f = Frame(g, width=50, height=200)
    f['background']=colorA
    f.pack(side=LEFT, fill=BOTH)
    l = Label(f, text="Generate Report", background=colorA, foreground=colorB)
    l.pack(side=TOP)
    m = Button(f, text="Monthly", width=10)

    la = [157,265,1087,1094,1016,1762,315,372,1065,138,1053,0]
    lac = [352,379,501,368,358,348,308,346,453,379,379,379]
           
    m['command'] = partial(monthly, c, la, lac)
    m.pack(side=TOP, padx=5, pady=1)
    q = Button(f, text="Quarterly", width=10)
    
    lb = [1510,3873,1752,1191]
    lbc = [1232,1073,1107,1138]

    q['command'] = partial(quarterly, c, lb, lbc)
    q.pack(side=TOP, padx=5)
    #Join room numbers with prices
    #select Rooms.RoomIDNum, A.Price from Rooms join (select * from RoomClasses)A on Rooms.TypeID=A.TypeIDNum;   
    #Number of days for booking
    #select BookingIDNum, DATEDIFF(CheckOut,CheckIn) Days from Bookings;
    #Total revenues from each booking
    #select BookingIDNum, DATEDIFF(CheckOut,CheckIn) Days, C.Price Rate, (C.Price*DATEDIFF(CheckOut,CheckIn)) Total from Bookings join (select Rooms.RoomIDNum, A.Price from Rooms join (select * from RoomClasses)A on Rooms.TypeID=A.TypeIDNum) C on Bookings.RoomIDNum=C.RoomIDNum;
    #Total revenues by month
##select month(B.CheckIn) Month, AVG(B.Days) Average_Days, SUM(B.Total) Total_Earnings from
##(select
##BookingIDNum, CheckIn, DATEDIFF(CheckOut,CheckIn) Days, C.Price Rate, (C.Price*DATEDIFF(CheckOut,CheckIn)) Total
##from
##Bookings
##join
##(select Rooms.RoomIDNum, A.Price from Rooms join (select * from RoomClasses)A on Rooms.TypeID=A.TypeIDNum) C
##on Bookings.RoomIDNum=C.RoomIDNum) B 
##group by month(B.CheckIn);
##select quarter(B.CheckIn), AVG(B.Days), SUM(B.Total)
##from
##(select BookingIDNum, CheckIn, DATEDIFF(CheckOut,CheckIn) Days, C.Price Rate, (C.Price*DATEDIFF(CheckOut,CheckIn)) Total
## from Bookings
## join (select Rooms.RoomIDNum, A.Price from Rooms
##       join (select * from RoomClasses)A on Rooms.TypeID=A.TypeIDNum) C
## on Bookings.RoomIDNum=C.RoomIDNum) B
##group by quarter(B.CheckIn);

def cancel():
    #Delete booking
    w = Tk()
    w.title("Cancellation")
    w['background']=colorA
    d = Frame(w)
    d.pack(pady=20,padx=20)
    f = Frame(d)
    f.pack(side=TOP)
    lbl = Label(f, text="Enter Name: ")
    lbl.pack(side=LEFT)
    en = Entry(f, width=20)
    en.pack(side=LEFT)
    b = Frame(d)
    b.pack(side=TOP, fill=X)
    bt = Button(b, text="Cancel Booking")
    bt.pack(fill=X)
    bt['command'] = partial(cancel_book, en)

   
def list_rooms(lst, lstbx, sm, sd, em, ed, but):
    start_m = sm.get()
    start_d = sd.get()
    end_m = em.get()
    end_d = ed.get()
    lstbx.delete(0,END)
    #Query
    #select B.BookingIDNum, B.RoomIDNum, C.Name, B.CheckIn, DATEDIFF(B.Checkout, CheckIn) Days from Bookings B join Customers C on B.CustomerIDNum=C.CustomerIDNum;.
    lst = ["1 | Twin | Shower | $22.95", "2 | Queen | Shower | $33.50", "3 | Queen | Shower + Tub | $52.50", "3 | King | Shower + Jacuzzi Tub | $75.95"]
    file = open("rooms.txt", "w")
    lst_str = ""
    for i in range(len(lst)):
        lst_str += lst[i]+","
    lst_str += "\n"+start_m+","+start_d+","+end_m+","+end_d
    file.write(lst_str)
    file.close()
    #Loop insert into listbox
    for i in range(len(lst)):
        lstbx.insert(END, lst[i])
    but.pack(side=BOTTOM, pady=2, padx=2, fill=X)

def select(lstbx, NAME, CCNUM, SEC, EXPM, EXPD, SDATEM, SDATED, EDATEM, EDATED, GNUM):
    file = open("rooms.txt", "r")
    file_str = file.read()
    ls = file_str.split(",")
    print(ls[int(lstbx.curselection()[0])])
    #Insert new customer
    #"insert into Customers (Name, CreditCardNum, SecCode, ExpDate) values ("+NAME+", "+CCNUM+", "+SEC+", "+EXP+");"
    #Choose available room number from room type selected
    #"select RoomIDNum from Rooms where RoomIDNum not in (select RoomIDNum from Bookings where (month(CheckIn) between 2 and 3) and (day(CheckIn) between 10 and 20)) and TypeID=TYPE limit 1;"
    #Insert new booking with newly generated customer id
    #insert into Bookings (CustomerIDNum, RoomIDNum, CheckIn, CheckOut, Guests) values (
    #(select CustomerIDNum from Customers where Name=NAME),
    #(select RoomIDNum from Rooms where RoomIDNum not in (select RoomIDNum from Bookings where (month(CheckIn) between 2 and 3) and (day(CheckIn) between 10 and 20)) and TypeID=TYPE limit 1),
    #SDATE, EDATE, GNUM);
    #####
    #insert into Bookings (CustomerIDNum, RoomIDNum, CheckIn, CheckOut, Guests) values ( (select CustomerIDNum from Customers where Name="Joe Smith"), (select RoomIDNum from Rooms where RoomIDNum not in (select RoomIDNum from Bookings A where (month(CheckIn) between 2 and 3) and (day(CheckIn) between 10 and 20)) and TypeID=1 limit 1), '2019-04-20','2019-04-22',2);
    
    

def new_book():
    book = Tk()
    book.title("Book Room")

    inpt = Frame(book, width=200, height=200)
    inpt['background'] = colorA
    inpt.pack(side=RIGHT, anchor=E, fill=BOTH)

    d = Frame(book, width=300, height=200)
    d['background'] = colorB
    d.pack(side=LEFT, anchor=W, fill=BOTH)
    
    #Input Dates
    i = Frame(inpt, width=200)
    i['background'] = colorA
    i.pack(side=TOP, fill=X)
    dtLbl = Label(i,text='Check-In Date (MM/DD): ')
    dtLbl['background'] = colorA
    dtLbl['foreground'] = colorB
    dtLbl.pack(side=LEFT)
    day = Entry(i, width=4)
    day.pack(side=RIGHT)
    mon = Entry(i, width=4)
    mon.pack(side=RIGHT)
    j = Frame(inpt, width=200)
    j['background'] = colorA
    j.pack(side=TOP, fill=X)
    edtLbl = Label(j,text='Check-Out Date (MM/DD): ')
    edtLbl['background'] = colorA
    edtLbl['foreground'] = colorB
    edtLbl.pack(side=LEFT)
    eday = Entry(j, width=4)
    eday.pack(side=RIGHT)
    emon = Entry(j, width=4)
    emon.pack(side=RIGHT)
    #Number Guests
    ng = Frame(inpt, width=200)
    ng['background'] = colorA
    ng.pack(side=TOP, fill=X)
    ngLbl = Label(ng,text='Number of Guests: ')
    ngLbl['background'] = colorA
    ngLbl['foreground'] = colorB
    ngLbl.pack(side=LEFT)
    eng = Entry(ng, width=4)
    eng.pack(side=RIGHT)
    #Show available rooms
    #select TypeID from (select * from Rooms where RoomIDNum not in (select RoomIDNum from Bookings where (month(CheckIn) between 2 and 3) and (day(CheckIn) between 10 and 20)))A group by TypeID;
    #select * from RoomClasses R join (select TypeID from (select * from Rooms where RoomIDNum not in (select RoomIDNum from Bookings where (month(CheckIn) between 2 and 3) and (day(CheckIn) between 10 and 20)))A group by TypeID)B on R.TypeIDNum=B.TypeID;
    #"select TypeID from (select * from Rooms where RoomIDNum not in (select RoomIDNum from Bookings where (month(CheckIn) between "+str(start_m)+" and "+str(end_m)+") and (day(CheckIn) between "+str(start_d)+" and "+str(end_d)+")))A group by TypeID;"
    rooms_ls = list()
    #Button
    showB = Button(inpt, text="Show Availability", relief=GROOVE, borderwidth=4)
    showB['background'] = colorB
    showB.pack(side=TOP, fill=X)
    #Display
    rooms = Listbox(d, width=50, height=20)
    rooms.pack(fill=BOTH)
    #Select Room
    selB = Button(inpt, text="Select Room", relief=GROOVE, borderwidth=4)
    selB['background'] = colorB


    showB['command'] = partial(list_rooms, rooms_ls, rooms, mon, day, emon, eday, selB)
    
    #Input client info
    #Name
    n = Frame(inpt, width=200)
    n['background'] = colorA
    n.pack(side=TOP, fill=X)
    nLbl = Label(n,text='Name: ')
    nLbl['background'] = colorA
    nLbl['foreground'] = colorB
    nLbl.pack(side=LEFT)
    name = Entry(n, width=25)
    name.pack(side=RIGHT)
    #Card No
    cn = Frame(inpt, width=200)
    cn['background'] = colorA
    cn.pack(side=TOP, fill=X)
    cnLbl = Label(cn,text='Card No. (16 dgts): ')
    cnLbl['background'] = colorA
    cnLbl['foreground'] = colorB
    cnLbl.pack(side=LEFT)
    cname = Entry(cn, width=25)
    cname.pack(side=RIGHT)
    #Security Code
    cd = Frame(inpt, width=200)
    cd['background'] = colorA
    cd.pack(side=TOP, fill=X)
    cdLbl = Label(cd,text='Security Code (4 dgts): ')
    cdLbl['background'] = colorA
    cdLbl['foreground'] = colorB
    cdLbl.pack(side=LEFT)
    code = Entry(cd, width=9)
    code.pack(side=RIGHT)
    #Expiration date
    c = Frame(inpt, width=200)
    c['background'] = colorA
    c.pack(side=TOP, fill=X)
    cLbl = Label(c,text='Card Expiration Date (MM/DD): ')
    cLbl['background'] = colorA
    cLbl['foreground'] = colorB
    cLbl.pack(side=LEFT)
    expM = Entry(c, width=4)
    expM.pack(side=RIGHT)
    expD = Entry(c, width=4)
    expD.pack(side=RIGHT)

    selB['command'] = partial(select, rooms, name, cname, code, expM, expD, mon, day, emon, eday, eng)
    

def show_books():
    books = Tk()
    books.title("Bookings")
    
    #Query bookings
    ls = ["Room 1", "Room 2", "Room 3"]
    for i in range(len(ls)):
        Label(books, borderwidth=4, width=80, text=ls[i]).pack(side=TOP)
