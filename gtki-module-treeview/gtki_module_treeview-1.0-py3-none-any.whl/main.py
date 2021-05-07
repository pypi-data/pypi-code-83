from tkinter import ttk
from tkinter import *
import os
import datetime
from gtki_module_treeview import functions
from gtki_module_treeview import settings


class MainTreeview:
    def __init__(self, master, font='"Roboto" 12', text_foreground_color='white', height=18, text_background_color='black',
                 standart_screen_height=1080, *args, **kwargs):
        self.master = master
        self.screenwidth = master.winfo_screenwidth()
        self.screenheight = master.winfo_screenheight()
        self.companies = {}
        self.font = font
        self.reverse = False
        self.style = ttk.Style()
        self.style.map("Treeview",
                       foreground=self.fixed_map("foreground"),
                       background=self.fixed_map("background"))
        self.text_foreground_color = text_foreground_color
        self.text_background_color = text_background_color
        self.height = functions.get_screen_kf(table_height=height, screen_height=self.screenheight,
                                              screen_height_standart=standart_screen_height)

    def sortTime(self, tv, col):
        """ Ранжировка поля по времени """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        newList = []
        for el in l:
            if el[0] == 'None':
                newList.append(('23:59:59', el[1]))
            else:
                newList.append((el[0], el[1]))
        newList.sort(key=lambda x: datetime.datetime.strptime(x[1], '%H:%M:%S'), reverse=self.reverse)
        for index, (val, k) in enumerate(newList):
            tv.move(k, '', index)
        self.change_reverse()

    def sortDate(self, tv, col):
        """ Ранжировака поля по дате """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        newList = []
        for el in l:
            if el[0] == 'None':
                newList.append(('23:59 01.01', el[1]))
            else:
                newList.append((el[0], el[1]))
        try:
            newList.sort(key=lambda x: datetime.datetime.strptime(x[0], '%H:%M %d.%m'),
                         reverse=self.reverse)
        except:
            newList.sort(key=lambda x: datetime.datetime.strptime(x[0], '%H:%M %d.%m'),
                         reverse=self.reverse)
        for index, (val, k) in enumerate(newList):
            tv.move(k, '', index)
        self.change_reverse()

    def sortWeight(self, tv, col):
        """ Ранжировка поля по числам (здесь - веса) """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        newList = []
        for el in l:
            if el[0] == 'None':
                newList.append((0, el[1]))
            else:
                newList.append((el[0], el[1]))
        newList.sort(key=lambda t: int(t[0]), reverse=self.reverse)
        for index, (val, k) in enumerate(newList):
            tv.move(k, '', index)
        self.change_reverse()

    def getMovedDate(self, date):
        """ Возвращает отформатированное время, где время стоит перед датой"""
        try:
            date = date.strftime('%H:%M %d.%m')
        except AttributeError:
            date = 'None'
        return date

    def change_reverse(self):
        """ Переключить флажок для порядка сортировки"""
        if self.reverse == False:
            self.reverse = True
        else:
            self.reverse = False

    def sortId(self, tv, col, reverse=False):
        """ Функция для ранжировки поля по ID """
        l = [(tv.item(k)["text"], k) for k in tv.get_children()]  # Display column #0 cannot be set
        if reverse == False:
            l.sort(key=lambda t: t[0], reverse=self.reverse)
            self.change_reverse()
        else:
            l.sort(key=lambda t: t[0], reverse=True)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)

    def sortUsual(self, tv, col):
        """ Обычная ранжировка поля по алфавиту """
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=self.reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
        self.change_reverse()

    def OnClick(self, event):
        """ Реакция treeview на клик по названию поля"""
        col = self.tree.identify_column(event.x)
        if self.reverse:
            self.img = PhotoImage(file=settings.tric_up_pic_path)
        else:
            self.img = PhotoImage(file=settings.tric_down_pic_path)
        self.tree.heading(col, anchor='w', image=self.img)

    def fixed_map(self, option):
        return [elm for elm in self.style.map("Treeview", query_opt=option)
                if elm[:2] != ("!disabled", "!selected")]

    def get_tree(self):
        """ Вернуть таблицу """
        return self.tree

    def get_timenow(self):
        """ Возвращает отформатированную, читабельную дату """
        today = datetime.datetime.today()
        frmt = today.strftime('%Y.%m.%d %H:%M:%S')
        return frmt

    def clearTree(self):
        """ Очистить таблицу"""
        self.tree.delete(*self.tree.get_children())

    def create_get_tree(self):
        self.tree = self.createTree()
        return self.get_tree()

