#! /usr/bin/env python

from Tkinter import *
from ttk import *
import time

def calculate(*args):
    for i in range (4):
        time.sleep(1)
        print i
        speed.set(i)
    joystick_entry.insert(0, "USB")
    

if __name__ == "__main__":
    root = Tk()
    root.title("Robot Control Interface")
    
    mainframe = Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)
    
    Label(mainframe, text="Joystick").grid(column=1, row=1, sticky=W)
    joystick_entry = Entry(mainframe, width=15)
    joystick_entry.grid(column=2, row=1, sticky=(W, E))
    
    Label(mainframe, text="Bluetooth").grid(column=1, row=2, sticky=W)
    Combobox(mainframe).grid(column=2, row=2, sticky=W)
    
    Label(mainframe, text="Speed").grid(column=1, row=3, sticky=W)
    speed = Scale(mainframe, from_=0, to=6, orient=HORIZONTAL, length=175)
    speed.grid(column=2, row=3, sticky=W)
    
    Button(mainframe, text="Connect", command=calculate).grid(column=3, row=3, sticky=E)
    
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    
    joystick_entry.focus()
    root.bind('<Return>', calculate)
    
    root.mainloop()