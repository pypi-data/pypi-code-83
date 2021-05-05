import time
import sys
from threading import Thread
from queue import Queue

from . import WinMMWrapper

BUTTONS = {
'BTN_X': 1,
'BTN_A': 2,
'BTN_B': 4,
'BTN_Y': 8,
'BTN_L': 16,
'BTN_R': 32,
'BTN_SELECT': 256,
'BTN_START': 512
}

ARROWS_X = {
    'ARW_RIGHT': 1,
    'ARW_LEFT': -1
}

ARROWS_Y = {
    'ARW_UP': -1,
    'ARW_DOWN': 1,
}

ARROW_VALS = {
    0: -1,
    32511: 0,
    32767: 0,
    65535: 1
}


class Gamepad:

    def __init__(self):
        self.handle = self.get_gamepad_handle()
        self.caps = self.get_caps()
        self.btn_state = {btn: 0 for btn in list(BUTTONS.keys()) 
                          + list(ARROWS_X.keys()) + list(ARROWS_Y.keys())}
        self.is_running = False
        self.event_queue = Queue()
        self.bound_events = {}
        
        self.bind_event('BTN_START_PRESSED', self.stop_reading)

    def get_gamepad_handle(self):
        num = WinMMWrapper.joyGetNumDevs()
        ret, caps, _ = False, None, None
        for handle in range(num):
            ret, caps = WinMMWrapper.joyGetDevCaps(handle)
            if ret:
                print("gamepad detected: " + caps.szPname)
                return handle
        else:
            print("no gamepad detected")
            sys.exit()
            #return False

    def get_caps(self):
        _, caps = WinMMWrapper.joyGetDevCaps(self.handle)
        return caps
    
    def start_reading(self):
        self.is_running = True
        self.t = Thread(target=self.read)
        self.t.daemon = True
        self.t.start()
        self.t.join()
        
    def stop_reading(self):
        self.is_running = False
        print('Stopping reading')
        
    def read(self):
        while self.is_running:
            ret, info = WinMMWrapper.joyGetPosEx(self.handle)
            
            # Record new button states
            state = {btn: btn_code & info.dwButtons for btn, btn_code in BUTTONS.items()}        
            for arw_dict, current_val in zip((ARROWS_X, ARROWS_Y), (info.dwXpos, info.dwYpos)):
                current_val = ARROW_VALS[current_val]
                for btn, val in arw_dict.items():
                    state[btn] = 1 if val == current_val else 0
            
            # Check changes
            for btn in state.keys():
                if state[btn] != self.btn_state[btn]:
                    if state[btn] > self.btn_state[btn]:
                        self.event_queue.put(btn + '_PRESSED')
                    else:
                        self.event_queue.put(btn + '_RELEASED')
                    self.btn_state[btn] = state[btn]
            
            if not self.event_queue.empty():
                self.process_events()
            
            time.sleep(0.05)
            
    def process_events(self):
        while not self.event_queue.empty():
            event = self.event_queue.get()
            if event in self.bound_events:
                self.bound_events[event]()
        
    def bind_event(self, event, func):
        self.bound_events[event] = func

    def release_event(self, event):
        if event in self.bound_events:
            del self.bound_events[event]
        else:
            raise KeyError('Event is unbound')

if __name__ == '__main__':
    gamepad = Gamepad()
    gamepad.start_reading()
            


        

    
