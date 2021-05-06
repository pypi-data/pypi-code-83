import tkinter as winprog

class console():
  def write(text):
    print(text)
  def ask(ask):
    input(ask)

class windowprog():
  
  # create window:
  def createwin(rootvar, geometry, title):
    rootvar.geometry(geometry)
    rootvar.title(title)
  
  # main loop:
  def mainloop(rootvar):
    rootvar.mainloop()