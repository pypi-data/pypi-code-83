import time
import random
import win32clipboard
import win32con
import webbrowser
from subprocess import getstatusoutput
from xyw_macro.win32 import send_kb_event, send_unicode
from xyw_macro.hook import VK


def press_key(v_key):
    """
    按下某个按键
    :param v_key:
    :return:
    """
    return send_kb_event(v_key, True)


def release_key(v_key):
    """
    松开某个按键
    :param v_key:
    :return:
    """
    return send_kb_event(v_key, False)


def random_sleep(seconds, range_percent=None):
    """
    睡眠指定秒数，随机浮动指定比例
    :param seconds: 睡眠时间，单位s
    :param range_percent: 浮动比例
    :return: 实际睡眠时间，单位s
    """
    if range_percent is None:
        range_percent = 0
    ran = seconds * range_percent
    sleep_time = random.uniform(seconds - ran, seconds + ran)
    time.sleep(sleep_time)
    return sleep_time


def press_copy():
    press_key(VK('VK_CONTROL'))
    press_key(ord('C'))
    release_key(VK('VK_CONTROL'))
    release_key(ord('C'))
    time.sleep(0.2)


def get_clipboard_files():
    """
    获取剪切板中文件的文件地址
    :return: 地址元组
    """
    if win32clipboard.IsClipboardFormatAvailable(win32con.CF_HDROP) == 0:
        return
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32con.CF_HDROP)
    win32clipboard.CloseClipboard()
    return data


def run_cmd(cmd):
    """
    运行cmd命令，可以用来打开应用快捷方式
    :param cmd:
    :return:
    """
    return getstatusoutput(cmd)


def open_file(path):
    """
    使用系统默认程序打开文件或文件夹
    :param path:
    :return:
    """
    return getstatusoutput('explorer.exe %s' % path)


def input_chars(chars):
    """
    模拟键盘输入字符串
    :param chars:
    :return:
    """
    for char in chars:
        send_unicode(char)


def open_url(url, browser_path=None):
    """
    使用浏览器打开网址
    :param url: 网址
    :param browser_path: 非默认浏览器程序地址
    :return:
    """
    if browser_path is not None:
        webbrowser.register('browser', None, webbrowser.BackgroundBrowser(browser_path))
        webbrowser.get('browser').open(url, new=0, autoraise=True)
    else:
        webbrowser.open(url, new=0, autoraise=True)


if __name__ == '__main__':
    # print(random_sleep(0.2, 0.25))
    # print(get_clipboard_files())
    # print(type(get_clipboard_files()))
    # press_copy()
    # print(run_cmd(r"C:\Program Files (x86)\Thunder Network\Thunder\Program\ThunderStart.exe"))
    # print(open_file('xue'))
    # input_chars('今天是个好人797987/*/-*-*+')
    # open_url('www.baidu.com', r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    open_url('www.baidu.com')
