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
        self.set_default_values()
        self.setSource(QUrl.fromLocalFile("Rover.qml"))
        self.setResizeMode(QDeclarativeView.SizeRootObjectToView)
        self.ro = self.rootObject()
        
        self.control = Controller()
        self.control_thread = ControllerThread()
        self.control_start = False
        
    def set_default_values(self):
        '''
        Set the default values to start the GUI.
        '''
        self.joystick = ""
        self.bluetooth = ""
        self.power = 0.0
        self.angle = 0.0
        self.rc = self.rootContext()
        self.rc.setContextProperty("joystick", self.joystick)
        self.rc.setContextProperty("bluetooth", self.bluetooth)
        self.rc.setContextProperty("power", self.power)
        self.rc.setContextProperty("angle", self.angle)
        
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
        
    def set_event_signal(self):
        '''
        Define the GUI interactions with the system.
        '''
        self.ro.connection.connect(self.__connect_hw)
        self.ro.disconnection.connect(self.__disconnect_hw)
        
    def __connect_hw(self):
        '''
        Connect to the CONTROL software.
        '''
        if not self.control_start:
            self.control_start = True
            self.control.connect(self.joystick, self.bluetooth)
            self.control_thread.start()
        
    def __disconnect_hw(self):
        '''
        Disconnect from the CONTROL software.
        '''
        self.control_thread.stop_communication()
        time.sleep(1)            
        self.control.disconnect()
        time.sleep(1)
        sys.exit(0)

    def update(self, observer):
        '''
        Method to update values in the GUI.
        '''
        self.power = observer.power
        self.rc.setContextProperty("power", self.power)
        self.angle = observer.angle
        self.rc.setContextProperty("angle", self.angle)
        
        
from Driving import Driving

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Rover()
    updater = Driving()
    updater.register_observer(window)
    window.set_connection()
    window.set_event_signal()
    window.show()
    sys.exit(app.exec_())