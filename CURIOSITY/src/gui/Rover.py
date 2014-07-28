#!/usr/bin/env python
 
import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *
from Controller import Controller
from ControllerThread import ControllerThread
 
class Rover(QDeclarativeView):
   
    def __init__(self, parent=None):
        '''
        Initialize the attributes class.
        '''
        super(Rover, self).__init__(parent)
        self.setWindowTitle("Robotic Control Interface")
        self.setSource(QUrl.fromLocalFile("Rover.qml"))
        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)
        self.rc = self.rootContext()
        self.ro = self.rootObject()
        
        self.control = Controller()
        self.control_thread = ControllerThread()
        self.joystick = None
        self.bluetooth = None
        
    def set_connection(self):
        '''
        Display the devices selected for the communication.
        '''
        joystick_list = self.control.get_joystick_list()
        for element in joystick_list:
            if "DragonRise" in element:
                self.joystick = element
                break
        self.rc.setContextProperty("joystick", self.joystick)
        
        bluetooth_list = self.control.get_bluetooth_list()
        for element in bluetooth_list:
            if "CURIOSITY" in element:
                self.bluetooth = element
                break
        self.rc.setContextProperty("bluetooth", self.bluetooth)
        
        self.rc.setContextProperty("speed", 0)
        
    def set_event_signal(self):
        '''
        Define the GUI interactions with the system.
        '''
        self.ro.connection.connect(self.__connect_hw)
        self.ro.disconnection.connect(self.__disconnect_hw)
        
    def __connect_hw(self):
        '''
        '''
        self.control.connect(self.joystick, self.bluetooth)
        self.control_thread.start()
        
    def __disconnect_hw(self):
        '''
        '''
        self.control_thread.stop_communication()
        time.sleep(1)
        counter = 0
        while self.control_thread.isAlive() and counter < 15:
            print "Waiting to release the thread."
            counter = counter + 1
            time.sleep(1)
            
        self.control.disconnect()
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Rover()
    window.set_connection()
    window.set_event_signal()
    window.show()
    sys.exit(app.exec_())
