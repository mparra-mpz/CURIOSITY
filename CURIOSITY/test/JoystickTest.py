#! /usr/bin/env python

import unittest
from Joystick import Joystick

class JoystickTest(unittest.TestCase):
    
    def setUp(self):
        '''
        Verify environment is setup properly.
        '''
        pass
    
    def tearDown(self):
        '''
        Verify environment is tore down properly.
        '''
        pass
    
    def test_connection(self):
        '''
        Verify that the joystick communication is working without problems.
        '''
        joystick = Joystick()
        value = True
        value = value and joystick.connect()
        print "Press any key in the joystick."
        value = value and joystick.get_commands()
        value = value and joystick.disconnect()
        self.assertTrue(value)
        
if __name__ == '__main__':
    unittest.main()