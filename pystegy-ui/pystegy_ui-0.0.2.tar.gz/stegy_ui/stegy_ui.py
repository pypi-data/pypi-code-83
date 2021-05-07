import os
import json
from datetime import datetime

import tkinter as tk
from tkinter.messagebox import *
from .tkinterdnd2 import TkinterDnD, DND_FILES, COPY
from PIL import Image, ImageTk

from .frame_option import FrameOptionSource,FrameOptionKey, FrameMessage, FrameButtons
from .ui.title import TitleBar

from pystegy import stegyImage
from pystegy.utils import BadKey, NoMessage

import pkg_resources
import shutil

consts = {"FRAME_COLOR" : 'gray30'}

FRAME_COLOR = 'gray30'
IMAGE_SIZE = (320,240)
OP_IMAGE_SIZE = (97,80)

class ContentFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.FRAMES = {}
        
        self.FRAMES["src"] = FrameOptionSource(self, text= 'image')
        self.FRAMES["key"] = FrameOptionKey(self, text= 'clé')
        self.FRAMES["mess"] = FrameMessage(self, text= 'message')
        
        self.current = "src"
        self.showFrame('src')

    def showFrame(self, name, force = False):
        ret = False

        if force == False :
            if name == self.current == 'key':
                name = 'mess'
            elif name == self.current == 'src':
                name = 'mess'
            else:
                ret = True
        else:
            ret = True

        self.current = name

        self.FRAMES["src"].pack_forget()
        self.FRAMES["key"].pack_forget()
        self.FRAMES["mess"].pack_forget()

        self.FRAMES[name].pack(side ='left', fill = 'both', expand=True)

        return ret

    def message(self, text = None):
        return self.FRAMES["mess"].message( text)

    def key(self):
        op = self.FRAMES["key"].options()
        return op['key']

    def options(self, **op):
        opts = {}

        opts.update(self.FRAMES["src"].options(**op))
        opts.update(self.FRAMES["key"].options(**op))

        return opts

    def optionsSelected(self):
        opts = {}

        opts.update(self.FRAMES["src"].optionsSelected())
        opts.update(self.FRAMES["key"].options())

        return opts

    def ReadConf(self):
        try :
            with open('stegy.cnf', 'rt') as conf:
                op = json.load(conf)
                self.options(**op)
        except:
            pass

    def WriteConf(self):
        try :
            with open('stegy.cnf', 'wt') as conf:
                op = self.options()
                json.dump(op, conf)
        except:
            pass


