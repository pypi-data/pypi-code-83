from tkinter import Tk
from tkinter import messagebox


class Msg:
    def __init__(self):
        pass

    def error(self, title, message):
        root = Tk()
        root.withdraw()
        messagebox.showerror(title, message)
        root.destroy()

    def warning(self, title, message):
        root = Tk()
        root.withdraw()
        messagebox.showwarning(title, message)
        root.destroy()

    def info(self, title, message):
        root = Tk()
        root.withdraw()
        messagebox.showinfo(title, message)
        root.destroy()
