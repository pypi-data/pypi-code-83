# SPDX-FileCopyrightText: 2021 ajs256
#
# SPDX-License-Identifier: Unlicense

import busio
import board
import seriallcd

uart = busio.UART(board.TX, None, baudrate=9600)

disp = seriallcd.Display(uart)  # Create the display object, passing in the UART.

disp.set_backlight(True)  # Turn on the backlight.
disp.print("Hello CircuitPython!")  # Add some text to the display
