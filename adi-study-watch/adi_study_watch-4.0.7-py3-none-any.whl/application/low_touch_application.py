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

from typing import Dict, List

from .common_application import CommonApplication
from ..core import utils
from ..core.enums.common_enums import Application, CommonCommand
from ..core.enums.low_touch_enum import LTCommand
from ..core.packets.common_packets import LibraryConfigReadWritePacket
from ..core.packets.low_touch_packets import ReadCH2CapPacket


class LowTouchApplication(CommonApplication):
    """
    FS Application class.

    .. code-block:: python3
        :emphasize-lines: 4

        from adi_study_watch import SDK

        sdk = SDK("COM4")
        application = sdk.get_low_touch_application()
    """

    def __init__(self, packet_manager):
        super().__init__(Application.LT_APP, packet_manager)

    def read_ch2_cap(self) -> Dict:
        """
        Read the AD7156 CH2 Capacitance in uF.

        :return: A response packet as dictionary.
        :rtype: Dict

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_low_touch_application()
            x = application.read_ch2_cap()
            print(x["payload"]["cap_value"])
            # 0
        """
        packet = ReadCH2CapPacket(self._destination, LTCommand.READ_CH2_CAP_REQ)
        return self._send_packet(packet, LTCommand.READ_CH2_CAP_RES)

    def write_library_configuration(self, fields_values: List[List[int]]) -> Dict:
        """
        Writes library configuration from List of fields and values.

        :param fields_values: List of fields and values to write.
        :type fields_values: List[List[int]]
        :return: A response packet as dictionary.
        :rtype: Dict

        .. list-table::
           :widths: 50 50
           :header-rows: 1

           * - Fields Lower Limit
             - Fields Upper Limit
           * - 0x00
             - 0x03

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_low_touch_application()
            x = application.write_library_configuration([[0x00, 0x1]])
            print(x["payload"]["data"])
            # [['0x0', '0x1']]

        """
        address_range = [0x00, 0x03]
        packet = LibraryConfigReadWritePacket(self._destination, CommonCommand.WRITE_LCFG_REQ)
        packet.set_number_of_operations(len(fields_values))
        utils.check_array_address_range(fields_values, address_range, 2)
        packet.set_write_fields_data(fields_values)
        return self._send_packet(packet, CommonCommand.WRITE_LCFG_RES)

    def read_library_configuration(self, fields: List[int]) -> Dict:
        """
        Reads library configuration from specified field values.

        :param fields: List of field values to read.
        :type fields: List[int]
        :return: A response packet as dictionary
        :rtype: Dict

        .. list-table::
           :widths: 50 50
           :header-rows: 1

           * - Fields Lower Limit
             - Fields Upper Limit
           * - 0x00
             - 0x03

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_low_touch_application()
            x = application.read_library_configuration([0x00])
            print(x["payload"]["data"])
            # [['0x0', '0x0']]
        """
        address_range = [0x00, 0x03]
        packet = LibraryConfigReadWritePacket(self._destination, CommonCommand.READ_LCFG_REQ)
        packet.set_number_of_operations(len(fields))
        utils.check_array_address_range(fields, address_range, 1)
        packet.set_read_fields_data(fields)
        return self._send_packet(packet, CommonCommand.READ_LCFG_RES)

    def set_timeout(self, timeout_value: float) -> None:
        """
        Sets the time out for queue to wait for command packet response.

        :param timeout_value: queue timeout value (in sec).
        :type timeout_value: int
        :return: None

        .. code-block:: python3
            :emphasize-lines: 5

            from adi_study_watch import SDK

            sdk = SDK("COM4")
            application = sdk.get_low_touch_application()
            application.set_timeout(10)

        """
        super().set_timeout(timeout_value)
