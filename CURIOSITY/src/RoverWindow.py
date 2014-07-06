#! /usr/bin/env python

from Tkinter import *
from ttk import *
from Controller import Controller

def control(*args):
    controller.initialize()
    joystick_entry.insert(0, controller.joystick.name)
    message.set("Set speed and move the Rover")
    aux_list = []
    for element in controller.communication.device_list:
        aux_list.append(element.name)
    box["values"] = aux_list
    

if __name__ == "__main__":
    controller = Controller()
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
    box_value = StringVar()
    box = Combobox(mainframe, textvariable=box_value)
    box.grid(column=2, row=2, sticky=W)
    
    Label(mainframe, text="Speed").grid(column=1, row=3, sticky=W)
    speed = Scale(mainframe, from_=0, to=6, orient=HORIZONTAL, length=175)
    speed.grid(column=2, row=3, sticky=W)
    
    Button(mainframe, text="Connect", command=control).grid(column=3, row=3, sticky=E)
    
    message = StringVar()
    Label(mainframe, textvariable=message).grid(column=2, row=4, sticky=W)
    
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    
    root.bind('<Return>', control)
    
    root.mainloop()