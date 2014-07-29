#!/usr/bin/env python
 
import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import *
from Controller import Controller
from ControllerThread import ControllerThread
from Speed import Speed
 
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
        self.speed = 0.0
        
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
        
        self.rc.setContextProperty("speed", self.speed)
        
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
        self.control.connect(self.joystick, self.bluetooth)
        self.control_thread.start()
        
    def __disconnect_hw(self):
        '''
        Disconnect from the CONTROL software.
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

    def update(self, observer):
        '''
        Method to update the speed.
        '''
        self.speed = observer.speed
        self.rc.setContextProperty("speed", self.speed)


import time
from threading import Thread
tag = True
def loop(speed):
    print "loop"
    while tag:
        speed.calculate_speed()
        print speed.speed
        time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Rover()
    updater = Speed()
    updater.register_observer(window)
    t = Thread(target=loop, args=(updater,))
    t.start()
    window.set_connection()
    window.set_event_signal()
    window.show()
    sys.exit(app.exec_())
    tag = False
