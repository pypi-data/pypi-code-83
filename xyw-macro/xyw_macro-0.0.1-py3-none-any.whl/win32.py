import ctypes
import time
from ctypes import wintypes, windll

PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdMsg(ctypes.Structure):
    """
    键盘回调函数用结构体
    """
    _fields_ = [
        ('vkCode', wintypes.DWORD),
        ('scanCode', wintypes.DWORD),
        ('flags', wintypes.DWORD),
        ('time', wintypes.DWORD),
        ('dwExtraInfo', PUL)]


class KeyBdInput(ctypes.Structure):
    """
    键盘输入用结构体
    """
    EXTENDEDKEY = 0x0001
    KEYUP = 0x0002
    SCANCODE = 0x0008
    UNICODE = 0x0004

    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    """
    硬件输入用结构体
    """
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    """
    鼠标输入用结构体
    """
    MOVE = 0x0001
    LEFTDOWN = 0x0002
    LEFTUP = 0x0004
    RIGHTDOWN = 0x0008
    RIGHTUP = 0x0010
    MIDDLEDOWN = 0x0020
    MIDDLEUP = 0x0040
    XDOWN = 0x0080
    XUP = 0x0100
    WHEEL = 0x0800
    HWHEEL = 0x1000
    ABSOLUTE = 0x8000

    XBUTTON1 = 0x0001
    XBUTTON2 = 0x0002

    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class InputUnion(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    """
    SendInput函数用最终结构体
    """
    MOUSE = 0
    KEYBOARD = 1
    HARDWARE = 2

    _fields_ = [("type", ctypes.c_ulong),
                ("ii", InputUnion)]


# 键盘事件用回调函数
HookProc = ctypes.WINFUNCTYPE(
    wintypes.LPARAM,
    ctypes.c_int32, wintypes.WPARAM, ctypes.POINTER(KeyBdMsg))


# 消息队列发送函数
SendInput = windll.user32.SendInput
SendInput.argtypes = (
    wintypes.UINT,
    ctypes.POINTER(Input),
    ctypes.c_int)


# 获取并阻断消息队列
GetMessage = windll.user32.GetMessageA
GetMessage.argtypes = (
    wintypes.MSG,
    wintypes.HWND,
    wintypes.UINT,
    wintypes.UINT)


# 设置回调函数
SetWindowsHookEx = windll.user32.SetWindowsHookExA
SetWindowsHookEx.argtypes = (
    ctypes.c_int,
    HookProc,
    wintypes.HINSTANCE,
    wintypes.DWORD)


# 解除回调函数
UnhookWindowsHookEx = windll.user32.UnhookWindowsHookEx
UnhookWindowsHookEx.argtypes = (
    wintypes.HHOOK,)


# 将消息传递到钩子链下一函数
CallNextHookEx = windll.user32.CallNextHookEx
CallNextHookEx.argtypes = (
    wintypes.HHOOK,
    ctypes.c_int,
    wintypes.WPARAM,
    KeyBdMsg)


GetAsyncKeyState = windll.user32.GetAsyncKeyState
GetAsyncKeyState.argtypes = (
    ctypes.c_int,
)


GetMessageExtraInfo = windll.user32.GetMessageExtraInfo


SetMessageExtraInfo = windll.user32.SetMessageExtraInfo
SetMessageExtraInfo.argtypes = (
    wintypes.LPARAM,
)


def send_kb_event(v_key, is_pressed):
    """
    向消息队列发送键盘输入，指定dwExtraInfo为228，便于回调函数过滤此部分键盘输入
    :param v_key: 虚拟键号
    :param is_pressed: 是否按下
    :return:
    """
    extra = ctypes.c_ulong(0)
    li = InputUnion()
    flag = KeyBdInput.KEYUP if not is_pressed else 0
    li.ki = KeyBdInput(v_key, 0x48, flag, 0, ctypes.pointer(extra))
    SetMessageExtraInfo(228)
    input = Input(Input.KEYBOARD, li)
    return SendInput(1, ctypes.pointer(input), ctypes.sizeof(input))


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


@HookProc
def kb_callback(n_code, w_param, l_param):
    l_param = l_param.contents
    if GetMessageExtraInfo() == 228:
        SetMessageExtraInfo(0)
        return CallNextHookEx(0, n_code, w_param, l_param)
    # print(n_code)
    # print(w_param)
    # print(l_param)
    # print(l_param.vkCode)
    # print(l_param.scanCode)
    # print(l_param.flags)
    # print(l_param.time)
    # print(l_param.dwExtraInfo)
    # print('press')
    press_key(ord('A'))
    release_key(ord('A'))
    return -1


def PressAltTab():
    press_key(0x012)  # Alt
    press_key(0x09)  # Tab

    time.sleep(2)  # optional : if you want to see the atl-tab overlay

    release_key(0x09)  # ~Tab
    release_key(0x012)  # ~Alt


if __name__ == "__main__":
    # import win32con
    # res = SetWindowsHookEx(
    #     win32con.WH_KEYBOARD_LL,
    #     kb_callback,
    #     None,
    #     0
    # )
    # print(res)
    # GetMessage(wintypes.MSG(), 0, 0, 0)
    PressAltTab()
    # press_key(0x012)  # Alt
    # print(SetMessageExtraInfo(228))
    # print(GetMessageExtraInfo())
