# -*- coding: utf-8 -*- 
"""Created by ssfanli on 2021/05/07 
"""
import wda
import uiautomator2 as u2

from loginhelper import LoginHelper

if __name__ == '__main__':
    deviceid = '00008020-001D1D900CB9002E'
    d = wda.USBClient(deviceid)

    # deviceid = 'abdfde57' # 'abdfde57'     # 'TEV0217315000851'
    # d = u2.connect(deviceid)
    lh = LoginHelper(d, deviceid, 'xxx', 'xxx')
    lh.qqlogin()