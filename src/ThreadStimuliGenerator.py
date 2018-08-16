'''
Created on Aug 15, 2018

@author: Debi
'''

"""
Stimuli generator
1. Wait Te time.
2. Generate initial stimuli (visual or sound, random selection)
3. Wait Ta time.
4. Generate final stimuli (sound)
5. Wait Tt.
6. Repeat N times from step 2.
"""

# Te: establishment time [s] Default: 6s.
Te = 6
# Tsi: wait time after initial stimuli (default: 2s) -> human wait.
# Ta: action duration time (default: 7s).
Ta = 7
# Tt: time between trials (between 4 and 6, random choice) 
Ttmin = 4
Ttmax = 6
# N: number of trials (default: 25)
N_MAX_TRIALS = 25

import time
from threading import Thread

import Globals
import winsound
import random

class ThreadStimuliGenerator(Thread):
    
    # Overrided
    def run(self):
            
        n_trials = 0

        print("ThreadStimuliGenerator started.")
        
        while n_trials<=N_MAX_TRIALS:

            if(Globals.flag_exit.get()):
                break    
            
            # 1. Wait Te time.
            time.sleep(Te)
            if(Globals.flag_exit.get()):
                break  
            
            # 2. Generate initial stimuli (visual or sound, random selection)
            # https://stackoverflow.com/questions/6537481/python-making-a-beep-noise
            print("Action ON")
            winsound.Beep(500, 1500)
            Globals.flag_marker.set(True)
            if(Globals.flag_exit.get()):
                break  
            
            # 3. Wait Ta time.
            time.sleep(Ta)
            if(Globals.flag_exit.get()):
                break  
            
            # 4. Generate final stimuli (sound)
            print("Action OFF")
            winsound.Beep(500, 1500)
            Globals.flag_marker.set(False)
            if(Globals.flag_exit.get()):
                break  

            # 5. Wait Tt.
            Tt = random.randint(Ttmin, Ttmax)
            time.sleep(Tt)
            if(Globals.flag_exit.get()):
                break  

            # 6. Repeat N times from step 2.
            n_trials = n_trials + 1
            
        print("ThreadStimuliGenerator finished.")