#! /usr/bin/env python

import unittest
import time
from Communication import Communication

class CommunicationTest(unittest.TestCase):
    
    def setUp(self):
        '''
        Verify environment is setup properly.
        '''
        self.controller = Communication()
    
    def tearDown(self):
        '''
        Verify environment is tore down properly.
        '''
        pass
    def test_get_bluetooth_list(self):
        '''
        Verify that the bluetooth list was retrieve without problems.
        '''
        value = False
        b_list = self.controller.get_bluetooth_list()
        if "Empty" not in b_list[0]:
            value = True
        self.assertTrue(value)
        
    def test_send_instruction(self):
        '''
        Verify that the instruction was send without problems.
        '''
        self.controller.connect("CURIOSITY")
        value = self.controller.send_instruction("Hello")
        time.sleep(3)
        self.controller.disconnect()
        self.assertTrue(value)
        
if __name__ == '__main__':
    unittest.main()