class NotificationTreeview(MainTreeview):
    """ Тревью о ситуации в системе """
    def __init__(self,  master, *args, **kwarg):
        super().__init__(master, *args, **kwarg)
        self.errors_desctription = {True: 'Подключение успешно',
                                    False: 'Подключение утеряно'}


    def createTree(self):
        print("G")
        self.tree = ttk.Treeview(self.master, style="Custom.Treeview")
        self.tree["columns"] = ("one")
        self.tree.column("#0", width=int(self.screenwidth/4.8), minwidth=int(self.screenwidth/36), stretch='NO')
        self.tree.column("one", width=int(self.screenwidth/1.669), minwidth=int(self.screenwidth/36), stretch='NO')

        self.tree.heading("#0", text="Пункт", anchor='w')
        self.tree.heading("one", text="Статус", anchor='w')
        self.tree.bind("<Button-1>", self.OnClick)
        self.tree.config(height=self.height)


    def fillTree(self, information):
        self.clearTree()
        for point, info in information.items():
            value = self.errors_desctription[info['status']]
            self.tree.insert("", 0, text=point, values=(value,))


class CurrentTreeview(MainTreeview):
    def init(self,  master, *args, **kwarg):
        super().__init__( master, *args, **kwarg)

    def createTree(self):
        self.tree = ttk.Treeview(self.master, style="Custom.Treeview")
        self.tree["columns"] = ("one", "two", "two1", "two2", "three", "four", "five")
        self.tree.column("#0", width=int(self.screenwidth / 14.0146), minwidth=int(self.screenwidth / 64), stretch='NO')
        self.tree.column("one", width=int(self.screenwidth / 13.913), minwidth=int(self.screenwidth / 64), stretch='NO')
        self.tree.column("two", width=int(self.screenwidth / 17.1428), minwidth=int(self.screenwidth / 64),
                         stretch='NO')
        self.tree.column("two1", width=int(self.screenwidth / 17.1428), minwidth=int(self.screenwidth / 64),
                         stretch='NO')
        self.tree.column("two2", width=int(self.screenwidth / 18.8235), minwidth=int(self.screenwidth / 64),
                         stretch='NO')
        self.tree.column("three", width=int(self.screenwidth / 13.913), minwidth=int(self.screenwidth / 64),
                         stretch='NO')
        self.tree.column("four", width=int(self.screenwidth / 13.913), minwidth=int(self.screenwidth / 64),
                         stretch='NO')
        self.tree.column("five", width=int(self.screenwidth / 12.15189), minwidth=int(self.screenwidth / 64),
                         stretch='NO')

        self.tree.heading("#0", text="ID записи", anchor='w',
                          command=lambda: self.sortId(self.tree, "#0"))
        self.tree.heading("one", text="Въезд", anchor='w',
                          command=lambda: self.sortDate(self.tree, "one"))
        self.tree.heading("two", text="Брутто", anchor='w',
                          command=lambda: self.sortWeight(self.tree, "two"))
        self.tree.heading("two1", text="Тара", anchor='w',
                          command=lambda: self.sortWeight(self.tree, "two"))
        self.tree.heading("two2", text="Нетто", anchor='w',
                          command=lambda: self.sortWeight(self.tree, "two"))
        self.tree.heading("three", text="Категория", anchor='w',
                          command=lambda: self.sortUsual(self.tree, "three"))
        self.tree.heading("four", text="Гос. номер", anchor='w',
                          command=lambda: self.sortUsual(self.tree, "four"))
        self.tree.heading("five", text="Комментарии", anchor='w',
                          command=lambda: self.sortUsual(self.tree, "five"))
        self.tree.bind("<Button-1>", self.OnClick)
        self.tree.config(height=self.height)


    def fillTree(self, records):
        self.clearTree()
        print(locals())
        for rec in records:
            self.tree.insert("", 1, text=rec[0], values=(self.getFrmtDate(rec[6]),
                                                         rec[2], rec[3], rec[4], rec[5], rec[1], rec[7]))

    def getFrmtDate(self, date):
        newdate = date.strftime('%H:%M %d.%m')
        return newdate

