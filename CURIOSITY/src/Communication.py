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
            
class Communication():
    
    def __init__(self):
        '''
        Initialize class attributes.
        '''
        self.port = 1
        self.bluetooth_list = []
        self.sock = None
        
    def get_bluetooth_list(self):
        '''
        Return the bluetooth name list retrieve by the computer, if a
        problem is found print the error and return None
        '''
        try:
            tmp_list = []
            address_list = bluetooth.discover_devices()
            for address in address_list:
                name = str(bluetooth.lookup_name(address))
                auxiliar = Device(name, address)
                self.bluetooth_list.append(auxiliar)
                tmp_list.append(name)
        except:
            print str(traceback.format_exc())
        if len(tmp_list) == 0:
            tmp_list.append("--- Empty ---")
        return tmp_list
            
    def connect(self, bluetooth_name):
        '''
        Return true if the device accept the connection, if a problem
        is found print the error and return false.
        '''
        try:
            address = "-1"
            for element in self.bluetooth_list:
                if element.name == bluetooth_name:
                    address = element.address
            self.sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            self.sock.connect((address, self.port))
        except:
            print str(traceback.format_exc())
            return False
        return True
    
    def disconnect(self):
        '''
        Return true if the device accept the disconnection, if a
        problem is found print the error and return false.
        '''
        try:
            self.sock.close()
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
