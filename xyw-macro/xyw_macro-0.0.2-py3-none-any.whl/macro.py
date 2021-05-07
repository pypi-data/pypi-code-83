import sys
import threading
import time

from xyw_macro.hook import KbHook, Core
from xyw_macro.notify import Notification


class Macro:
    def __init__(self, pool, start_message='xyw_macro\n已启动'):
        self.__pool = pool
        self.__message = start_message
        self.__core = Core(self.__pool)

    def __sub_thread(self):
        kb = KbHook()
        kb.set_handler(self.__core)
        kb.start()

    def __start_gui(self, window):
        window.text = self.__message
        window.show()
        time.sleep(2)
        window.hide()

    def add_config(self, config):
        self.__core.add_config(config)

    def run(self):
        window = Notification()
        self.__core.add_window(window)
        self.__pool.submit(self.__start_gui, window)
        self.__pool.submit(self.__sub_thread)
        window.run()
