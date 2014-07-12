#! /usr/bin/env python

import traceback
from Joystick import Joystick
from Communication import Device
from Communication import Communication

class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Controller(object):

    __metaclass__ = Singleton

    def __init__(self):
        '''
        Initialize class attributes.
        '''
        self.joystick = Joystick()
        self.communication = Communication()
        self.gear = 0

    def get_joystick_list(self):
        '''
        Return the control joystick list.
        '''
        return self.joystick.get_joystick_list()
            
    def get_bluetooth_list(self):
        '''
        Return the bluetooth communication list.
        '''
        return self.communication.get_bluetooth_list()
    
    def connect(self, joystick_name, bluetooth_name):
        '''
        Initialize the joystick and bluetooth connection.
        '''
        if self.joystick.connect(joystick_name) and \
        self.communication.connect(bluetooth_name):
            return True
        return False

    def disconnect(self):
        '''
        Perform the joystick and bluetooth disconnection.
        '''
        if self.joystick.disconnect() and \
        self.communication.disconnect():
            return True
        return False
            
    def send_commands(self):
        '''
        Read the joystick commands and send it to the rover using a
        bluetooth device.
        '''
        try:
            command = ""
            self.joystick.get_commands()
            if self.joystick.commands["UP"] == True and \
            self.joystick.commands["DOWN"] == False and \
            self.joystick.commands["LEFT"] == False and \
            self.joystick.commands["RIGHT"] == False:
                command = "D1"
                self.communication.send_instruction(command)
            elif self.joystick.commands["UP"] == True and \
            self.joystick.commands["DOWN"] == False and \
            self.joystick.commands["LEFT"] == False and \
            self.joystick.commands["RIGHT"] == True:
                command = "D2"
                self.communication.send_instruction(command)
            elif self.joystick.commands["UP"] == False and \
            self.joystick.commands["DOWN"] == False and \
            self.joystick.commands["LEFT"] == False and \
            self.joystick.commands["RIGHT"] == True:
                command = "D3"
                self.communication.send_instruction(command)
            elif self.joystick.commands["UP"] == False and \
            self.joystick.commands["DOWN"] == True and \
            self.joystick.commands["LEFT"] == False and \
            self.joystick.commands["RIGHT"] == True:
                command = "D4"
                self.communication.send_instruction(command)
            elif self.joystick.commands["UP"] == False and \
            self.joystick.commands["DOWN"] == True and \
            self.joystick.commands["LEFT"] == False and \
            self.joystick.commands["RIGHT"] == False:
                command = "D5"
                self.communication.send_instruction(command)
            elif self.joystick.commands["UP"] == False and \
            self.joystick.commands["DOWN"] == True and \
            self.joystick.commands["LEFT"] == True and \
            self.joystick.commands["RIGHT"] == False:
                command = "D6"
                self.communication.send_instruction(command)
            elif self.joystick.commands["UP"] == False and \
            self.joystick.commands["DOWN"] == False and \
            self.joystick.commands["LEFT"] == True and \
            self.joystick.commands["RIGHT"] == False:
                command = "D7"
                self.communication.send_instruction(command)
            elif self.joystick.commands["UP"] == True and \
            self.joystick.commands["DOWN"] == False and \
            self.joystick.commands["LEFT"] == True and \
            self.joystick.commands["RIGHT"] == False:
                command = "D8"
                self.communication.send_instruction(command)
                
            if self.joystick.commands["SPEED"] == True and self.gear < 6:
                self.gear = self.gear + 1
                command = "V%d" % self.gear
                self.communication.send_instruction(command)
            elif self.joystick.commands["BREAK"] == True and self.gear > 0:
                self.gear = self.gear - 1
                command = "V%d" % self.gear
                self.communication.send_instruction(command)
        except:
            print str(traceback.format_exc())
