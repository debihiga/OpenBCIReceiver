'''
Created on Aug 15, 2018

@author: Debi
'''

import socket
import csv
import json
import sys
from threading import Thread

import Globals

UDP_IP = "0.0.0.0"
UDP_PORT = 12347

class ThreadOpenBCIReceiver(Thread):
    
    # Overrided
    def run(self):

        print("ThreadStimuliGenerator started.")
                
        s = socket.socket(socket.AF_INET,           # Internet
                             socket.SOCK_DGRAM)     # UDP
        s.settimeout(5)
        s.bind((UDP_IP, UDP_PORT))
        print("Socket connected to " + UDP_IP + ":" + str(UDP_PORT))
    
        # http://www.pythonforbeginners.com/csv/using-the-csv-module-in-python
        file  = open('output.csv', "wb")
        writer = csv.writer(file, delimiter=',')
    
        while True:
        
            if(Globals.flag_exit.get()):
                break
        
            try:
                data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
                print("received message:" + data)
                j = json.loads(data)
                if(j['type']=="eeg"):
                            
                    eeg = j['data']
                    marker = Globals.flag_marker.get()
                    if(marker):         
                        eeg.append(1)   # ON
                    else:
                        eeg.append(0)   # OFF
                    print(eeg)
                    
                    writer.writerow(eeg)
    
            except:
                print(sys.exc_info()[0])
        
        file.close()