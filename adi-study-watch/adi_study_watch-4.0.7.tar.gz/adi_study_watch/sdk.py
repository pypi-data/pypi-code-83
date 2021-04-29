# ******************************************************************************
# Copyright (c) 2019 Analog Devices, Inc.  All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# - Redistributions of source code must retain the above copyright notice, this
#  list of conditions and the following disclaimer.
# - Redistributions in binary form must reproduce the above copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
# - Modified versions of the software must be conspicuously marked as such.
# - This software is licensed solely and exclusively for use with
#  processors/products manufactured by or for Analog Devices, Inc.
# - This software may not be combined or merged with other code in any manner
#  that would cause the software to become subject to terms and conditions
#  which differ from those listed here.
# - Neither the name of Analog Devices, Inc. nor the names of its contributors
#  may be used to endorse or promote products derived from this software
#  without specific prior written permission.
# - The use of this software may or may not infringe the patent rights of one
#  or more patent holders.  This license does not release you from the
#  requirement that you obtain separate licenses from these patent holders to
#  use this software.
#
# THIS SOFTWARE IS PROVIDED BY ANALOG DEVICES, INC. AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# NONINFRINGEMENT, TITLE, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL ANALOG DEVICES, INC. OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, DAMAGES ARISING OUT OF
# CLAIMS OF INTELLECTUAL PROPERTY RIGHTS INFRINGEMENT; PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ******************************************************************************

import sys
import logging
from typing import List

import serial
import serial.tools.list_ports

from .core.packet_manager import PacketManager
from .application.pm_application import PMApplication
from .application.fs_application import FSApplication
from .application.sqi_application import SQIApplication
from .application.ecg_application import ECGApplication
from .application.eda_application import EDAApplication
from .application.bcm_application import BCMApplication
from .application.ppg_application import PPGApplication
from .application.test_application import TestApplication
from .application.adxl_application import ADXLApplication
from .application.adpd_application import ADPDApplication
from .application.ad7156_application import AD7156Application
from .application.low_touch_application import LowTouchApplication
from .application.pedometer_application import PedometerApplication
from .application.temperature_application import TemperatureApplication

logger = logging.getLogger(__name__)


