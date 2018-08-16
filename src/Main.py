'''
Created on Aug 15, 2018

@author: Debi
'''
from ThreadOpenBCIReceiver import ThreadOpenBCIReceiver
from ThreadKeyboardEventListener import ThreadKeyboardEventListener
from ThreadStimuliGenerator import ThreadStimuliGenerator
 
def main():

    input("Press ENTER to start.")
    thread_openbci_receiver = ThreadOpenBCIReceiver()
    thread_openbci_receiver.start()
    thread_keyboard_event_listener = ThreadKeyboardEventListener()
    thread_keyboard_event_listener.start()
    thread_stimuli_generator = ThreadStimuliGenerator()
    thread_stimuli_generator.start()
        
if __name__ == "__main__":
    main()