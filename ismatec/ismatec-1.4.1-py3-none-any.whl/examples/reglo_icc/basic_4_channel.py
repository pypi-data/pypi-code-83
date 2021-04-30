import time
import logging
from ismatec.peristaltic_pump import RegloICCFourChannel, ChannelStatus


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    # connect to pump
    port = 'COM8'
    icc = RegloICCFourChannel(port)

    rpm = 1
    for pump_channel in range(4):
        pump_channel = pump_channel + 1
        icc.set_mode_pump_rpm(pump_channel, rpm)
        icc.start(pump_channel)
        time.sleep(2)
        for check_pump_channel in range(4):
            check_pump_channel = check_pump_channel + 1
            if check_pump_channel == pump_channel:
                if icc.channel_status(check_pump_channel) != ChannelStatus.PUMPING:
                    logger.error(f'Failed to start pump channel {check_pump_channel}')
            else:
                if icc.channel_status(check_pump_channel) != ChannelStatus.STOPPED:
                    logger.error(f'Pump channel {check_pump_channel} should be stopped')
        icc.stop(pump_channel)
        time.sleep(2)

    print('done')

