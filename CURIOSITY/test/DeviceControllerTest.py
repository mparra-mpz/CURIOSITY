#! /usr/bin/env python

import unittest
from DeviceController import DeviceController

class DeviceControllerTest(unittest.TestCase):
    
    def setUp(self):
        '''
        Verify environment is setup properly.
        '''
        self.controller = DeviceController()
        self.address = "00:12:12:28:10:49"
        self.instruction = "Hello"
    
    def tearDown(self):
        '''
        Verify environment is tore down properly.
        '''
        pass
    
    def test_get_device_list(self):
        '''
        Verify that the device list was completed without problems.
        '''
        value = self.controller.get_device_list()
        self.assertTrue(value)
        
    def test_connect_device(self):
        '''
        Verify that the device list was completed without problems.
        '''
        value = self.controller.connect_device(self.address)
        self.controller.disconnect_device()
        self.assertTrue(value)
        
    def test_disconnect_device(self):
        '''
        Verify that the device list was completed without problems.
        '''
        self.controller.connect_device(self.address)
        value = self.controller.disconnect_device()
        self.assertTrue(value)
        
    def test_send_instruction(self):
        '''
        Verify that the device list was completed without problems.
        '''
        self.controller.connect_device(self.address)
        value = self.controller.send_instruction(self.instruction)
        self.controller.disconnect_device()
        self.assertTrue(value)
        
if __name__ == '__main__':
    unittest.main()