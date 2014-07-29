#!/usr/bin/env python

import random
import time
 
class Speed():
   
    def __init__(self):
        '''
        Initialize the attributes class.
        '''
        self.observers_list = []
        self.speed = 0.0
        
    def register_observer(self, observer):
        '''
        Register a new observer in the notification list.
        '''
        self.observers_list.append(observer)
        
    def remove_observer(self, observer):
        '''
        Remove an observer from the notification list.
        '''
        self.observers_list.remove(observer)
        
    def notify_observers(self):
        '''
        Notify to all the observers a change in the status.
        '''
        for observer in self.observers_list:
            observer.update(self)
        
    def calculate_speed(self):
        '''
        Calculate current speed.
        '''
        self.speed = random.random() * 120
        self.notify_observers()
