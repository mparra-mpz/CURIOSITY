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
        self.commands = {}
        self.__reset_commands()
        
    def __reset_commands(self):
        '''
        By the default no movement was command from the joystick.
        '''
        self.commands["UP"] = False
        self.commands["DOWN"] = False
        self.commands["LEFT"] = False
        self.commands["RIGHT"] = False
        self.commands["SPEED"] = False
        self.commands["BREAK"] = False
        
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
        
    def get_commands(self):
        '''
        Return true if the method could read the actions trigger by
        the joystick, return false if any problem appear.
        '''
        try:
            pygame.event.wait()
            axis_x = float(self.joystick.get_axis(0))
            axis_y = float(self.joystick.get_axis(1))
            speed = float(self.joystick.get_button(7))
            brake = float(self.joystick.get_button(6))
            
            self.__reset_commands()
            
            if axis_x > 0.0: self.commands["RIGHT"] = True
            elif axis_x < 0.0: self.commands["LEFT"] = True
            
            if axis_y > 0.0: self.commands["DOWN"] = True
            elif axis_y < 0.0: self.commands["UP"] = True
            
            if speed == 1.0: self.commands["SPEED"] = True
            elif brake ==1.0: self.commands["BREAK"] = True
        except:
            print str(traceback.format_exc())
            return False
        return True
    
    def clear_commmands(self):
        '''
        Remove all the pending commands from the queue.
        '''
        try:
            pygame.event.clear()
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