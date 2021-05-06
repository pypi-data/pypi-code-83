import sys
import threading
import time

from xyw_macro.hook import KbHook, Core
from xyw_macro.notify import Notification, QtWidgets, QCoreApplication, TextEvent, VisibleEvent


class Macro:
    def __init__(self, start_message='xyw_macro\n已启动'):
        self.__message = start_message
        self.__core = Core()

    def __sub_thread(self):
        kb = KbHook()
        kb.set_handler(self.__core)
        kb.start()

    def __start_gui(self, window):
        QCoreApplication.postEvent(window, TextEvent(self.__message))
        QCoreApplication.postEvent(window, VisibleEvent(True))
        time.sleep(2)
        QCoreApplication.postEvent(window, VisibleEvent(False))

    def add_config(self, config):
        self.__core.add_config(config)

    def run(self):
        app = QtWidgets.QApplication(sys.argv)
        window = Notification()
        self.__core.add_window(window)
        threading.Thread(target=self.__sub_thread).start()
        threading.Thread(target=self.__start_gui, args=(window,)).start()
        sys.exit(app.exec_())
