'''
Created on Aug 15, 2018

@author: Debi
'''

import msvcrt

from threading import Thread

import Globals

class ThreadKeyboardEventListener(Thread):
    
    # Overrided
    def run(self):

        print("ThreadKeyboardEventListener started.")
           
        while True:
            
            if(Globals.flag_exit.get()):
                break
                
            char = msvcrt.getch().decode('utf-8')
            if char=="\r":
                print("Enter pressed.")
                Globals.flag_exit.set(True)
            
            
        print("ThreadKeyboardEventListener finished.")