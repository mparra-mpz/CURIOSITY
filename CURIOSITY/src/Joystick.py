#! /usr/bin/env python

import pygame
import traceback
            
class Joystick():
    
    def __init__(self):
        '''
        Initialize class attributes.
        '''
        self.joystick = None
        self.name = ""
        self.axis_x = 0.0
        self.axis_y = 0.0
        self.speed_up = 0.0
        self.brake = 0.0
        
    def connect(self):
        '''
        Return true if you can connect to the joystick, return false
        if any problem appear.
        '''
        try:
            pygame.init()
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
            self.name = self.joystick.get_name()
        except:
            print str(traceback.format_exc())
            return False
        return True
        
    def get_action(self):
        '''
        Return true if the method could read the actions trigger by
        the joystick, return false if any problem appear.
        '''
        try:
            pygame.event.wait()
            self.axis_x = float(self.joystick.get_axis(0))
            self.axis_y = float(self.joystick.get_axis(1))
            self.speed_up = float(self.joystick.get_button(7))
            self.brake = float(self.joystick.get_button(6))
        except:
            print str(traceback.format_exc())
            
    def disconnect(self):
        '''
        Return true if the disconnection is successful, return false
        if any problem appear.
        '''
        try:
            pygame.quit()
        except:
            print str(traceback.format_exc())
            return False
        return True