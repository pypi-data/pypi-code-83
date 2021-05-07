# -*- coding: utf-8 -*-
"""
@Author: Ssfanli
@Time  : 2021/04/20 8:46 下午
@Desc  :
"""
import os
import tempfile
import time
import typing
from functools import wraps

import wda
import uiautomator2 as u2
from loguru import logger

from loginhelper.const import *


class BaseDevice(object):

    def __init__(self, device_id: str):
        self.did = device_id

    def checker(func):
        """parameters checker"""

        @wraps(func)
        def wrapper(self, **kwargs):
            plt = kwargs.get('platform')
            wch = kwargs.get('which')
            if plt:
                assert plt in COMMON.PLATFORMS
            if wch:
                assert wch in COMMON.APPS
            return func(self, **kwargs)

        return wrapper

    @staticmethod
    def _exec(cmd: str):
        logger.debug(f'exec_cmd: {cmd}')
        with os.popen(cmd) as op:
            return op.read()

    @staticmethod
    def _exec_for_errcode(cmd: str) -> int:
        logger.debug(f'exec_cmd: {cmd}')
        return os.system(cmd)

    @checker
    def _xx_installed(self, *, platform: str, which: str) -> bool:
        if platform == PLATFORM.AND:
            cmd = f'adb -s {self.did} shell pm list packages -3 | ' \
                  f'grep {PACKAGE.ANDQQ if which == APP.QQ else PACKAGE.ANDWX}'
        elif platform == PLATFORM.IOS:
            cmd = f'tidevice -u {self.did} applist | ' \
                  f'grep {PACKAGE.IOSQQ if which == APP.QQ else PACKAGE.ANDWX}'
        else:
            raise KeyError
        if self._exec(cmd):
            return True
        else:
            return False

    @property
    def qq_installed_in_android(self) -> bool:
        return self._xx_installed(platform=PLATFORM.AND, which=APP.QQ)

    @property
    def qq_installed_in_ios(self) -> bool:
        return self._xx_installed(platform=PLATFORM.IOS, which=APP.QQ)

    @property
    def wx_installed_in_android(self) -> bool:
        return self._xx_installed(platform=PLATFORM.AND, which=APP.WX)

    @property
    def wx_installed_in_ios(self) -> bool:
        return self._xx_installed(platform=PLATFORM.IOS, which=APP.QQ)

    @checker
    def _download(self, *, platform: str, which: str, tmpdir: str = None):
        if not tmpdir:
            tmpdir = tempfile.mkdtemp()
        if platform == PLATFORM.AND:
            path = os.path.join(tmpdir, 'qq.apk')
            cmd = f"curl -o {path} {URL.ANDQQ if which == APP.QQ else URL.ANDWX}"
        else:
            raise NotImplementedError
        errcode = self._exec_for_errcode(cmd)
        if errcode == 0:
            return path
        raise Exception(f'_download failed, error code: {errcode}')

    @property
    def download_android_qq(self) -> str:
        return self._download(platform=PLATFORM.AND, which=APP.QQ)

    @checker
    def _install(self, *, platform: str, path: str):
        """install app"""
        if platform == PLATFORM.AND:
            cmd = f'adb -s {self.did} install -g {path}'
        elif platform in PLATFORM.IOS:
            cmd = f'tidevice -u {self.did} install {path}'
        else:
            raise KeyError
        return self._exec(cmd)

    @property
    def install_qq_in_android(self):
        apk = self.download_android_qq
        try:
            ret = self._install(platform=PLATFORM.AND, path=apk)
        finally:
            os.remove(apk)
        return 'success' in ret.lower()


