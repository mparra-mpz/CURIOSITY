#!/usr/bin/env python

class SingletonSpeed(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonSpeed, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Speed(object):
    
    __metaclass__ = SingletonSpeed
   
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
        
    def calculate_speed(self, gear):
        '''
        Calculate current speed.
        '''
        self.speed = 20 * gear
        self.notify_observers()
