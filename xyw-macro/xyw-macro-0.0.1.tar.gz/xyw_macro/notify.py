import sys
import threading
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QEvent, QCoreApplication
from PyQt5.QtGui import QPalette


class VisibleEvent(QEvent):
    """
    窗体可见性更改事件
    """
    idType = QEvent.registerEventType()

    def __init__(self, data):
        super().__init__(VisibleEvent.idType)
        self.__data = data

    def get_data(self):
        return self.__data

    data = property(get_data)


class TextEvent(QEvent):
    """
    显示文本更改事件
    """
    idType = QEvent.registerEventType()

    def __init__(self, data):
        super().__init__(TextEvent.idType)
        self.__data = data

    def get_data(self):
        return self.__data

    data = property(get_data)


class Notification(QtWidgets.QWidget):
    def __init__(self, text='xyw'):
        super().__init__()
        self.__text = text
        self.__visible = False
        self.setVisible(False)
        self.__label = QtWidgets.QLabel()
        self.__vnum = 0
        self.__init_gui()

    def __init_gui(self):
        """
        初始化界面
        :return:
        """
        # 获取屏幕信息
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        # 计算窗口宽度和高度
        width = round(screen.width() / 5)
        height = width
        # 计算窗体居中的左上角点坐标
        x = round((screen.width() - width) / 2)
        y = round((screen.height() - height) / 2)
        # 设置窗体为固定尺寸
        self.setFixedSize(width, height)
        # 居中窗体
        self.move(x, y)
        # 设置窗体状态，无边框、始终置顶、无任务栏图标
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        # 设置窗体透明度
        self.setWindowOpacity(0.8)
        # 设置窗体背景颜色
        palette = QPalette()
        palette.setColor(QPalette.Background, Qt.black)
        self.setPalette(palette)

        # 创建标签控件
        self.__label.setAlignment(Qt.AlignCenter)
        # 设置标签中的文本内容
        self.set_text(self.__text)
        # 创建垂直布局
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.__label)
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

    def get_text(self):
        """
        获取标签文本
        :return:
        """
        return self.__text

    def set_text(self, text):
        """
        设置标签文本
        :param text:
        :return:
        """
        self.__text = text
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
        font_size = round(self.geometry().width() * 0.8 / length)
        # 设置标签控件样式
        self.__label.setStyleSheet('color:white;font-size:{0}px;font-weight:bold;margin:{1}px;'
                                   'border-color:white;border-width:{1}px;border-style:solid'
                                   .format(font_size, round(self.geometry().width() / 50)))
        # 更改标签文本
        self.__label.setText(self.__text)

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
        self.setVisible(self.__visible)

    text = property(get_text, set_text)
    visible = property(get_visible, set_visible)

    def customEvent(self, event):
        if event.type() == TextEvent.idType:
            self.text = event.get_data()
        elif event.type() == VisibleEvent.idType:
            if event.get_data():
                if self.__vnum == 0:
                    self.setVisible(True)
                self.__vnum = self.__vnum + 1
            else:
                self.__vnum = self.__vnum - 1
                if self.__vnum == 0:
                    self.setVisible(False)


if __name__ == '__main__':
    # import threading
    #
    # def tes():
    #     app = QtWidgets.QApplication(sys.argv)
    #     window = Notification()
    #     window.set_text('不胜利,\n毋宁死!')
    #     window.show()
    #     sys.exit(app.exec_())
    # threading.Thread(target=tes).start()
    # sys.exit(app.exec_())
    def delay_hide():
        time.sleep(2)
        QCoreApplication.postEvent(window1, VisibleEvent(False))
        time.sleep(2)
        QCoreApplication.postEvent(window1, TextEvent('张怡雯\n2264'))
        QCoreApplication.postEvent(window1, VisibleEvent(True))

    app = QtWidgets.QApplication(sys.argv)
    window1 = Notification()
    window1.text = '不胜利,\n毋宁死!'
    # window1.text = '我'
    # window1.text = '02'
    window1.show()
    threading.Thread(target=delay_hide).start()
    sys.exit(app.exec_())
