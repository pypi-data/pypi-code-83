def start():
    import pystray
    from pystray import MenuItem as item
    from PIL import Image, ImageDraw
    import os

    class Utility:
        def __init__(self):
            self.image = Image.new('RGB', (64, 64))
            self.dc = ImageDraw.Draw(self.image)
            self.dc.rectangle((64, 64, 0, 0), 0x00ff00)

            self.menu = (item('Дипетчер Задач', self.taskmgrr), item('Выйти', self.vladik))

            self.icon = pystray.Icon(name='Tray Utility By Ars', icon=self.image, title='Tray Utility By Ars', menu=self.menu)

            self.icon.run(self.setup)

        def setup(self, icon):
            self.icon.visible = True

        def vladik(self):
            self.icon.notify('Дима не разрешает тебе выйти', 'evlaep')

        def taskmgrr(self):
            os.startfile('taskmgr.exe')


    utilities = Utility()
