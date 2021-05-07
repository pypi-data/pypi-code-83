import tkinter as tk
from PIL import Image, ImageTk
import os
from .tkinterdnd2 import TkinterDnD, DND_FILES, COPY

from tkinter.scrolledtext import ScrolledText
from pystegy import stegyImage

SRC_FILE = 'file'
SRC_RANDOM = 'random'
IMAGE_SIZE = (320,240)
OP_IMAGE_SIZE = (160,120)

class FrameButtons(tk.Frame):
  
    def __init__(self, master, content, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)# self.configure(/ackground = FRAME_COLOR)
        options = {'padx': 10, 'pady': 2}
        self.content = content

        self.buttons = {}
        # button
        self.buttonOk = tk.Button(self, text='Go !')
        self.buttonOk['command'] = master.generate
        # self.buttonOk.grid(row=0, column=3, sticky = 'EN', **options)
        self.buttonOk.pack(side='right', **options)
        self.file_generated = ""

        # placeholderlabel
        self.message = tk.Label(self, text='')
        # self.message.grid(row=0, column=0, columnspan=3, padx = 560)
        self.message.pack(side='bottom', fill='x', expand=True,  padx=320)


        # options button
        self.buttons['src'] = tk.Button(self, text='Options...', relief="groove")
        self.buttons['src']['command'] = lambda : self.showFrame("src") 
        # self.buttons['src'].grid(row=0, column=1, **options)
        self.buttons['src'].pack(side='left', **options)
        # key button
        self.buttons['key'] = tk.Button(self, text='Clé...', relief="groove")
        self.buttons['key']['command'] = lambda : self.showFrame("key") 
        # self.buttons['key'].grid(row=0, column=2, sticky = 'W', **options)
        self.buttons['key'].pack(side='left', **options)

        self.showFrame("mess")
        
    def showFrame(self, frName, force = False):
        for n, b in self.buttons.items():
            b.configure(relief = 'groove')
        if self.content.showFrame(frName, force) == True:
            button = self.buttons.get(frName)
            if not(button is None):
                button.configure(relief = 'sunken')



class FrameMessage(tk.LabelFrame):
  
    def __init__(self, master=None, cnf={}, **kw):
        tk.LabelFrame.__init__(self, master, cnf, **kw)# self.configure(/ackground = FRAME_COLOR)
        options = {'padx': 10, 'pady': 10}
 
        # entry
        self.inputValue = tk.StringVar()
        self.inputValue.set("entrez votre message ici")
        self.text_area = ScrolledText(self, wrap=tk.WORD,
                                      width=40, height=10)
                                    #   font=("Times New Roman", 15))
        # self.input = tk.Entry(self, textvariable = self.inputValue)
        # self.text_area.insert(tk.INSERT,self.op['txt'].get())

        # s0elf.text_area.grid(row=0, column=1, columnspan = 3, **options)
        self.text_area.pack(side='top', fill='both', expand = True,**options)
        self.text_area.focus_set()

    def message(self, text = None):
        if text is None:
            return self.text_area.get("1.0",'end-1c')
        else:
            self.text_area.delete(1.0, 'end')
            self.text_area.insert(1.0,text)
  


class FrameOptionKey(tk.LabelFrame):
  
    def __init__(self, master=None, cnf={}, **kw):
        tk.LabelFrame.__init__(self, master, cnf, **kw)# self.configure(/ackground = FRAME_COLOR)
        options = {'padx': 10, 'pady': 10}
 
        # options variables
        self.op = {}
        self.op['key'] = tk.StringVar()
        self.op['key'].set("")
        # key : textbox
        self.opKey = tk.Entry(self, width=55, textvariable = self.op['key'])
        self.opKey.pack(side='top', fill='x', expand=True, **options)
        self.opKey.focus_set()

    def key(self, key = None):
        if key is None:
            return self.op['key'].get()
        else:
            self.op['key'].set(key)


    def options(self, key = None, **op):
        opts = {}
        
        if (key is None):
            # fill opts
            opts['key'] = self.op['key'].get() 
            return opts

        if len(key):
            self.op['key'].set(key)  

        return opts



class FrameOptionSource(tk.LabelFrame):

    def __init__(self, master=None, cnf={}, **kw):
        tk.LabelFrame.__init__(self, master, cnf, **kw)# self.configure(/ackground = FRAME_COLOR)
        options = {'padx': 10, 'pady': 10}
 
        # options variables
        self.op = {}
        self.op['src'] = tk.StringVar()
        self.op['src'].set(SRC_RANDOM)
        self.op['topics'] = tk.StringVar()
        self.op['topics'].set("dog,cat")
        

        # topic : radio
        self.r1 = tk.Radiobutton(self, text = "Aléatoire", variable = self.op['src'], value = SRC_RANDOM)
        self.r1.grid(row=0, column= 0, sticky = 'W')
        # image : radio
        self.r2 = tk.Radiobutton(self, text = "Image", variable = self.op['src'], value = SRC_FILE)
        self.r2.grid(row=2, column= 0, sticky = 'W')
        
        # topic : label        
        tk.Label(self, text='''image prise aléatoirement sur Flicker, vous pouvez 
spécifier un ou plusieurs topics :''', anchor='w').grid(row=0, column= 1)
        # topic : textbox
        self.opTopics = tk.Entry(self, textvariable = self.op['topics'])
        self.opTopics.grid(row=1, column= 1, sticky='EW')

        # image : label
        tk.Label(self, text='''image de votre choix, droppez-la ici''', anchor='w').grid(row=2, column= 1, sticky='EW')
        # image : image
        global opPhoto
        opIimageSrc = Image.open( os.path.join('ress','src.png')).resize(OP_IMAGE_SIZE, Image.BILINEAR)
        opPhoto = ImageTk.PhotoImage(opIimageSrc)
        self.opSrc = tk.Canvas(self, width = OP_IMAGE_SIZE[0], height = OP_IMAGE_SIZE[1], cursor="hand2")
        self.opSrcImage_in_canvas = self.opSrc.create_image(0,0, image=opPhoto, anchor=tk.NW)
        self.opSrc.grid(row=3, column=1, sticky= tk.NS, **options)
        # DnD stuff
        self.opSrc.drop_target_register(DND_FILES)
        self.opSrc.dnd_bind('<<Drop>>', self.generateSrc)

        self.opTopics.focus_set()
    
    def generateSrc(self, event):
        filepath = event.data
        global opPhoto
        
        self.r2.select()
        op = {}
        op['src'] = filepath 
        op['dest'] = 'ress/src.png' 
        result = stegyImage().encode( "", **op)
        # update canvas image with result
        image = Image.open( result)
        image = image.resize(OP_IMAGE_SIZE)
        opPhoto = ImageTk.PhotoImage(image) 
        self.opSrc.itemconfigure(self.opSrcImage_in_canvas, image = opPhoto)


    def options(self, src : str = None, topics : str = None, **op):
        opts = {}
        if (src is None) & (topics is None) :
            # fill opts
            val = self.op['src'].get()
            if len(val) > 0:
                opts['src'] =  val
            opts['topics'] = self.op['topics'].get() 
            return opts

        if len(src):        
            if src == SRC_RANDOM:
                self.r1.select()
            else:
                self.r2.select()

        if len(topics):
            self.op['topics'].set(topics)

        return opts

    def optionsSelected(self):
        opts = {}
        # if not(options is None):
        #     opts = options

        if self.op['src'].get() == SRC_RANDOM:
            opts['topics'] = self.op['topics'].get() 
        else:
            opts['src'] = 'ress/src.png' 

        return opts

        