class HistroryTreeview(MainTreeview):
    def init(self,  master, *args, **kwarg):
        super().__init__( master, *args, **kwarg)

    def createTree(self):
        self.tree = ttk.Treeview(self.master, style="Custom.Treeview", )
        self.tree["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11")
        self.tree.column("#0", width=104, minwidth=50, anchor='w')
        # self.tree.column("preone", width=50, minwidth=30, stretch='NO')
        self.tree.column("1", width=int(self.screenwidth/14), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.column("2", width=int(self.screenwidth/11), minwidth=int(self.screenwidth/64), anchor='w')
        self.tree.column("3", width=int(self.screenwidth/18), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.column("4", width=int(self.screenwidth/18), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.column("5", width=int(self.screenwidth/18), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.column("6", width=int(self.screenwidth/14), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.column("7", width=int(self.screenwidth/14), minwidth=int(self.screenwidth/64))
        self.tree.column("8", width=int(self.screenwidth/14), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.column("9", width=int(self.screenwidth/14), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.column("10", width=int(self.screenwidth/22), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.column("11", width=int(self.screenwidth/10), minwidth=int(self.screenwidth/64), stretch='NO')
        self.tree.bind("<Button-1>", self.OnClick)
        self.tree.heading("#0", text="ID", anchor='w',
                          command=lambda: self.sortId(self.tree, "#0"))
        self.tree.heading("1", text="Гос. номер", anchor='w',
                          command=lambda: self.sortUsual(self.tree, "1"))
        self.tree.heading("2", text="Перевозчик", anchor='w',
                          command=lambda: self.sortUsual(self.tree, "2"))
        self.tree.heading("3", text="Брутто", anchor='w',
                          command=lambda: self.sortWeight(self.tree, "3"))
        self.tree.heading("4", text="Тара", anchor='w',
                          command=lambda: self.sortWeight(self.tree, "4"))
        self.tree.heading("5", text="Нетто", anchor='w',
                          command=lambda: self.sortWeight(self.tree, "5"))
        self.tree.heading("6", text="Категория", anchor='w',
                          command=lambda: self.sortUsual(self.tree, "6"))
        self.tree.heading("7", text="Вид груза", anchor='w',
                          command=lambda: self.sortUsual(self.tree, "7"))
        self.tree.heading("8", text="Дата въезда", anchor='w',
                          command=lambda: self.sortDate(self.tree, "8"))
        self.tree.heading("9", text="Дата выезда", anchor='w',
                          command=lambda: self.sortDate(self.tree, "9"))
        # self.tree.heading("seven", text="На территории",anchor='w')
        self.tree.heading("10", text='Примечания', anchor='w',
                          command=lambda: self.sortUsual(self.tree, "10"))
        self.tree.heading("11", text="Комментарии", anchor='w',
                          command=lambda: self.sortUsual(self.tree, "11"))
        self.tree.config(height=self.height)

    def fillTree(self, history, trashcat='кат. груза', trashtype='вид груза',
                 contragent='перевозчики', carnum='гос. номер'):
        marks = ''
        self.clearTree()
        print('history is', history)
        if trashcat != 'кат. груза':
            marks += '1'
        else:
            marks += '0'
        if trashtype != 'вид груза':
            marks += '1'
        else:
            marks += '0'
        if contragent != 'перевозчики' and contragent != '':
            marks += '1'
        else:
            marks += '0'
        if carnum != 'гос. номер' and carnum != '':
            marks += '1'
        else:
            marks += '0'
        print('marks is', marks)
        if marks.count('1') <= 1:
            for rec in history:
                # print('rec from history insterting', rec)
                if marks == '0000':
                    self.insertRec(rec)
                if marks[0] == '1' and trashcat == rec[11]:
                    self.insertRec(rec)
                if marks[1] == '1' and trashtype == rec[10]:
                    self.insertRec(rec)
                if marks[2] == '1' and contragent == rec[9]:
                    self.insertRec(rec)
                if marks[3] == '1' and carnum == rec[1]:
                    self.insertRec(rec)
        else:
            for rec in history:
                show = True
                for liter in marks:
                    if marks[0] == '1' and trashcat != rec[11]:
                        show = False
                    if marks[1] == '1' and trashtype != rec[10]:
                        show = False
                    if marks[2] == '1' and contragent != rec[9]:
                        show = False
                    if marks[3] == '1' and carnum != rec[1]:
                        show = False
                if show == True:
                    print('here a')
                    self.insertRec(rec)

    def insertRec(self, rec):
        if rec[8] != None and rec[8] > '' and rec[14] == None:
            self.tree.insert("", 1, text=rec[0], tags=('red',), values=(rec[1],
                                                                        rec[9], rec[2], rec[3], rec[4], rec[11],
                                                                        rec[10],
                                                                        self.getMovedDate(rec[5]),
                                                                        self.getMovedDate(rec[6]),
                                                                        rec[8], rec[12]))
        elif rec[8] != None and rec[8] > '' and rec[14] == True:
            self.tree.insert("", 1, text=rec[0], tags=('green',), values=(rec[1],
                                                                          rec[9], rec[2], rec[3], rec[4], rec[11],
                                                                          rec[10],
                                                                          self.getMovedDate(rec[5]),
                                                                          self.getMovedDate(rec[6]),
                                                                          rec[8], rec[12]))
        else:
            self.tree.insert("", 1, text=rec[0], values=(rec[1],
                                                         rec[9], rec[2], rec[3], rec[4], rec[11], rec[10],
                                                         self.getMovedDate(rec[5]), self.getMovedDate(rec[6]),
                                                         rec[8], rec[12]), tags='usual')
        self.tree.tag_configure('red', background='#BE6161',
                                foreground='#E2E2E2', font=self.font)
        self.tree.tag_configure('usual', background="#2F2F2F",
                                font=self.font, foreground='#E2E2E2')