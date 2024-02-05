from tkinter import Tk
from tkinter import Label
import time
import sys

master=Tk()
master.title("python digital Clock")

def get_time():
    timeVar= time.strftime("%H:%M:%S %p")
    clock.config(text=timeVar)
    clock.after(200, get_time)
Label(master,font=("Arial",30),text="Digital Clock",fg="red",bg="black").pack()
clock = Label(master, font=("Calibri",90),bg="green",fg="white")
clock.pack()

get_time()
master.mainloop()
