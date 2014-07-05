#! /usr/bin/env python

from Tkinter import *
from ttk import *

class RoverWindow(Frame):
  
    def __init__(self, parent, width, height):
        Frame.__init__(self, parent)   
        self.parent = parent
        self.width = width
        self.height = height
        self.initUI()
        
    def initUI(self):
        self.parent.title("Rover Control Interface")
        self.pack(fill=BOTH, expand=1)
        self.bluetooth()
        self.center_window()
        
    def center_window(self):
        width = self.parent.winfo_screenwidth()
        height = self.parent.winfo_screenheight()
        x = (width - self.width) / 2
        y = (height - self.height) / 2
        self.parent.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))
        
    def bluetooth(self):
        header = Label(self.parent, text="BLUETOOTH")
        header.grid(row=1,column=1)
        header.pack()
        box = Combobox(self.parent)
        box.grid(row=2,column=1)
        box.pack()
        button = Button(self.parent, text="Connect")
        button.grid(row=1,column=2)
        button.pack()

if __name__ == "__main__":
    root = Tk()
    ex = RoverWindow(root, 700, 500)
    root.mainloop() 