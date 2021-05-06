# -*- coding: utf-8 -*-
"""
Created on Tue May  4 15:59:03 2021

@author: braxt
"""
from math import log
import time
import sys


class ProgressBar(object):
    def __init__(self, items=None, completed=0, maxlen=25, char='█', show_on_update=False, ips=1, lsttime=None):
        self.completed = completed
        self.items = items
        self.maxlen = maxlen
        self.pos = 0
        self.char = char
        self.items_per_sec = ips
        if lsttime:
            self.last_time = lsttime
        else:
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
        a = ProgressBar(self.items, self.completed, self.maxlen, self.char,
                        self.show_on_update, self.items_per_sec, self.last_time)
        a.update(self.completed + other)
        return a

    def format_time(self):
        secs = (self.items-self.completed)/self.items_per_sec
        return f'{int(secs//3600)}:{str(int(secs//60)%60).zfill(2)}:{str(int(secs%60)).zfill(2)} '

    def show(self):
        st = ''
        if self.items:
            st = 'Eta: ' + self.format_time() + '| '
            ips = self.items_per_sec
            if ips > 1:
                st += str(round(ips, 2)) + ' items/s'
            else:
                st += str(round(1/ips, 2)) + ' s/item'

        sys.stdout.write(
            f'{f"{str(self.completed).rjust(int(log(50,10)+.5))}/{self.items}" if self.items else ""} \
{str(round(self.pos*100,2)).ljust(5)}% \
[{(self.char*int(self.pos*self.maxlen)).ljust(self.maxlen)}] {st}\t\r')

    def update(self, completed):
        if self.items:
            t = time.time() - self.last_time
            if t != 0:
                comp = completed - self.completed
                self.items_per_sec += .1 * (comp/t - self.items_per_sec)
                self.last_time = time.time()
                self.completed = completed
                self.pos = completed/self.items
        else:
            self.pos = completed
        if self.show_on_update:
            self.show()


if __name__ == '__main__':
    import random
    prog = ProgressBar(100000, show_on_update=True, ips=1.5)
    for i in range(prog.items):
        prog.update(i)
