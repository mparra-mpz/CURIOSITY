#! /usr/bin/env python

import traceback
from Joystick import Joystick
from DeviceController import DeviceController
from DeviceController import Device

class Controller():
    
    def __init__(self):
        '''
        Initialize class attributes.
        '''
        self.joystick = Joystick()
        self.communication = DeviceController()
        self.gear = 0
        
    def initialize(self):
        '''
        Perform the joystick connection and get the bluetooth list.
        '''
        try:
            self.joystick.connect()
            self.communication.get_device_list()
        except:
            print str(traceback.format_exc())
            
    def clean_up(self):
        '''
        Perform the joystick and bluetooth disconnection.
        '''
        try:
            self.joystick.disconnect()
            self.communication.disconnect_device()
        except:
            print str(traceback.format_exc())
            
    def get_rover_list(self):
        '''
        Return the bluetooth communication list.
        '''
        try:
            blue_list = ["None"]
            for device in self.communication.device_list:
                blue_list.append(device.name)
            return blue_list
        except:
            print str(traceback.format_exc())
            return None
    
    def initialize_rover_communication(self, name):
        '''
        Initialize the bluetooth communication.
        '''
        try:
            for element in self.communication.device_list:
                if name == element.name:
                    device = element
                    break
            self.communication.connect_device(device.address)
        except:
            print str(traceback.format_exc())
            
    def send_rover_commands(self):
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