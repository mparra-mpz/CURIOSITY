#! /usr/bin/env python

from Tkinter import *
from ttk import *
import time
from Controller import Controller
from ControllerThread import ControllerThread

class RoverWindow():

    def __init__(self):
        '''
        Initialize class attributes.
        '''
        self.root = Tk()
        self.root.title("Robot Control Interface")
        self.mainframe = None
        self.combo_joystick = None
        self.combo_bluetooth = None
        self.__configure_frame()
        self.root.mainloop()

    def __configure_frame(self):
        '''
        '''
        self.mainframe = Frame(self.root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)
        self.message = StringVar()
        Label(self.mainframe, textvariable=self.message).grid(column=2, row=2, sticky=W)
        self.disconnect_button = Button(self.mainframe, text="Disconnect", command=self.disconnect, state=DISABLED)
        self.speed = StringVar()
        Label(self.mainframe, textvariable=self.speed).grid(column=2, row=4, sticky=W)
        self.disconnect_button.grid(column=3, row=3, sticky=E)
        self.root.bind('<Return>', self.disconnect)
        self.joystick_section()
        self.bluetooth_section()
        for child in self.mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
        self.combo_joystick.current(0)
        self.combo_bluetooth.current(0)

    def joystick_section(self):
        '''
        '''
        Label(self.mainframe, text="Joystick").grid(column=1, row=1, sticky=W)
        value = StringVar()
        self.combo_joystick = Combobox(self.mainframe, textvariable=value)
        self.combo_joystick.grid(column=2, row=1, sticky=(W, E))
        self.combo_joystick["values"] = ["Simulated Joystick", "Real Joystick"]
        self.combo_joystick.bind("<<ComboboxSelected>>")

    def bluetooth_section(self):
        '''
        '''
        Label(self.mainframe, text="Bluetooth").grid(column=1, row=3, sticky=W)
        value = StringVar()
        self.combo_bluetooth = Combobox(self.mainframe, textvariable=value)
        self.combo_bluetooth.grid(column=2, row=3, sticky=W)
        self.combo_bluetooth["values"] = ["Simulated Bluetooth", "Real Bluetooth"]
        self.combo_bluetooth.bind("<<ComboboxSelected>>")
        self.button_bluetooth = Button(self.mainframe, text="Connect", command=self.connect)
        self.button_bluetooth.grid(column=3, row=1, sticky=E)
        self.root.bind('<Return>', self.connect)

    def speed_update(self):
        '''
        '''
        self.speed.set("300 Km/h")

    def connect(self):
        '''
        '''
        print "Joystick: %s" % self.combo_joystick.get()
        print "Bluetooth: %s" % self.combo_bluetooth.get()
        self.message.set("Set speed and move the Rover")
        self.button_bluetooth["state"] = "disabled"
        self.disconnect_button["state"] = "enabled"
        self.speed_update()

    def disconnect(self):
        '''
        '''
        self.message.set("Set speed and move the Rover")
        self.button_bluetooth["state"] = "disabled"
        self.disconnect_button["state"] = "enabled"
        self.message.set("")
        self.combo_joystick.current(0)
        self.combo_bluetooth.current(0)
        self.disconnect_button["state"] = "disabled"


if __name__ == "__main__":
    win = RoverWindow()
