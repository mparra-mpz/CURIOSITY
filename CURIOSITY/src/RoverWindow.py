#! /usr/bin/env python

from Tkinter import *
from ttk import *
import time
from Controller import Controller
from ControllerThread import ControllerThread

def connect(*args):
    message.set("Set speed and move the Rover")
    c_button["state"] = "disabled"
    q_button["state"] = "enabled"
    controller.initialize_rover_communication(str(box.get()))
    c_thread.set_controller(controller)
    c_thread.setDaemon(True)
    c_thread.start()
    
def disconnect(*args):
    message.set("")
    box.current(0)
    q_button["state"] = "disabled"
    c_thread.stop_communication()
    time.sleep(3)
    while c_thread.isAlive():
        print "Waiting to release the thread."
        time.sleep(1)
    controller.clean_up()

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
    box_value = StringVar()
    box = Combobox(mainframe, textvariable=box_value)
    box.grid(column=2, row=2, sticky=W)
    
    c_button = Button(mainframe, text="Connect", command=connect)
    c_button.grid(column=3, row=2, sticky=E)
    
    message = StringVar()
    Label(mainframe, textvariable=message).grid(column=2, row=3, sticky=W)
    
    q_button = Button(mainframe, text="Disconnect", command=disconnect, state=DISABLED)
    q_button.grid(column=3, row=4, sticky=E)
    
    controller = Controller()
    c_thread = ControllerThread()
    controller.initialize()
    joystick_entry.insert(0, controller.joystick.name)
    
    box["values"] = controller.get_rover_list()
    box.current(0)
    
    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
    
    box.bind("<<ComboboxSelected>>")
    
    root.bind('<Return>', connect)
    
    root.bind('<Return>', disconnect)
    
    
    root.mainloop()