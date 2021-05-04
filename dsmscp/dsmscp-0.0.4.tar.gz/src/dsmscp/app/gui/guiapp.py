'''
Created on 19 avr. 2021

@author: tm
'''

import sys
from PyQt5.QtWidgets import QApplication
from .MainWindow import MainWindow


class GuiApp(object):
    """Main class of the module
    """
    def __init__(self, config=None):
        '''
        Constructor
        '''

        self.app = QApplication(sys.argv)
        self.config = config
        
    def start(self):
        """start the app
        """
        self.window = MainWindow(self.config)
        self.window.show()
        
        self.app.exec_()
        
    def stop(self):
        try:
            self.thread.terminate()
        except:
            pass
        