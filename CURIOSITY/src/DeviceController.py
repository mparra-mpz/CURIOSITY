#! /usr/bin/env python

import bluetooth
import traceback

class Device():
    
    def __init__(self, name, address):
        '''
        Initialize class attributes.
        '''
        self.name = name
        self.address = address
            
class DeviceController():
    
    def __init__(self):
        '''
        Initialize class attributes.
        '''
        self.port = 1
        self.device_list = []
        self.sock = None
        
    def get_device_list(self):
        '''
        Return true if the device list was retrieved, if a problem is
        found print the error and return false.
        '''
        try:
            address_list = bluetooth.discover_devices()
            for address in address_list:
                name = str(bluetooth.lookup_name(address))
                auxiliar = Device(name, address)
                self.device_list.append(auxiliar)
        except:
            print str(traceback.format_exc())
            return False
        return True
            
    def connect_device(self, address):
        '''
        Return true if the device accept the connection, if a problem
        is found print the error and return false.
        '''
        try:
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((address, self.port))
        except:
            print str(traceback.format_exc())
            return False
        return True
    
    def disconnect_device(self):
        '''
        Return true if the device accept the disconnection, if a
        problem is found print the error and return false.
        '''
        try:
            self.sock.cloce()
        except:
            print str(traceback.format_exc())
            return False
        return True
            
    def send_instruction(self, instruction):
        ''''
        Return true if the device receive the instruction, if a
        problem is found print the error and return false.
        '''
        try:
            self.sock.send(instruction)
        except:
            print str(traceback.format_exc())
            return False
        return True