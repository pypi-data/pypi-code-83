"""
These classes perform simple operations on pins.
"""
try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO

import logging
from whendo.core.action import Action
from whendo.core.util import Rez

logger = logging.getLogger(__name__)


class SetPin(Action):
    """
    Sets the pin state to HIGH if <on> is True, to LOW otherwise.
    """

    pin: int
    on: bool  # accepts, 0, 1, False, True

    def description(self):
        return f"This action sets pin ({self.pin}) state to ({'GPIO.HIGH' if self.on else 'GPIO.LOW'})."

    def execute(self, tag: str = None, rez: Rez = None):
        flds = self.compute_flds(rez=rez)
        pin = flds["pin"]
        on = flds["on"]
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH if on else GPIO.LOW)
        return self.action_result(result=on, rez=rez, flds=rez.flds if rez else {})


class PinState(Action):
    """
    Returns True if the pin state is HIGH, 0 if the pin state is LOW.
    """

    pin_state: str = "pin_state"  # for Action deserialization
    pin: int

    def description(self):
        return f"This action returns True if the pin state is HIGH, False if LOW."

    def execute(self, tag: str = None, rez: Rez = None):
        flds = self.compute_flds(rez=rez)
        pin = flds["pin"]
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin, GPIO.IN)
        return self.action_result(
            result=GPIO.input(pin) == GPIO.HIGH, rez=rez, flds=rez.flds if rez else {}
        )


class TogglePin(Action):
    """
    Sets the pin state to HIGH if LOW, to LOW if HIGH. Returns True
    if final state is HIGH, False if final state is LOW.
    """

    toggle_pin: str = "toggle_pin"  # for Action deserialization
    pin: int

    def description(self):
        return f"This action sets pin ({self.pin}) state to GPIO.HIGH if LOW, to GPIO.LOW if HIGH. Returns True if final state is HIGH, False if final state is LOW."

    def execute(self, tag: str = None, rez: Rez = None):
        flds = self.compute_flds(rez=rez)
        pin = flds["pin"]
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin, GPIO.OUT)
        state = not GPIO.input(pin)
        GPIO.output(pin, state)
        return self.action_result(
            result=state == GPIO.HIGH, rez=rez, flds=rez.flds if rez else {}
        )


class CleanupPins(Action):
    """
    Clean up the pins. See the docs for GPIO.cleanup().
    """

    cleanup_pins: str = "cleanup_pins"

    def description(self):
        return f"This action executes GPIO.cleanup."

    def execute(self, tag: str = None, rez: Rez = None):
        GPIO.cleanup()
        return self.action_result(result=True, rez=rez, flds=rez.flds if rez else {})
