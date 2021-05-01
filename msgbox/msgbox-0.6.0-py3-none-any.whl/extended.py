from tkinter import Tk
from tkinter import messagebox


class Extended:
    def __init__(self):
        pass

    def ask(self, title, message):
        root = Tk()
        root.withdraw()
        result = messagebox.askquestion(title, message)
        root.destroy()
        return result


    def askyesno(self, title, message):
        root = Tk()
        root.withdraw()
        result = messagebox.askyesno(title, message)
        root.destroy()
        return result


    def askyesnocancel(self, title, message):
        root = Tk()
        root.withdraw()
        result = messagebox.askyesnocancel(title, message)
        root.destroy()
        return result


    def askokcancel(self, title, message):
        root = Tk()
        root.withdraw()
        result = messagebox.askokcancel(title, message)
        root.destroy()
        return result


    def askretrycancel(self, title, message):
        root = Tk()
        root.withdraw()
        result = messagebox.askretrycancel(title, message)
        root.destroy()
        return result
