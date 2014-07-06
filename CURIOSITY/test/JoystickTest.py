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
    
    def test_comunication(self):
        '''
        Verify that the joystick communication is working without
        problems.
        '''
        joystick = Joystick()
        value = joystick.connect()        
        value = value and joystick.disconnect()
        self.assertTrue(value)
        
    def test_up(self):
        '''
        Verify that the joystick up movement is working without
        problems.
        '''
        joystick = Joystick()
        joystick.connect()
        joystick.clear_commmands()
        print "Move up using the joystick."
        joystick.get_commands()
        value = joystick.commands["UP"]        
        joystick.disconnect()
        self.assertTrue(value)
        
    def test_down(self):
        '''
        Verify that the joystick down movement is working without
        problems.
        '''
        joystick = Joystick()
        joystick.connect()
        joystick.clear_commmands()
        print "Move down using the joystick."
        joystick.get_commands()
        value = joystick.commands["DOWN"]        
        joystick.disconnect()
        self.assertTrue(value)
        
    def test_left(self):
        '''
        Verify that the joystick left movement is working without
        problems.
        '''
        joystick = Joystick()
        joystick.connect()
        joystick.clear_commmands()
        print "Move left using the joystick."
        joystick.get_commands()
        value = joystick.commands["LEFT"]        
        joystick.disconnect()
        self.assertTrue(value)
        
    def test_right(self):
        '''
        Verify that the joystick right movement is working without
        problems.
        '''
        joystick = Joystick()
        joystick.connect()
        joystick.clear_commmands()
        print "Move right using the joystick."
        joystick.get_commands()
        value = joystick.commands["RIGHT"]        
        joystick.disconnect()
        self.assertTrue(value)
        
    def test_speed(self):
        '''
        Verify that the joystick speed command is working without
        problems.
        '''
        joystick = Joystick()
        joystick.connect()
        joystick.clear_commmands()
        print "Speed up using the joystick."
        joystick.get_commands()
        value = joystick.commands["SPEED"]        
        joystick.disconnect()
        self.assertTrue(value)
        
    def test_break(self):
        '''
        Verify that the joystick break command is working without
        problems.
        '''
        joystick = Joystick()
        joystick.connect()
        joystick.clear_commmands()
        print "break using the joystick."
        joystick.get_commands()
        value = joystick.commands["BREAK"]        
        joystick.disconnect()
        self.assertTrue(value)
        
if __name__ == '__main__':
    unittest.main()