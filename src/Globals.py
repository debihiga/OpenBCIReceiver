'''
Created on Aug 15, 2018

@author: Debi
'''

from threading import Lock

class LockableFlag():
    
    def __init__(self, value):
        self.mutex = Lock()
        self.flag = value
    
    def set(self, value):
        with self.mutex:
            self.flag = value
            
    def get(self):
        with self.mutex:
            value = self.flag
        return value
            
flag_exit = LockableFlag(False)
flag_marker = LockableFlag(False)