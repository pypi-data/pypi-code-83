from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import os
import os.path
from PyQt5.uic import loadUiType
import cv2
import numpy as np
from PIL import Image, ImageGrab 
import pyperclip
import threading

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyTnstaler"""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

ui,_ = loadUiType(resource_path('waitimage.ui'))
img = None

class MainApp(QMainWindow, ui):
    def __init__(self, parent = None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.initUi()
        self.handleButtons()
        self.setWindowTitle('Click Finder')
        self.setMaximumSize(QSize(778, 478))
                
        # radiobutton.toggled.connect(self.onClicked)
        # layout.addWidget(radiobutton, 0, 0)
        
    def initUi(self):
        self.tabWidget.tabBar().setVisible(False)
        # self.line1.setVisible(False)
        # self.line2.setVisible(False)
        style = open(resource_path('themes/classic.css'), 'r')
        style = style.read()
        self.setStyleSheet(style)
        self.codeText.setVisible(False)
        self.copyCodes.setVisible(False)
         
    def closeEvent(self, event):

        quit_msg = "Are you sure you want to exit the program?"
        reply = QMessageBox.question(self, 'Exit', 
                        quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def handleButtons(self):
        self.browse.clicked.connect(self.handleBrowse)
        self.load.clicked.connect(self.loadImage)
        self.copy.clicked.connect(self.handleCopy)
        self.generate.clicked.connect(self.generateCode)
        self.copyCodes.clicked.connect(self.copyCode)
        self.copyCodes2.clicked.connect(self.copyCode2)
        self.home.clicked.connect(self.openHome)
        self.imgLoader.clicked.connect(self.openImageLoader)
        self.codeGen.clicked.connect(self.openCodeGenerator)
        self.settings.clicked.connect(self.openSettings)
        self.darkTheme.clicked.connect(self.applyDarkBlue)
        self.qdarkTheme.clicked.connect(self.applyQDark)
        self.defaultTheme.clicked.connect(self.applyDefaultTheme)
        self.sClick.toggled.connect(self.generateCode)
        # self.lClick.toggled.connect(self.generateCode)
        self.DBClick.toggled.connect(self.generateCode)
        
        self.rClick.toggled.connect(self.generateCode)
        self.clear.clicked.connect(self.clearFields)
        self.generate.setCheckable(True)
        self._toggle = False
        self.bots.clicked.connect(self.openBots)
        self.vpn_bot.clicked.connect(self.vpnBot)
        self.dependences.clicked.connect(self.dependences_download)
        self.test.clicked.connect(self.test_code)
        self.help_btn.clicked.connect(self.help)

    
    def handleBrowse(self):
        saveLocation = QFileDialog.getOpenFileName(self, caption= "Open File", directory="", filter="'Images (*.png *.jpg)'")
        self.imageLocation.setText(str(saveLocation[0]))
        # print(os.getcwd())
    
    def handleCopy(self):
        points = self.genText.text()
        pyperclip.copy(points)
    
    def saveBrowse(self):
        pass
    
    
        
    def loadImage(self):
        saveLocation = self.imageLocation.text()
        if saveLocation == '':
            QMessageBox.warning(self, 'Error', 'Browse image location to continue')            
        else:
            def click_event(event, x, y, flags, param):    
                if event == cv2.EVENT_LBUTTONDOWN:
                    # print(x,', ' ,y)
                    self.genText.setText(str(x) + ',' + str(y))
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    strXY = str(x) + ', '+ str(y)
                    cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
                    cv2.imshow('image', img)
                    cv2.destroyAllWindows()
                    QApplication.processEvents
                if event == cv2.EVENT_RBUTTONDOWN:
                    blue = img[y, x, 0]
                    green = img[y, x, 1]
                    red = img[y, x, 2]
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
                    cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
                    cv2.imshow('image', img)
                    QApplication.processEvents

    #img = np.zeros((512, 512, 3), np.uint8)
            img = cv2.imread(saveLocation)
            cv2.imshow('image', img)
            
            cv2.setMouseCallback('image', click_event)


            cv2.waitKey(0)
            cv2.destroyAllWindows()
        
            QApplication.processEvents

    def help(self):
        QMessageBox.information(self, 'Info', 'For further help, Contact the developers\n at Stanbic Ghana RPA Team \n\nDaniel Williams - WilliamsD@stanbic.com.gh\n\nPatrick Adu-Amankwah - Adu-amankwahP@stanbic.com.gh\n\nStephen Anokye - AnokyeS@stanbic.com.gh\n\nAgyeman-Nimako Alexander - Agyeman-nimakoA@stanbic.com.gh\n\nCollins Mawutor Tenge - TengeC@stanbic.com.gh') 

              
    def copyCode(self):
        code = self.codeText.text()
        pyperclip.copy(code)
        
        
    def copyCode2(self):
        code = self.codeText2.text()
        pyperclip.copy(code)

    def get_mouse_speed(self):
        speed = self.mouse_speed.value()
        return speed
    
    def get_duration(self):
        duration = self.duration.value()
        return duration

    def vpnBot(self):
        QMessageBox.information(self, 'Info', 'This section is still under development. \nIt might be available during the next update. \nWho knows? 🤷') 

    
        
    def generateCode(self):
        # radioButton = self.sender()

        if self.rClick.isChecked():
            if self.generate.isChecked():
                self.codeText.setText(self.rightClick())
                self.generate.setChecked(self._toggle)

        elif self.DBClick.isChecked():
            if self.generate.isChecked():
                self.codeText.setText(self.doubleClick())
                self.generate.setChecked(self._toggle)

        # elif self.lClick.isChecked():
        #     if self.generate.isChecked():
        #         self.codeText.setText(self.leftClick())
        #         self.generate.setChecked(self._toggle)

        elif self.sClick.isChecked():
            if self.generate.isChecked():
                self.codeText.setText(self.singleClick())
                self.generate.setChecked(self._toggle)

        else:
            self.codeText.setText(None)
        saveLocation = self.imageLocation.text()
        # self.codeText.setText('template = setTemplate(' + f"r'{saveLocation }'"+')'+'\nwaitImageLeftDBClick(template, ' + self.genText.text() + ', duration = 10)')
        # self.line1.setVisible(True)
        # self.line2.setVisible(True)
        QApplication.processEvents
    


    def openHome(self):
        self.tabWidget.setCurrentIndex(0)

    def openBots(self):
        self.tabWidget.setCurrentIndex(1)

    def openImageLoader(self):
        self.tabWidget.setCurrentIndex(2)

    def openCodeGenerator(self):
        self.tabWidget.setCurrentIndex(3)

    def openSettings(self):
        self.tabWidget.setCurrentIndex(4)
    
    def singleClick(self):
        # if self.genText.text() == None:
            

        while self.genText.text() == '':

            answer = QMessageBox.question(self, 'Alert', 'You have not selected any co-ordinates, \nDo you still want to generate the code?', QMessageBox.Yes, QMessageBox.No)
            
            if answer == QMessageBox.Yes:
                self.codeText2.setText(f"""# Make sure to import stanbic-iautolib by typing from iautolib import ilib