class BaseOperate(object):

    # in facebook-wda text/textXXX alias name/nameXXX
    WHITELIST = [{'text': i} for i in COMMON.WHITELIST]

    def __init__(self, session: typing.Union[u2.Device, wda.Client]):
        if isinstance(session, wda.Client):
            self.sess = session
            self.qq_pkg = PACKAGE.IOSQQ
            self.wx_pkg = PACKAGE.IOSWX
            self.is_ios = True
        elif isinstance(session, u2.Device):
            self.sess = session
            self.qq_pkg = PACKAGE.ANDQQ
            self.wx_pkg = PACKAGE.ANDWX
            self.is_ios = False
        else:
            raise TypeError

    def only(used: str):

        assert used in COMMON.PLATFORMS

        def decorator(func):
            @wraps(func)
            def wrapper(self, *args, **kwargs):
                if used == PLATFORM.AND:
                    assert isinstance(self.sess, u2.Device), f'func: {func.__name__} only used in: {PLATFORM.AND}'
                else:
                    assert isinstance(self.sess, wda.Client), f'func: {func.__name__} only used in: {PLATFORM.IOS}'
                return func(self, *args, **kwargs)
            return wrapper
        return decorator

    def _uiobj(self, **loc) -> typing.Union[wda.Selector, u2.UiObject]:
        if self.is_ios:
            return self.sess(**loc).get(timeout=10)
        return self.sess(**loc)

    def _start(self, package: str):
        return self.sess.app_start(package)

    def _stop(self, package: str):
        self.sess.app_stop(package)

    def qq_start(self):
        self._stop(self.qq_pkg)
        time.sleep(.5)
        return self._start(self.qq_pkg)

    def wx_start(self):
        return self._start(self.wx_pkg)

    def qq_stop(self):
        return self._stop(self.qq_pkg)

    def wx_stop(self):
        return self._stop(self.wx_pkg)

    def ele_exist(self, **loc) -> bool:
        """check element exist or not"""
        return self.sess(**loc).exists

    def ele_text(self, **loc):
        """return element's text"""
        obj = self._uiobj(**loc)
        if self.is_ios:
            return obj.text
        return obj.get_text()

    def _app_current(self):
        return self.sess.app_current()

    @property
    def is_qq_current(self):
        ret = self._app_current()['bundleId' if self.is_ios else 'package']
        logger.debug(f'is_qq_current: {ret}')
        return ret == self.qq_pkg

    @property
    def is_wx_current(self):
        return self.wx_pkg == self._app_current()['bundleId' if self.is_ios else 'package']

    def to_click(self, *, wait: typing.Union[int, float] = 10, **loc):
        """click func

        wait: timeout for click
        loc (dict): element's locator
        """
        try:
            self.sess(**loc).click(timeout=wait)
            logger.debug(f'to_click {loc}, success')
        except Exception as e:
            logger.error(e)
            self._recovery_mode()
            try:
                self.sess(**loc).click(timeout=wait)
            except Exception:
                raise

    def _recovery_mode(self):
        """click's recovery mode, just be used in to_click() !!!"""
        logger.debug('enter recovery_mode ...')
        for name in BaseOperate.WHITELIST:
            if self.ele_exist(**name):
                self.sess(**name).click()
                logger.debug(f'try to click {name}')
                time.sleep(.5)
                return

    def _clear_text(self, **loc):
        obj = self._uiobj(**loc)
        if self.is_ios:
            return obj.set_text('\b' * 100)
        return obj.clear_text()

    def send_keys(self, content: str, **loc):
        """send key

        content (str): need input content
        loc (dict): input box's locator
        """
        self._clear_text(**loc)
        time.sleep(.5)
        self._uiobj(**loc).set_text(content)
        logger.debug(f'send_keys, loc: {loc}, content: {content}')

    @only(used=PLATFORM.AND)
    def wait_for_activity(self, target: typing.Union[tuple, list] = None, timeout: int = 10):
        target = target or COMMON.ACTIVITIES
        end = time.time() + timeout
        while time.time() <= end:
            current_activity = self._app_current().get('activity')
            if current_activity in target:
                return True
            time.sleep(.5)
        return False

    def wait_for_appear(self, timeout: int = 30, **loc):
        end = time.time() + timeout
        while not self.ele_exist(**loc) and time.time() <= end:
            time.sleep(1)
        else:
            if time.time() > end:
                raise TimeoutError
            logger.debug(f'element: {loc} is appeared')


