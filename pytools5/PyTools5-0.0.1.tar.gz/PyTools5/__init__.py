#############################
############PYTOOLS5#########
#############################
# PyTools5 by Luke Dixon
# PyTools is a library with some tools useful for python coding
# Copyright 2021 © LukeYT
from PIL import ImageTk,Image
import tkinter
from tkinter import *
import os, sys, glob
import PyQt5

class gui:
    def makelabel(text):
        my_label = Label(root, text=text)

    def makebutton(text, command):
        my_btn = Button(root, text=text, command=command)

class calculate:
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2

class system:
    def _sysprint_(args)
        os.system(f'echo {args}')

    def _syspause_()
        os.system("Pause")

class pywindow:
    def title(name)
        os.system(f"title {name}")