class SDK:
    """
    SDK class
    """

    def __init__(self, serial_port_address: str, is_ble: bool = False, baud_rate: int = 921600,
                 logging_filename: str = None, threads: int = 10, debug: bool = False, **kwargs):
        """
        Creates an adpd400 application object

        :param serial_port_address: serial port of the device connected
        :param baud_rate: baud rate
        :param **kwargs: other keys and values  for creating serial object
        """

        log_format = '%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s'
        date_format = '%Y-%m-%d %H:%M:%S'
        if logging_filename:
            logging.basicConfig(filename=logging_filename, filemode='a', format=log_format, datefmt=date_format,
                                level=logging.DEBUG)
        else:
            if debug:
                logging.basicConfig(format=log_format, datefmt=date_format, level=logging.DEBUG)
            else:
                logging.basicConfig(format=log_format, datefmt=date_format)
        logger.debug("----- Study Watch SDK Started -----")
        self._serial_object = serial.Serial(serial_port_address, baud_rate, **kwargs)
        self._packet_manager = PacketManager(self._serial_object, number_of_process_threads=threads)
        if is_ble:
            self._packet_manager.set_ble_source()
        else:
            self._packet_manager.set_usb_source()

        self._packet_manager.start_receive_and_process_threads()

    def get_adpd_application(self, callback_function_default=None, args=()):
        """
        Creates an adpd application object

        :param callback_function_default: callback function for all adpd slot stream.
        :type callback_function_default: Callable
        :param args: optional arguments that will be passed back with the callback.
        :returns: an Adpd Application
        :rtype: ADPDApplication
        """
        return ADPDApplication(callback_function_default, self._packet_manager, args)

    def get_adxl_application(self, callback_function=None, args=()):
        """
        Creates an adxl application object

        :param callback_function: callback function for adxl stream
        :type callback_function: Callable
        :param args: optional arguments that will be passed back with the callback.
        :returns: an Adxl Application
        :rtype: ADXLApplication
        """
        return ADXLApplication(callback_function, self._packet_manager, args)

    def get_ecg_application(self, callback_function=None, args=()):
        """
        Creates an ecg application object

        :param callback_function: callback function for ecg stream
        :type callback_function: Callable
        :param args: optional arguments that will be passed back with the callback.
        :returns: an ecg Application
        :rtype: ECGApplication
        """
        return ECGApplication(callback_function, self._packet_manager, args)

    def get_eda_application(self, callback_function=None, args=()):
        """
        Creates an eda application object

        :param callback_function: callback function for eda stream
        :type callback_function: Callable
        :param args: optional arguments that will be passed back with the callback.
        :returns: an eda Application
        :rtype: EDAApplication
        """
        return EDAApplication(callback_function, self._packet_manager, args)

    def get_fs_application(self):
        """
        Creates an fs application object

        :returns: an fs Application
        :rtype: FSApplication
        """
        return FSApplication(self._packet_manager)

    def get_pedometer_application(self, callback_function=None, args=()):
        """
        Creates an pedometer application object

        :param callback_function: callback function for pedometer stream
        :type callback_function: Callable
        :param args: optional arguments that will be passed back with the callback.
        :returns: an pedometer Application
        :rtype: PedometerApplication
        """
        return PedometerApplication(callback_function, self._packet_manager, args)

    def get_pm_application(self):
        """
        Creates an pm application object

        :returns: an pm Application
        :rtype: PMApplication
        """
        return PMApplication(self._packet_manager)

    def get_ppg_application(self, callback_ppg=None, callback_syncppg=None, args_ppg=(), args_syncppg=()):
        """
        Creates an ppg application object

        :param callback_ppg: callback function for ppg stream.
        :type callback_ppg: Callable
        :param callback_syncppg: callback function for sync ppg stream.
        :type callback_syncppg: Callable
        :param args_ppg: optional arguments that will be passed back with ppg callback.
        :param args_syncppg: optional arguments that will be passed back with sync ppg callback.
        :returns: an Ppg Application
        :rtype: PPGApplication
        """
        return PPGApplication(callback_ppg, callback_syncppg, self._packet_manager, args_ppg, args_syncppg)

    def get_temperature_application(self, callback_function=None, args=()):
        """
        Creates a temperature application object

        :param callback_function: callback function for temperature stream
        :type callback_function: Callable
        :param args: optional arguments that will be passed back with the callback.
        :returns: a Temperature Application
        :rtype: TemperatureApplication
        """
        return TemperatureApplication(callback_function, self._packet_manager, args)

    def get_sqi_application(self, callback_function=None, args=()):
        """
        Creates a sqi application object

        :param callback_function: callback function for sqi stream
        :type callback_function: Callable
        :param args: optional arguments that will be passed back with the callback.
        :returns: a SQI Application
        :rtype: SQIApplication
        """
        return SQIApplication(callback_function, self._packet_manager, args)

    def get_bcm_application(self, callback_function=None, args=()):
        """
        Creates a bcm application object

        :param callback_function: callback function for bcm stream
        :type callback_function: Callable
        :param args: optional arguments that will be passed back with the callback.
        :returns: a BCM Application
        :rtype: BCMApplication
        """
        return BCMApplication(callback_function, self._packet_manager, args)

    def get_ad7156_application(self):
        """
        Creates a ad7156 application object

        :returns: a AD7156 Application
        :rtype: AD7156Application
        """
        return AD7156Application(self._packet_manager)

    def get_low_touch_application(self):
        """
        Creates a low touch application object

        :returns: a LowTouch Application
        :rtype: LowTouchApplication
        """
        return LowTouchApplication(self._packet_manager)

    def get_test_application(self, key_test_callback=None, cap_sense_callback=None):
        """
        Creates a test application object, used for internal firmware testing.

        :returns: a Test Application
        :rtype: TestApplication
        """
        return TestApplication(key_test_callback, cap_sense_callback, self._packet_manager)

    def unsubscribe_all_streams(self):
        """
        Unsubscribe from all application streams
        """
        result = [self.get_adxl_application().unsubscribe_stream(), self.get_sqi_application().unsubscribe_stream(),
                  self.get_ppg_application().unsubscribe_stream(), self.get_bcm_application().unsubscribe_stream(),
                  self.get_ecg_application().unsubscribe_stream(), self.get_eda_application().unsubscribe_stream(),
                  self.get_temperature_application().unsubscribe_stream(),
                  self.get_pedometer_application().unsubscribe_stream()]
        test_app = self.get_test_application()
        result.append(test_app.disable_cap_sense_test())
        result.append(test_app.disable_key_press_test())
        adpd_app = self.get_adpd_application()
        fs_app = self.get_adpd_application()
        for stream in adpd_app.get_supported_streams():
            result.append(adpd_app.unsubscribe_stream(stream))
        for stream in fs_app.get_supported_streams():
            result.append(fs_app.unsubscribe_stream(stream))
        return result

    @staticmethod
    def get_available_ports() -> List:
        """
        returns the list of tuple (port, description, hardware_id) of available ports.
        """
        ports = serial.tools.list_ports.comports()
        result = []
        for port, desc, hardware_id in sorted(ports):
            result.append((port, desc, hardware_id))
        return result

    @staticmethod
    def quit():
        """Closes serial port"""
        logger.debug("----- Study Watch SDK Stopped -----")
        sys.exit(0)