class BaseQQ(BaseOperate):
    """qq login logic"""

    def __init__(self, session: typing.Union[u2.Device, wda.Client], account: str, password: str):
        super().__init__(session)
        self.acc = account
        self.pwd = password
        self.plt = PLATFORM.IOS if self.is_ios else PLATFORM.AND

    def _init_app(self):
        self.qq_start()
        if not self.is_ios:
            self.wait_for_activity()
        time.sleep(3)
        if self.is_ios:
            # ios close popup
            self._recovery_mode()
        self._first_start_init()
        self._login_fail_ctl()
        logger.debug(f'qq init finish ...')

    def _first_start_init(self):
        if self.ele_exist(**QQLoc.privacy_title[self.plt]):
            logger.debug('enter _first_start_init ...')
            self.to_click(**QQLoc.agree_btn[self.plt])
            self.wait_for_appear(**QQLoc.first_login_btn[self.plt])
            self._first_login_enter()

    def _first_login_enter(self):
        if self.ele_exist(**QQLoc.first_login_btn[self.plt]):
            logger.debug('enter _first_login_enter ...')
            self.to_click(**QQLoc.first_login_btn[self.plt])
            time.sleep(.5)

    def _authorize(self):
        if self.ele_exist(**QQLoc.authority_title[self.plt]):
            logger.debug('enter _authorize ...')
            self.to_click(**QQLoc.authorize_btn[self.plt])
            self.to_click(**QQLoc.confirm_btn[self.plt])
            time.sleep(.5)

    def _login(self):
        time.sleep(1)
        self.send_keys(self.acc, **QQLoc.acc[self.plt])
        time.sleep(1)
        self.send_keys(self.pwd, **QQLoc.pwd[self.plt])
        time.sleep(1)
        self.to_click(**QQLoc.login[self.plt])
        time.sleep(1)
        self._authorize()
        time.sleep(5)

    def _login_fail_ctl(self):
        if self.ele_exist(**QQLoc.login_fail[self.plt]):
            logger.debug('enter _login_fail_ctl ...')
            self.to_click(**QQLoc.confirm_btn[self.plt])
            time.sleep(.5)

    @property
    def _is_login(self):
        if not self.is_qq_current:
            self._init_app()
        self._login_fail_ctl()
        ret = self.ele_exist(**QQLoc.qq_login_flag[self.plt])
        logger.debug(f'_is_login: {ret}')
        return ret

    def _qq_login(self, retry: int = 3):
        cnt = 1
        self._init_app()
        while cnt <= retry:
            if self._is_login:
                return
            logger.debug(f'qq login {cnt} times')
            self._first_login_enter()
            self._login_fail_ctl()
            self._login()
            time.sleep(1)
            cnt += 1
        raise Exception('login retry exceed limited!')


class BaseWX(BaseOperate):
    """wx login logic"""


class LoginHelper(BaseQQ, BaseWX):

    def __init__(self, session: typing.Union[u2.Device, wda.Client], device_id: str, account: str, password: str):
        super().__init__(session, account, password)
        self.did = device_id
        self.device = BaseDevice(self.did)

    def goback(func):
        """go back"""

        @wraps(func)
        def wrapper(self, *args, **kwargs):
            start_pkg = self._app_current()['bundleId' if self.is_ios else 'package']
            logger.debug(f'start_app_current: {start_pkg}')
            func(self, *args, **kwargs)
            self._start(start_pkg)
            time.sleep(1)
        return wrapper

    @goback
    def qqlogin(self):
        if self.is_ios:
            assert self.device.qq_installed_in_ios
        else:
            if not self.device.qq_installed_in_android:
                assert self.device.install_qq_in_android, 'qq install fail!'
        self._qq_login()

    @goback
    def wxlogin(self):
        raise NotImplementedError
