import os
import tkinter as tk
from tkinter import font

from tkinter.messagebox import askyesno


class TitleBar(tk.Frame):
    PATH_LOCK = 'TitleBar.lck'

    """Title Bar widget

    """    
   

    def __init__(self, master, title="TitleBar", buttons=None, font= None, **options):
        """TitleBar constructon with given master widget
        a buttons descritor and classical options ( padx=, padx=, ...)

        Args:
            master (tk.Widget): master widget
            buttons ([dict], optional): dictionary   { "X" : fn1, "Y" : fn2}
               create Button(... title="X", command=fn1 ...) and Button(... title="Y", command=fn2 ...) . 
               Defaults to None.
        """        
        tk.Frame.__init__(self, master)
        
        self._default = {}
        self.designButton = None
        
        self.configure(**options)
        # save given options like padx, padx...
        for txt, opts in options.items():
            self._default[txt] = opts

        self.isDesignMode = True
        self.bHideSystemBar = False
        # are we in design mode ?
        self.checkDesignMode()
        # init label with app title and add buttons
        self.label = tk.Label(self, text=title, **self._default, anchor='w')
        self.label.pack(expand=True, fill="x", side='left', padx = 5)

        self._init_buttons(buttons)

        # set D'nD callbacks
        self.label.bind('<B1-Motion>', self.move_window)
        self.label.bind('<ButtonPress-1>', self.move_window_init)
        self.label.bind('<ButtonRelease-1>', self.move_window_end)
        self.label.bind('<ButtonPress-3>', self.userLock)

    
    def userLock(self, event):
        if not(os.path.exists(self.PATH_LOCK)):
            if askyesno("verrouillage", '''Verouiller la geomètrie de l'application  
            (Effacer le fichier "'''+self.PATH_LOCK+'''" annulera cette action'''):
                with open(self.PATH_LOCK, "wt") as f:
                    f.write(self.winfo_toplevel().geometry())

                self.checkDesignMode()
 
    def checkDesignMode(self):
        self.isDesignMode = True
        try:
            if os.path.exists(self.PATH_LOCK):
                with open(self.PATH_LOCK, "rt") as f:
                    geom = f.read()
                    if len(geom) > 0 :
                        self.isDesignMode = False
                        self.hideRealTitle(geom)
                        if self.designButton:
                            self.designButton.forget()
        finally:
            pass

        return self.isDesignMode



    # 
    #  Drag'n Drop => Move APP on screen
    # 

    def move_window_init(self, event):
        # only when there is no system Title bar
        if self.bHideSystemBar:
            self.delta_x = event.x
            self.delta_y = event.y
        
            self.configure(cursor="hand2")

    def move_window_end(self, event):
        # only when there is no system Title bar
        if self.bHideSystemBar:
            self.configure(cursor="")

    def move_window(self, event):
        # only when there is no system Title bar
        if self.bHideSystemBar:
            self.winfo_toplevel().geometry('+{0}+{1}'.format(event.x_root-self.delta_x, event.y_root-self.delta_y))

    # initialise UI

    def _init_buttons(self, buttons: dict):
        """create buttons and install its highlights callback
            use the 'buttons' dict from constructor
            { "X" : fn1, "Y" : fn2}
            create Button(... title="X", command=fn1 ...) and Button(... title="Y", command=fn2 ...) 

        Args:
            buttons (dict): label , command dict
        """        
        for txt, cmd in reversed(buttons.items()):
            b=tk.Button(self, text=txt, command = cmd, **self._default)
            b.pack(side="right", padx=2, pady = 2)
            b.bind('<Enter>', lambda evt : self._setBgColor(evt, 'red'))
            b.bind('<Leave>', lambda evt : self._setBgColor(evt, None))
            
        if self.isDesignMode:
            self.designButton = tk.Button(self, text='~', command=self.toggleRealTitle, **self._default)
            self.designButton.pack(side="right", padx=2, pady = 2)
            self.designButton.bind('<Enter>', lambda evt : self._setBgColor(evt, 'red'))
            self.designButton.bind('<Leave>', lambda evt : self._setBgColor(evt, None))

    # callback to highlight toolbar buttons on mouse over event
    def _setBgColor(self, event, color = None):
        if color == None:
            event.widget['bg'] = event.widget.master['bg']
            event.widget['fg'] = 'black'
        else:
            event.widget['bg'] = color
            event.widget['fg'] = 'white'    

    def toggleRealTitle(self):
        """toogle system title bar visibily and deactivate geometry calculus
        """        
        if self.isDesignMode:
            self.bHideSystemBar = not(self.bHideSystemBar)
            self.winfo_toplevel().overrideredirect(self.bHideSystemBar) # turns off title bar, geometry

    def hideRealTitle(self, geometry):
        """hide system title bar and set window size and position
        """        
        self.bHideSystemBar = True
        self.winfo_toplevel().overrideredirect(self.bHideSystemBar) # turns off title bar, geometry
        self.winfo_toplevel().geometry(geometry)

