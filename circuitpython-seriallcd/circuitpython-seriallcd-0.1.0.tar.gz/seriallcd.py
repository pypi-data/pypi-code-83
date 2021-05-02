# pylint: disable=line-too-long
# SPDX-FileCopyrightText: Copyright (c) 2021 ajs256
#
# SPDX-License-Identifier: MIT
"""
`seriallcd`
================================================================================

CircuitPython helper library for Parallax's serial LCDs


* Author(s): ajs256

Implementation Notes
--------------------

**Hardware:**

* `16x2 Parallax Serial LCD <https://www.parallax.com/product/parallax-2-x-16-serial-lcd-with-piezo-speaker-backlit/>`_
* `20x4 Serial LCD <https://www.parallax.com/product/parallax-4-x-20-serial-lcd-with-piezospeaker-backlit/>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""
# pylint: enable=line-too-long

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/ajs256/CircuitPython_SerialLCD.git"

# Definitions of constants
CURSOR_OFF = 0b10
CURSOR_ON = 0b00

CHARACTER_BLINK = 0b01
NO_BLINK = 0b11

LIGHT_ON = 0b1
LIGHT_OFF = 0b0


def _hex_to_bytes(cmd):
    """
    A helper function to convert a hexadecimal byte to a bytearray.
    """
    return bytes([cmd])


class Display:
    """
    A display.

    :param uart: A ``busio.UART`` or ``serial.Serial`` (on SBCs) object.
    :param bool ignore_bad_baud: Whether or not to ignore baud rates \
    that a display may not support. Defaults to ``False``.

    """

    def __init__(self, uart, *, ignore_bad_baud=False):
        self._display_uart = uart
        try:  # Failsafe if they're using a weird serial object that doesn't have a baud rate object
            if uart.baudrate not in [2400, 9600, 19200] and ignore_bad_baud:
                print(
                    "WARN: Your serial object has a baud rate that the display does not support: ",
                    uart.baudrate,
                    ". Set ignore_bad_baud to True in the constructor to silence this warning.",
                )
        except AttributeError:
            pass

    # Printing

    def print(self, text):
        """
        Standard printing function.

        :param str text: The text to print.

        """
        buf = bytes(text, "utf-8")
        self._display_uart.write(buf)

    def println(self, text):
        """
        Standard printing function, but it adds a newline at the end.

        :param str text: The text to print.

        """
        buf = bytes(text, "utf-8")
        self._display_uart.write(buf)
        self.carriage_return()

    def write(self, data):
        """
        Sends raw data as a byte or bytearray.

        :param data: The data to write.

        """
        self._display_uart.write(data)

    # Cursor manipulation

    def cursor_left(self):
        """
        Moves the cursor left one space. This does not erase any characters.

        """
        self._display_uart.write(_hex_to_bytes(0x08))

    def cursor_right(self):
        """
        Moves the cursor right one space. This does not erase any characters.

        """
        self._display_uart.write(_hex_to_bytes(0x09))

    def line_feed(self):
        """
        Moves the cursor down one line. This does not erase any characters.

        """
        self._display_uart.write(_hex_to_bytes(0x0A))

    def form_feed(self):
        """
        Clears the display and resets the cursor to the top left corner.
        You must pause 5 ms after using this command.

        """
        # Must pause 5 ms after use
        self._display_uart.write(_hex_to_bytes(0x0C))

    def clear(self):
        """
        A more user-friendly name for ``form_feed``. You must pause 5 ms after using this command.

        """
        self.form_feed()

    def carriage_return(self):
        """
        Moves the cursor to position 0 on the next line down.

        """
        self._display_uart.write(_hex_to_bytes(0x0D))

    def new_line(self):
        """
        A more user-friendly name for ``carriage_return``.

        """
        self.carriage_return()

    # Mode setting

    def set_mode(self, cursor, blink):
        """
        Set the "mode" of the display (whether to show the cursor \
        or blink the character under the cursor).

        :param cursor: Whether to show the cursor. Pass in ``seriallcd.CURSOR_ON`` \
            or ``seriallcd.CURSOR_OFF``.
        :param blink: Whether to blink the character under the cursor. Pass \
            in ``seriallcd.CHARACTER_BLINK`` or ``seriallcd.NO_BLINK``

        """
        if cursor == CURSOR_ON and blink == CHARACTER_BLINK:
            self._display_uart.write(_hex_to_bytes(0x19))
        elif cursor == CURSOR_ON and blink == NO_BLINK:
            self._display_uart.write(_hex_to_bytes(0x18))
        elif cursor == CURSOR_OFF and blink == CHARACTER_BLINK:
            self._display_uart.write(_hex_to_bytes(0x17))
        elif cursor == CURSOR_OFF and blink == NO_BLINK:
            self._display_uart.write(_hex_to_bytes(0x16))
        else:
            raise TypeError("Pass in constants for set_mode. See the docs.")

    def set_backlight(self, light):
        """
        Enables or disables the display's backlight.

        :param light: Whether or not the light should be on. Pass in \
            ``seriallcd.LIGHT_ON`` or ``seriallcd.LIGHT_OFF``.

        """
        if light == LIGHT_ON:
            self._display_uart.write(_hex_to_bytes(0x11))
        elif light == LIGHT_OFF:
            self._display_uart.write(_hex_to_bytes(0x12))
        else:
            raise TypeError("Pass in constants for set_backlight. See the docs.")

    def move_cursor(self, row, col):
        """
        Move the cursor to a specific position.

        :param row: The row of the display to move to. Top is 0.
        :param col: The column of the display to move to. Left is 0.

        """
        cmd = _hex_to_bytes(0x80 + (row * 0x14 + col))
        self._display_uart.write(cmd)

    # Custom characters
    def display_custom_char(self, char_id=0):
        """
        Display a custom character.
        :param char_id: The ID of the character to show, from 0 to 7. Defaults to 0.

        """
        cmd = _hex_to_bytes(hex(char_id))
        self._display_uart.write(cmd)

    def set_custom_character(self, char_id, char_bytes):
        """
        Set a custom character.
        :param char_id: The ID of the character to set.
        :param bytes: An array of 8 bytes, one for each row of the display. Use 5 bits for each \
            row. `This <https://www.quinapalus.com/hd44780udg.html>`_ is a great site - \
            make sure to choose "Character size: 5x8".

        """
        start_char = _hex_to_bytes(0xF8 + char_id)
        self._display_uart.write(start_char)
        for byte in char_bytes:
            self._display_uart.write(byte)

    # Music functionality
