#! /usr/bin/env python

import threading
import traceback
from DeviceController import DeviceController

class ControllerThread(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        '''
        Initialize class attributes.
        '''
        threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
        self.controller = None
        self.state = True
    
    def set_controller(self, controller):
        '''
        Set the reference to the controller.
        '''
        self.controller = controller
        
    def stop_communication(self):
        '''
        Change the state to False, this will finish the communication
        cylce.
        '''
        self.state = False
    
    def run(self):
        '''
        Perform the joystick connection and get the bluetooth list.
        '''
        try:
            while self.state:
                self.controller.send_rover_commands()
        except:
            print str(traceback.format_exc())