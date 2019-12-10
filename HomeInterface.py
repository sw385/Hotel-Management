import tkinter as tk
from tkinter import *
#from tkinter import ttk
from functools import *
import hotel

colorA = "#587795"
colorB = "#ffffff"

master = Tk()
master.title("Hotel Management")
master['background'] = colorA

home = Frame(master)
home.pack(padx=50, pady=30)
home['background'] = "#aaaaaa"

#New Booking
newB = Button(home, width=40, text="New Booking")
newB['background'] = colorB
newB['command'] = hotel.new_book
newB.pack(side=TOP, pady=3, padx=6)

#Update Booking
##upB = Button(home, width=40, text="Update Booking")
##upB['background'] = colorB
##upB['command'] = hotel.update_book
##upB.pack(side=TOP, pady=3, padx=6)

#Cancel Booking
canB = Button(home, width=40, text="Cancel Booking")
canB['command'] = hotel.cancel
canB['background'] = colorB
canB.pack(side=TOP, pady=3, padx=6)

#Show Booking Schedule
showB = Button(home, width=40, text="Show Bookings")
showB['command'] = hotel.show_books
showB['background'] = colorB
showB.pack(side=TOP, pady=3, padx=6)

#Show Earnings (past booking revenues)
earnB = Button(home, width=40, text="Show Earnings")
earnB['command'] = hotel.earnings
earnB['background'] = colorB
earnB.pack(side=TOP, pady=3, padx=6)
