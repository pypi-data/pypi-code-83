import tkinter
import tkinter.font as tf
import time
import threading
from xyw_macro.utils import SingletonType


class Notification(metaclass=SingletonType):
    def __init__(self, text='xyw'):
        self.__text = text
        self.__visible = False
        self.__vnum = 0
        self.__window, self.__label, self.__width = self.__init__window()
        self.set_visible(self.__visible)

    def show(self):
        if self.__vnum == 0:
            self.set_visible(True)
        self.__vnum = self.__vnum + 1

    def hide(self):
        self.__vnum = self.__vnum - 1
        if self.__vnum == 0:
            self.set_visible(False)

    def __init__window(self):
        window = tkinter.Tk()
        window.wm_attributes('-topmost', True)
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        width = round(screen_width / 5)
        height = round(screen_width / 5)
        window.geometry('{}x{}+{}+{}'.format(width, height, (screen_width - width) // 2, (screen_height - height) // 2))
        window.overrideredirect(True)
        window.configure(background='black')
        window.attributes('-alpha', 0.7)
        font_size = self.__get_font_size(width)
        outer_border_size = round(font_size * 0.08)
        inner_border_size = round(font_size * 0.05)
        font = tf.Font(size=font_size, weight=tf.BOLD)
        label_border = tkinter.LabelFrame(window, background='white', relief='flat')
        label = tkinter.Label(label_border, text=self.__text, font=font, bg='black', fg='white',
                              height=height, width=width, justify='center', anchor='center',
                              borderwidth=0, relief='flat')
        label_border.pack(fill='both', expand=True, padx=outer_border_size, pady=outer_border_size)
        label.pack(fill='both', expand=True, padx=inner_border_size, pady=inner_border_size)
        return window, label, width

    def get_text(self):
        """
        获取标签文本
        :return:
        """
        return self.__text

    def __get_font_size(self, width):
        # 根据换行符拆分文本
        texts = self.__text.split('\n')
        # 英文半角字符集
        alnum = r'abcdefghijklmnopqrstuvwxyz0123456789+-*/=`~!@#$%^&*()_\|?><.,'
        # 计算最大单行字符长度
        length = [1]
        for item in texts:
            tem = 0
            for i in item:
                if i.lower() in alnum:
                    # 英文半角字符算半个字符长度
                    tem = tem + 0.5
                else:
                    # 其他字符算一个字符长度
                    tem = tem + 1
            length.append(tem)
        length = max(length)
        # 根据字符长度动态更改字体尺寸
        font_size = round(width * 0.6 / length)
        return font_size

    def set_text(self, text):
        """
        设置标签文本
        :param text:
        :return:
        """
        self.__text = text
        font_size = self.__get_font_size(self.__width)
        # 更改标签文本
        font = tf.Font(size=font_size, weight=tf.BOLD)
        self.__label.config(text=self.__text, font=font)

    def get_visible(self):
        """
        获取窗体可见性
        :return:
        """
        return self.__visible

    def set_visible(self, visible):
        """
        设置窗体可见性
        :param visible:
        :return:
        """
        self.__visible = visible
        if self.__visible:
            self.__window.update()
            self.__window.deiconify()
        else:
            self.__window.withdraw()

    def run(self):
        self.__window.mainloop()

    text = property(get_text, set_text)
    visible = property(get_visible, set_visible)


if __name__ == '__main__':
    def sub():
        time.sleep(2)
        notify.text = 'xue'
        notify.show()
        time.sleep(2)
        notify.hide()
    #     notify = Notification()
    #     threading.Thread(target=auto_hide).start()
    #     notify.start()
    # thd = threading.Thread(target=sub)
    # thd.start()
    # def auto_hide():
    #     time.sleep(2)
    #     # notify.destroy()
    #     # flag = False
    #     notify.hide()
    notify = Notification('xyw_macro\n已启动')
    threading.Thread(target=sub).start()
    notify.run()
    # notify.show(0.2)
    # print('end')
    # time.sleep(2)
    # notify.set_text('changed')
    # notify.show()

    # notify.start()
    # print('xue')
    # print(type(notify.get_window()))
    # notify.start()
    # flag = True
    # while flag:
    #     # notify.get_window().update_idletasks()
    #     notify.get_window().update()
