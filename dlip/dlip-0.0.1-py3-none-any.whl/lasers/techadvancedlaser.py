import sys
import serial
import time

from utils import accept_strings

PORT = 'COM4'


class TechAdvancedLaser:
    
    func_dict = {'laser_on': 'Turns the laser on',
                 'laser_off': 'Turns the laser off',
                 'set_trigger_ext': 'Sets the triggering mode to external',
                 'set_trigger_int': 'Sets the triggering mode to internal',
                 'set_power': 'Sets the laser power (%)',
                 'set_frequency': 'Sets the laser frequency (Hz)',
                 'read_laser': 'Reads the laser state',
                 'read_trigger': 'Reads the registered triggering mode',
                 'read_info': 'Reads laser state and trigger mode',
                 'positioning': 'Laser on, trigger int, power to 50%',
                 'shutdown': 'Laser off, trigger, power 0%'}
    
    def __init__(self, port, baudrate=4800, bytesize=8, 
                 parity='N', stopbits=1, timeout=0):
        self.port = port
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout
        
    def __enter__(self):
        self.connect()
        return self
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.disconnect()
        
    def connect(self):
        self.connection = serial.Serial(port=self.port, 
                                        baudrate=self.baudrate, 
                                        bytesize=self.bytesize, 
                                        parity=self.parity, 
                                        stopbits=self.stopbits, 
                                        timeout=self.timeout)
        
    def disconnect(self):
        self.connection.close()
    
    def get_method(self, method):
        if method in self.func_dict.keys():
            return getattr(self, method)
        
    @classmethod
    def print_help(cls):
        print('Use one of the following commands:\n')
        for func, description in cls.func_dict.items():
            print(f'{func}\t-\t{description}')
    
    def laser_on(self):
        command = b'\x83\x01'
        self.connection.write(command)
    
    def laser_off(self):
        command = b'\x83\x00'
        self.connection.write(command)
    
    def set_trigger_ext(self):
        command = b'\x9E\x01'
        self.connection.write(command)
    
    def set_trigger_int(self):
        command = b'\x9E\x00'
        self.connection.write(command)
    
    def read_trigger(self, print_=True):
        command = b'\x1E'
        self.connection.write(command)
        ret = int.from_bytes(self.receive(), 'little')
        if ret:
            state = "TRIGGER_EXT"
        else:
            state = "TRIGGER_INT"
        if print_:
            print(state)
        else:
            return state

    def read_info(self):
        self.read_laser()
        self.read_trigger()
    
    def read_laser(self, print_=True):
        command = b'\x05'
        self.connection.write(command)
        ret = int.from_bytes(self.receive(), 'little')
        if ret:
            state = "LASER_ON"
        else:
            state = "LASER_OFF"
        if print_:
            print(state)
        else:
            return state

    @accept_strings
    def set_frequency(self, frequency):
        upper_byte, lower_byte  = list(map(int, divmod(frequency / 10, 256)))
        command_lower_byte = bytes([0x97, lower_byte])
        command_upper_byte = bytes([0x98, upper_byte])
        self.connection.write(command_lower_byte)
        self.connection.write(command_upper_byte)

    @accept_strings
    def set_power(self, power):
        power_byte = int(power * 2.55)
        command = bytes([0x80, power_byte])
        self.connection.write(command)

    def positioning(self):
        self.laser_on()
        time.sleep(0.2)
        self.set_trigger_int()
        time.sleep(0.2)
        self.set_frequency(1000)
        time.sleep(0.2)
        self.set_power(50)

    def shutdown(self):
        self.set_power(0)
        self.set_trigger_ext()
        self.laser_off()

    def read_actual_power(self):
        command_upper_byte = b'\x08'
        command_lower_byte = b'\x09'
        self.connection.write(command_upper_byte)
        upper_byte = self.receive()
        self.connection.write(command_lower_byte)
        lower_byte = self.receive()
        reading = int.from_bytes(upper_byte + lower_byte, byteorder='big')
        return reading
        
        
    def receive(self):
        while True:
            ret = self.connection.readline()
            if ret != b'':
                break
        return ret
        
if __name__ == '__main__':
    with TechAdvancedLaser(PORT) as laser:
        if len(sys.argv) == 1:
            laser.print_help()
        else:
            args = sys.argv[1:]
            command = laser.get_method(args[0])
            command(*args[1:])
            
    
    
