#!/usr/bin/env python
 
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *
 
class MainWindow(QDeclarativeView):
   
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Robotic Control Interface")
        # Renders 'view.qml'
        self.setSource(QUrl.fromLocalFile("Rover.qml"))
        # QML resizes to main window
        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)
        self.rc = self.rootContext()
        
    def set_connection(self, joystick, bluetooth):
        self.rc.setContextProperty("joystick", joystick)
        self.rc.setContextProperty("bluetooth", bluetooth)
        self.rc.setContextProperty("speed", 0)
 
 
from Controller import Controller

if __name__ == "__main__":
    control = Controller()
    joystick_list = control.get_joystick_list()
    joystick = None
    for element in joystick_list:
        if "DragonRise" in element:
            joystick = element
            break
    bluetooth_list = control.get_bluetooth_list()
    bluetooth = None
    for element in bluetooth_list:
        if "CURIOSITY" in element:
            bluetooth = element
            break
    app = QApplication(sys.argv)
    window = MainWindow()
    window.set_connection(joystick, bluetooth)
    window.show()
    sys.exit(app.exec_())