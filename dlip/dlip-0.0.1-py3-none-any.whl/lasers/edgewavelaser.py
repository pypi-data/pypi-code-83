import serial
import re
import sys
import time
import traceback
import psutil

from ..utils import accept_strings


DEFAULT_CONFIG = ('COM3', 57600)
GUI_PROCESS = 'EWLaserControlv4.exe'


class EdgewaveLaser:
    
    func_dict = {'read_info': 'Read current laser configuration',
                 'read_state': 'Read the state of the laser (on/off)',
                 'read_trigger': 'Read trigger mode (int/ext)',                 
                 'read_frequency': 'Read internal frequency',
                 'read_power': 'Read the current laser power in %',
                 'read_burst': 'Read the current burst mode',
                 'laser_on': 'Turn on the laser',
                 'laser_off': 'Turn off the laser',
                 'set_trigger_ext': 'Activate external free trigger mode',
                 'set_trigger_int': 'Activate internal free trigger mode',
                 'set_frequency': 'Set internal frequency',
                 'set_power': 'Set the laser power in %',                 
                 'set_burst': 'Set burst mode between 0 and 20',                 
                 'write': 'Issue custom write command to the laser',
                 'read': 'Issue custom read command from the laser',
                 'shutdown': 'Set safe configuration and turn off the laser',
                 'wait_for_laser_warmup': 'Wait for laser warmup',
                 'positioning': 'Set trigger to internal, 1kHz, 30% power and laser on',
                 'full_power': 'Set laser to 90% power and 1kHz'
                 }
               
    def __init__(self, port, baudrate):
        self.port = port
        self.baudrate = baudrate
        self.command_read_reg = re.compile(r'r\d+( \d+)?\r')
        self.command_write_reg = re.compile(r'w\d+( \d+)?\r')

    @staticmethod
    def kill_gui():
        for process in psutil.process_iter():
            try:
                if process.name() == GUI_PROCESS:
                    process.kill()
                    EdgewaveLaser.wait_for_process()
                    break
            except psutil.AccessDenied:
                pass

    @staticmethod
    def wait_for_process():
        while True:
            running = []
            for process in psutil.process_iter():
                try:
                    running.append(process.name())
                except psutil.AccessDenied:
                    pass
            if GUI_PROCESS not in running:
                break

    @classmethod
    def print_help(cls):
        print('Command syntax: laser <command> (<value>)\nPossible commands are:')
        max_len = max([len(command) for command in cls.func_dict.keys()])
        for command, description in cls.func_dict.items():
            print(f'  {command.ljust(max_len)} - {description}')

        
    def connect(self):
        self.connection = serial.Serial(port=self.port, baudrate=self.baudrate,
                                        bytesize=serial.EIGHTBITS,
                                        stopbits=serial.STOPBITS_ONE,
                                        parity=serial.PARITY_NONE, timeout=1)
    
    def disconnect(self):
        self.connection.close()
        
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)
        self.disconnect()

    def laser_on(self):
        state = self.read('r60\r', print_return=False).split('_')[-1].rstrip()
        if state == 'OFF':
            self.set_trigger_ext()
            self.write('w60 1\r')
            wait = 0
            while wait<8:
                print('waiting for startup...')
                time.sleep(0.5)
                wait += 0.5

    def laser_off(self):
        self.write('w60 0\r')
    
    def read_state(self):
        self.read('r60\r')

    @accept_strings
    def set_power(self, power):
        if power <= 100 and power >= 0:
            state = self.read('r178\r', print_return=False)
            if state != 'asd':
                self.write('w178 1\r')
            self.write(f'w175 {power}\r')
    
    def read_power(self):
        self.read('r175\r')

    @accept_strings
    def set_burst(self, burst):
        self.write(f'w233 {burst}\r')
    
    def read_burst(self):
        self.read('r233\r')

    def set_trigger_int(self):
        self.write('w232 0\r')
        self.write('w71 0\r')
        
    def set_trigger_ext(self):
        self.write('w232 0\r')
        self.write('w71 1\r')

    def read_trigger(self):
        self.read('r71\r')

    @accept_strings
    def set_frequency(self, frequency):
        self.write(f'w73 {frequency}\r')

    def read_frequency(self):
        self.read('r73\r')

    def wait_for_laser_warmup(self):
        while True:
            self.connection.write('r91\r'.encode('ascii'))
            response = self.connection.readline().decode('utf-8', 'ignore')
            self.connection.write('w91 101\r')
            time.sleep(1)
            if response == '86':
                print('Waiting for stable oven temperature...')
            elif response == '':
                print('Response none')
                break
            else:
                print('asd')

    def positioning(self):
        self.set_frequency(1000)
        self.set_power('30')
        self.laser_on()
        self.set_trigger_int()

    # only intended for use in 3D-measuring
    def full_power(self):
        self.set_trigger_int()
        self.set_frequency(3000)
        self.set_power(100)
        
    def write(self, command):
        if not command.startswith('w') and not command.endswith('\r'):
            command = f'w{command}\r'
        if self.command_write_reg.search(command) != None:
            self.connection.write(command.encode(encoding='ascii'))
            response = self.connection.readline().decode('utf-8', 'ignore')
            if response.rstrip() == 'OK':
                return
            else:
                print(response)
        else:
            print(command)
            print(r'Write commands must be formatted as "w<number> <number>\r"')
        
    
    def read(self, command, print_return=True):
        if not command.startswith('r') and not command.endswith('\r'):
            command = f'r{command}\r'
        if self.command_read_reg.search(command) != None:
            self.connection.write(command.encode(encoding='ascii'))
            line = self.connection.readline().decode('utf-8', 'ignore')
            if print_return:
                print(line)
            else:
                return line
        else:
            print(r'Read commands must be formatted as "r<number> <number>\r"')

    
    def get_command(self, command_name):
        command = getattr(self, command_name)
        return command

    def read_info(self):
        state = self.read('r60\r', print_return=False).split('_')[-1].rstrip()
        power = self.read('r175\r', print_return=False).split('=')[-1].rstrip()
        burst = self.read('r233\r', print_return=False).split('=')[-1].rstrip()
        trigger = self.read('r71\r', print_return=False).split(' ')[2].upper()
        frequency = str(float(self.read('r73\r', print_return=False).split('=')[-1].split(' ')[-2])/1000) + ' kHz'
        print(f'STATE: {state}\nTRIGGER: {trigger}\nFREQUENCY: {frequency}\nPOWER: {power}\nBURST: {burst}')

    def shutdown(self):
        self.write('w232 0\r')
        self.write('w71 1\r')
        self.write('w233 1\r')
        self.write('w175 0\r')
        self.write('w60 0\r')
        while True:
            state = self.read('r60\r', print_return=False).split('_')[-1].rstrip()
            if state == 'OFF':
                break
        self.read_info()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        if args[0] in EdgewaveLaser.func_dict.keys():
            EdgewaveLaser.kill_gui()
            with EdgewaveLaser('COM3', 57600) as laser:
                command = laser.get_command(args[0])
                if len(args) == 1:
                    command()
                elif len(args) == 2:
                    if args[1].endswith('\\r'):
                        args[1] = bytes(args[1], 'utf-8').decode('unicode-escape')
                    command(args[1])
                elif len(args) > 2:
                    arg = ' '.join(args[1:])
                    if arg.endswith('\\r'):
                        arg = bytes(arg, 'utf-8').decode('unicode-escape')
                    command(arg)
        else:
            print('Invalid command.\nType in "laser" to list possible commands.')
    else:
        EdgewaveLaser.print_help()