img = ilib.setTemplate(r'{self.imageLocation.text()}')
ilib.waitImageLeftClick(img, """ + self.genText.text() + """, mouseSpeed="""+ str(self.get_mouse_speed()) + """, duration ="""+ str(self.get_duration()) +""" )""")
                break
            else:
                # self.codeText2.setText(None)
                break
        
        else:
            self.codeText2.setText(f"""# Make sure to import stanbic-iautolib by typing from iautolib import ilib
img = ilib.setTemplate(r'{self.imageLocation.text()}')
ilib.waitImageLeftClick(img, """ + self.genText.text() + """, mouseSpeed="""+ str(self.get_mouse_speed()) + """, duration = """+ str(self.get_duration()) +""" )""")

#         self.codeText2.setText("""from iautolib import ilib

# img = ilib.setTemplate(r'C:/Users/C833238/Desktop/image1.JPG')
# ilib.waitImageLeftClick(img, """ + self.genText.text() + """, duration = 10)""")

        # print (self.genText.text())
    # def singleClick(self):
    #     self.codeText2.setText('pyautogui.click()')
    
    def doubleClick(self):
        # if self.genText.text() == None:
        #     pass
        

        while self.genText.text() == '':

            answer = QMessageBox.question(self, 'Error', 'You have not selected any co-ordinates, \nDo you still want to generate the code?', QMessageBox.Yes, QMessageBox.No)
            
            if answer == QMessageBox.Yes:
                self.codeText2.setText(f"""# Make sure to import stanbic-iautolib by typing from iautolib import ilib
img = ilib.setTemplate(r'{self.imageLocation.text()}')
ilib.waitImageLeftDBClick(img, """ + self.genText.text() + """, mouseSpeed="""+ str(self.get_mouse_speed()) + """, duration ="""+ str(self.get_duration()) +""" )""")
                break
            else:
                # self.codeText2.setText(None)
                break

        else:
            self.codeText2.setText(f"""# Make sure to import stanbic-iautolib by typing from iautolib import ilib
img = ilib.setTemplate(r'{self.imageLocation.text()}')
ilib.waitImageLeftDBClick(img, """ + self.genText.text() + """, mouseSpeed="""+ str(self.get_mouse_speed()) + """, duration ="""+ str(self.get_duration()) +""" )""")
#         self.codeText2.setText("""from iautolib import ilib