class TitleFrame(tk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        # self.configure(background = consts['FRAME_COLOR'])
        toptions = {'padx' : 0, 
                    'pady': 0, 
                    'relief':'flat', 
                    'bg' : consts['FRAME_COLOR'],
                    'font' : ('Times New Roman' , 10)
                    }

        self.title = TitleBar(self, title = "Stegy", buttons={"X": container.destroy},  **toptions)
        self.title.grid(row = 0, column=0, columnspan = 2, sticky="WE")

        options = {'padx' : 5, 
                    'pady': 5
                    }

        # canvas
        global photo
        imageDef = Image.open( os.path.join('ress','stegy.bmp'))
        photo = ImageTk.PhotoImage(imageDef) 
        self.imCan = tk.Canvas(self, width = IMAGE_SIZE[0], height = IMAGE_SIZE[1], cursor="hand2")
        self.image_in_canvas = self.imCan.create_image(0,0, image=photo, anchor=tk.NW)
        self.imCan.grid(row=1, column=0 , sticky='W', **options)
        # Dnd stuff
        self.imCan.drop_target_register(DND_FILES)
        self.imCan.dnd_bind('<<Drop>>', self.fileDroppedOnMe)
        self.imCan.drag_source_register(DND_FILES)
        self.imCan.dnd_bind('<<DragInitCmd>>', self.dragResult)
        # self.share.drag_source_register(DND_FILES)
        # self.share.dnd_bind('<<DragInitCmd>>', self.resultDragInit)





        self.content = ContentFrame(self)
        self.content.grid(row = 1, column=1, sticky="WE", **options)

        self.buttons = FrameButtons(self, self.content)

        self.buttons.grid(row = 2, column = 0, columnspan = 2, **options)
        self.file_generated = None
        self.stegy = stegyImage()


        self.content.ReadConf()

    def generate(self):
        self.content.WriteConf()
        
        op = self.content.optionsSelected()
        op['dest'] = self.genDestFileName()
        
        self.file_generated = os.path.abspath(
                self.stegy.encode(self.content.message(),  **op ))

        self.verify(self.file_generated)

    def genDestFileName(self):

        now = datetime.now() # current date and time
        return now.strftime("data/%H_%M_%S.png")


    def verify(self, filepath):
        global photo2
        
        # clean results info 
        # self.message.config( text="")
        # self.share['state'] = 'disabled'
        
        # update canvas image with result
        image = Image.open( filepath)
        photo2 = ImageTk.PhotoImage(image) 
        self.imCan.itemconfigure(self.image_in_canvas, image = photo2)
        
        try:    
            # re-extract text to verify validity
            txt = self.stegy.decode(filepath, key = self.content.key())
            # update label accordingly
            self.content.message(txt)
            self.buttons.showFrame("mess", True)
            if len(txt) > 50:
                showinfo(title='message', message=txt)
        except BadKey:
            showerror(message = '''Erreur de décodage du message !
            Essayez avec une autre clé de décodage''')
            self.buttons.showFrame("key", True)
        except NoMessage:
            showinfo(message = 'désolé pas de message dans cette image !')
       


    def fileDroppedOnMe(self, event):
        filepath = event.data
        self.verify(filepath)

    def dragResult(self, event):
        #   source : https://wiki.tcl-lang.org/page/TkDND+Tutorial   
        # bind .drag_source_text <<DragInitCmd>> \
        #   {list copy DND_Text {Some nice dropped text!}}
        # bind .drag_source_files <<DragInitCmd>> \
        #   {list {copy move} DND_Files [list $filename $filename]}

        return (COPY,DND_FILES, (self.file_generated,) )



    def getContent(self):
        return self.content

    def getTitle(self):
        return self.title




class StegyApp(TkinterDnD.Tk):


    def __init__(self):
        super().__init__()

        unpackResources()
    
        # configure the root window
        self.title('Stegy')

        self.iconbitmap('./ress/stegy.ico')

        self.initDirs()

        self.frame = TitleFrame(self)
        self.frame.grid(row = 0, column=0, sticky="WESN")


    def initDirs(self):
        if not(os.path.exists('./ress')):
            os.makedirs('./ress')
            # // appeler setegy pour creer un src.png
        if not(os.path.exists('ress\src.png')):
            s = stegyImage()
            s.encode("", topics='dinosaure', dest='ress\src.png' )
        if not(os.path.exists('data')):
            os.mkdir('data')
            
def unpackResources():
    locpath = ('./ress', './data')
    for l in locpath:
        if not (os.path.exists(os.path.abspath(l))):
            os.makedirs(os.path.abspath(l))

    lst = {'datas/stegy.ico' : 'ress/stegy.ico',
            'datas/share32.png' : 'ress/share32.png',
            'datas/stegy.bmp' : 'ress/stegy.bmp',
            'datas/src.png' : 'ress/src.png',
            'datas/TitleBar.lck' : 'TitleBar.lck',
            'datas/stegy.cnf' : 'stegy.cnf' }

    for source,dest  in lst.items():
        src = pkg_resources.resource_filename(__name__, source)
        if not(os.path.exists(dest)) :
            shutil.copyfile(src, dest)
        


if __name__ == "__main__":
    app = StegyApp()
    app.mainloop()



