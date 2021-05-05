from AeroTechAPI import A3200_controller, AxesDict
import AeroTechAPI

from ._gamepad import _gamepad


class Joystick:
    
    def __init__(self, config, speed=25):
        self._init_controller()
        self._config = config
        self._gamepad = _gamepad()
        self.axes = list(self._controller.create_axes(('X', 'Y', 'Z', 'A', 'U')))
        self._speed = speed
        
        self._set_bindings()
        self._axis_bound = 'Z'
        self._current_direction = AxesDict(zip(self.axes, [0 for i in range(len(self.axes))]))

        self._gamepad.start_reading()
              
    def _init_controller(self):
        self._controller = A3200_controller()
        self._controller.connect()
        
    def home_all(self):
        self._controller.home(('X', 'Y', 'Z'))
        
    def _set_bindings(self):
        self._gamepad.bind_event('ARW_UP_PRESSED', lambda: self._start_move(self._config.V_AXIS, self._config.V_UP))
        self._gamepad.bind_event('ARW_UP_RELEASED', lambda: self._stop_move(self._config.V_AXIS))
        self._gamepad.bind_event('ARW_DOWN_PRESSED', lambda: self._start_move(self._config.V_AXIS, self._config.V_DOWN))
        self._gamepad.bind_event('ARW_DOWN_RELEASED', lambda: self._stop_move(self._config.V_AXIS))
        self._gamepad.bind_event('ARW_RIGHT_PRESSED', lambda: self._start_move(self._config.H_AXIS, self._config.H_RIGHT))
        self._gamepad.bind_event('ARW_RIGHT_RELEASED', lambda: self._stop_move(self._config.H_AXIS))
        self._gamepad.bind_event('ARW_LEFT_PRESSED', lambda: self._start_move(self._config.H_AXIS, self._config.H_LEFT))
        self._gamepad.bind_event('ARW_LEFT_RELEASED', lambda: self._stop_move(self._config.H_AXIS))
        self._gamepad.bind_event('BTN_R_PRESSED', lambda: self._start_move('Z', 1))
        self._gamepad.bind_event('BTN_R_RELEASED', lambda: self._stop_move('Z'))
        self._gamepad.bind_event('BTN_L_PRESSED', lambda: self._start_move('Z', -1))
        self._gamepad.bind_event('BTN_L_RELEASED', lambda: self._stop_move('Z'))

        self._gamepad.bind_event('BTN_SELECT_PRESSED', self._change_axes_bindings)
        
        self._gamepad.bind_event('BTN_X_PRESSED', lambda: self._change_speed(self._config.DSPEED_LOW))
        self._gamepad.bind_event('BTN_Y_PRESSED', lambda: self._change_speed(-self._config.DSPEED_LOW))
        self._gamepad.bind_event('BTN_A_PRESSED', lambda: self._change_speed(self._config.DSPEED_HIGH))
        self._gamepad.bind_event('BTN_B_PRESSED', lambda: self._change_speed(-self._config.DSPEED_HIGH))

    def _change_axes_bindings(self):
        if self._axis_bound == 'Z':
            self._axis_bound = 'A'
            self._gamepad.bind_event('BTN_R_PRESSED', lambda: self._start_move(self._config.R_AXIS, self._config.R_UP))
            self._gamepad.bind_event('BTN_R_RELEASED', lambda: self._stop_move(self._config.R_AXIS))
            self._gamepad.bind_event('BTN_L_PRESSED', lambda: self._start_move(self._config.R_AXIS, self._config.R_DOWN))
            self._gamepad.bind_event('BTN_L_RELEASED', lambda: self._stop_move(self._config.R_AXIS))
        elif self._axis_bound == 'A':
            self._axis_bound = 'Z'
            self._gamepad.bind_event('BTN_R_PRESSED', lambda: self._start_move('Z', 1))
            self._gamepad.bind_event('BTN_R_RELEASED', lambda: self._stop_move('Z'))
            self._gamepad.bind_event('BTN_L_PRESSED', lambda: self._start_move('Z', -1))
            self._gamepad.bind_event('BTN_L_RELEASED', lambda: self._stop_move('Z'))
        
    def _start_move(self, axis, direction):
        try:
            self._controller.freerun_start(axis, speed=self._speed * direction)
            self._current_direction[axis] = direction
        except AeroTechAPI.CommandFaultError:
            pass
    
    def _stop_move(self, axis):
        self._controller.freerun_stop(axis)
        self._current_direction[axis] = 0
        
    def _change_speed(self, dspeed):
        new_speed = self._speed + dspeed
        if self._config.SPEED_MIN <= new_speed <= self._config.SPEED_MAX:
            self._speed = new_speed
            for axis, direction in self._current_direction.items():
                if direction != 0:
                    self._start_move(axis, direction) 
        
