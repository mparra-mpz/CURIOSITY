#! /usr/bin/env python

import unittest
from Joystick import Joystick

class JoystickTest(unittest.TestCase):
    
    def setUp(self):
        '''
        Verify environment is setup properly.
        '''
        self.joystick = Joystick()
        j_list = self.joystick.get_joystick_list()
        self.joystick.connect(j_list[0])
    
    def tearDown(self):
        '''
        Verify environment is tore down properly.
        '''
        self.joystick.disconnect()
        pass
        
    def test_up(self):
        '''
        Verify that the joystick up movement is working without
        problems.
        '''
        self.joystick.clear_commmands()
        print "Move up using the joystick."
        value = False
        while not value:
            self.joystick.get_commands()
            value = self.joystick.commands["UP"]
        self.assertTrue(value)
        
    def test_down(self):
        '''
        Verify that the joystick down movement is working without
        problems.
        '''
        self.joystick.clear_commmands()
        print "Move down using the joystick."
        value = False
        while not value:
            self.joystick.get_commands()
            value = self.joystick.commands["DOWN"]
        self.assertTrue(value)
        
    def test_left(self):
        '''
        Verify that the joystick left movement is working without
        problems.
        '''
        self.joystick.clear_commmands()
        print "Move left using the joystick."
        value = False
        while not value:
            self.joystick.get_commands()
            value = self.joystick.commands["LEFT"]
        self.assertTrue(value)
        
    def test_right(self):
        '''
        Verify that the joystick right movement is working without
        problems.
        '''
        self.joystick.clear_commmands()
        print "Move right using the joystick."
        value = False
        while not value:
            self.joystick.get_commands()
            value = self.joystick.commands["RIGHT"]
        self.assertTrue(value)
        
    def test_speed(self):
        '''
        Verify that the joystick speed command is working without
        problems.
        '''
        self.joystick.clear_commmands()
        print "Speed up using the joystick."
        value = False
        while not value:
            self.joystick.get_commands()
            value = self.joystick.commands["SPEED"]
        self.assertTrue(value)
        
    def test_break(self):
        '''
        Verify that the joystick break command is working without
        problems.
        '''
        self.joystick.clear_commmands()
        print "break using the joystick."
        value = False
        while not value:
            self.joystick.get_commands()
            value = self.joystick.commands["BREAK"]
        self.assertTrue(value)
        
if __name__ == '__main__':
    unittest.main()