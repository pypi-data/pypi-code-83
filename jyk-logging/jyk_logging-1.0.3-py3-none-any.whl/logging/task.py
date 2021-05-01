import os
import logging
from jyk.timer import Timer

from .core import initLogging, LogRootPath, initConsoleLogging


class TaskLog:
    def __init__(self,
                 task_name,
                 task_id=Timer().now(),
                 log_path=os.path.join(os.getcwd(), 'log'),
                 console_level=logging.INFO,
                 log_level=logging.WARNING):
        self.task_name = task_name
        self.task_id = task_id

        # config
        self.log = logging.getLogger(task_name)
        LogRootPath.set(log_path)
        initConsoleLogging(console_level)
        initLogging(f'{task_name}-{task_id}.log', log_level)

        # Timer
        self.timer = Timer()
        self.tick_name = self.task_name
        self.tick()

    def info(self, meg):
        self.log.info(meg)

    def warning(self, meg):
        self.log.warning(meg)

    def error(self, meg):
        self.log.error(meg)

    def tick(self, name=None):
        if name is None:
            name = self.tick_name
        else:
            self.tick_name = name

        self.timer.start()
        self.log.warning(f'{name} start at: {self.timer.now()}')

    def tock(self):
        name = self.tick_name
        self.timer.end()
        self.log.warning(f'{name} stop at: {self.timer.now()}')
        self.log.warning(
            f'{name} cost: {self.timer.elapse(from_origin=False)}')

    def end(self):
        name = self.task_name
        self.timer.end()
        self.log.warning(f'{name} stop at: {self.timer.now()}')
        self.log.warning(f'{name} cost: {self.timer.elapse(from_origin=True)}')
