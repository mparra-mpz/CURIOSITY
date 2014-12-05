#!/usr/bin/env python

class SingletonDriving(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonDriving, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class Driving(object):
    
    __metaclass__ = SingletonDriving
   
    def __init__(self):
        '''
        Initialize the attributes class.
        '''
        self.observers_list = []
        self.power = 0.0
        self.angle = 0.0
        
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
        
    def set_power(self, gear):
        '''
        Calculate current rover power.
        '''
        self.power = 20 * gear
        self.notify_observers()
        
    def set_angle(self, angle):
        '''
        Calculate current rover rotation.
        '''
        self.angle = angle
        self.notify_observers()