# img = ilib.setTemplate(r'C:/Users/C833238/Desktop/image1.JPG')
# ilib.waitImageLeftDBClick(img, """ + self.genText.text() + """, duration = 10)""")
        # self.codeText2.setText('pyautogui.doubleClick()')
    

#     def leftClick(self):
#         self.codeText2.setText("""from iautolib import ilib

# img = ilib.setTemplate(r'C:/Users/C833238/Desktop/image1.JPG')
# ilib.waitImageLeftClick(img, """ + self.genText.text() + """, duration = 10)""")


    # def leftClick(self):
    #     self.codeText2.setText('pyautogui.leftClick()')
        

    def rightClick(self):
        # if self.genText.text() == None:
        #     pass

        while self.genText.text() == '':

            answer = QMessageBox.question(self, 'Error', 
            'You have not selected any co-ordinates, \nDo you still want to generate the code?', QMessageBox.Yes, QMessageBox.No)
            
            if answer == QMessageBox.Yes:
                self.codeText2.setText(f"""# Make sure to import stanbic-iautolib by typing from iautolib import ilib
img = ilib.setTemplate(r{self.imageLocation.text()})
ilib.waitImageRightClick(img, """ + self.genText.text() + """, mouseSpeed="""+ str(self.get_mouse_speed()) + """, duration ="""+ str(self.get_duration()) +""" )""")
                break
            else:
                # self.codeText2.setText(None)
                break

        else:
            self.codeText2.setText(f"""# Make sure to import stanbic-iautolib by typing from iautolib import ilib
img = ilib.setTemplate(r'{self.imageLocation.text()}')
ilib.waitImageRightClick(img, """ + self.genText.text() + """, mouseSpeed="""+ str(self.get_mouse_speed()) + """, duration ="""+ str(self.get_duration()) +""" )""")



    # def rightClick(self):
    #     self.codeText2.setText('pyautogui.rightClick()')

    def clearFields(self):
        self.codeText2.setText(None)

    def test_code(self):
        code = f"""from iautolib import ilib\n{self.codeText2.text()}"""
        
        # print(code)
        exec(code)
               
    ############## App Themes ###############
    
    def applyDarkBlue(self):
        style = open(resource_path('themes/darkblue.css'), 'r')
        style = style.read()
        self.setStyleSheet(style)
    
    def applyQDark(self):
        style = open(resource_path('themes/qdark.css'), 'r')
        style = style.read()
        self.setStyleSheet(style)
        #34,29
    
    def applyDefaultTheme(self):
        style = open(resource_path('themes/classic.css'), 'r')
        style = style.read()
        self.setStyleSheet(style)

    def dependences_download(self):
        threadObj = threading.Thread(target=os.system("pip install stanbic-iautolib"))
        threadObj.start()
        
    
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()