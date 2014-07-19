#! /usr/bin/env python

import threading
import traceback
from Controller import Controller

class ControllerThread(threading.Thread):
    
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        '''
        Initialize class attributes.
        '''
        threading.Thread.__init__(self, group=group, target=target, name=name, verbose=verbose)
        self.controller = Controller()
        self.state = True
        
    def stop_communication(self):
        '''
        Change the state to False, this will finish the communication
        cylce.
        '''
        self.state = False
        self.controller.quit_commands()
    
    def run(self):
        '''
        Perform the joystick connection and get the bluetooth list.
        '''
        try:
            while self.state:
                self.controller.send_commands()
        except:
            print str(traceback.format_exc())
