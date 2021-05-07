from concurrent.futures import ThreadPoolExecutor
import time

from xyw_macro.hook import KbHook, Core
from xyw_macro.notify import Notification


class Macro:
    """
    最终封装好的宏命令类，只能在主线程中定义使用
    """
    def __init__(self, max_workers=20, start_message='xyw_macro\n已启动'):
        """
        初始化实例
        :param max_workers: 线程池最大线程数
        :param start_message: 启动时的显示语
        """
        self.__pool = ThreadPoolExecutor(max_workers=max_workers)
        self.__message = start_message
        self.__core = Core(self.__pool)

    def __sub_thread(self):
        """
        监听拦截键盘输入的子进程
        :return:
        """
        kb = KbHook()
        kb.set_handler(self.__core)
        kb.start()

    def __start_gui(self, window):
        """
        启动特效
        :param window:
        :return:
        """
        window.text = self.__message
        window.show()
        time.sleep(2)
        window.hide()

    def add_config(self, config):
        """
        添加配置
        :param config:
        :return:
        """
        self.__core.add_config(config)

    def run(self):
        """
        启动键盘宏
        :return:
        """
        window = Notification()
        self.__core.add_window(window)
        self.__pool.submit(self.__start_gui, window)
        self.__pool.submit(self.__sub_thread)
        window.run()
