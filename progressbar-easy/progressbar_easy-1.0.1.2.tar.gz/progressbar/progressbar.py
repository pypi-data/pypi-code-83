# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:59:03 2021

@author: braxt
"""
from math import log
import time
import sys


class ProgressBar(object):
    def __init__(self, items=None, maxlen=25, char='█', show_on_update=False, items_per_sec=1):
        self.completed = 0
        self.items = items
        self.maxlen = maxlen
        self.pos = 0
        self.char = char
        self.items_per_sec = items_per_sec
        self.last_time = time.time()
        self.show_on_update = show_on_update

    def __repr__(self):
        return str(self.pos)

    def __value__(self):
        return self.pos

    def __add__(self, other):
        return self.completed + other

    def __sub__(self, other):
        return self.completed - other

    def __mul__(self, other):
        return self.completed * other

    def __div__(self, other):
        return self.completed / other

    def __iadd__(self, other):
        a = ProgressBar(self.items, self.maxlen, self.char, self.show_on_update, self.items_per_sec)
        a.update(self.completed + other)
        return a

    def format_time(self):
        secs = self.items_per_sec*(self.items-self.completed)
        return f'{int(secs//3600)}:{str(int(secs//60)%60).zfill(2)}:{str(int(secs%60)).zfill(2)}'

    def show(self):
        st = ''
        if self.items:
            st = self.format_time() + ' remaining '
            ips = self.items_per_sec
            if ips < 1:
                st += str(round(1/ips, 2)) + ' items/s'
            else:
                st += str(round(ips, 2)) + ' s/item'

        sys.stdout.write(
            f'{f"{str(self.completed).rjust(int(log(50,10)+.5))}/{self.items}" if self.items else ""} \
Completed \
{str(round(self.pos*100,2)).ljust(5)}% \
[{(self.char*int(self.pos*self.maxlen)).ljust(self.maxlen)}] {st}\t\r')

    def update(self, completed):
        if self.items:
            self.items_per_sec += .05 * \
                ((time.time() - self.last_time) - self.items_per_sec)
            self.last_time = time.time()
            self.completed = completed
            self.pos = completed/self.items
        else:
            self.pos = completed
        if self.show_on_update:
            self.show()


if __name__ == '__main__':
    import random
    prog = ProgressBar(40000000000, show_on_update=True)
    for i in range(100):
        time.sleep(random.random()/5)
        prog += 1
