from tkinter import *
import sqlite3


class FindBookWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            self.db_cache = cur.execute(
                "SELECT * FROM books").fetchall()
            self.db_cache = sorted(self.db_cache, key = lambda item: item[3])
        self.resizable(0, 0)
        width, height = 560, 200
        self.geometry(f'{width}x{height}')
        self.title('Поиск книги')
        self.find_label = Label(self, fg = 'green',\
                                text = "    Название книги или имя автора:",\
                                font = ('Calibri', 12, 'bold'))
        self.find_label.grid(row = 0, column = 0, sticky = W)
        self.find_var = StringVar()
        self.find_var.trace("w", lambda name, index, mode,\
                            sv = self.find_var: self.callback(sv))
        self.find_entry = Entry(self, font = ('Calibri', 12, 'bold'),\
                                width = 65, textvariable = self.find_var)
        self.find_entry.grid(row = 1, column = 0, sticky = W,\
                            padx = 5, pady = 5)
        scroll_bar = Scrollbar(self)
        scroll_bar.grid(row = 1, column = 1, rowspan = 2, sticky = E)
        self.result_list = Listbox(self, height = 8, width = 75,
                            yscrollcommand = scroll_bar.set)
        self.result_list.grid(row = 2, column = 0, padx = 5, sticky = W)
        scroll_bar.config(command = self.result_list.yview)

    def callback(self, sv):
        required = sv.get()
        res = []
        for i in self.db_cache:
            if required in i[1] or required in i[2]:
                res.append(i)
        self.result_list.delete(0, END)
        for i in range(len(res)):
            self.result_list.insert(i, f'{res[i][1]}, '+\
                                    f'{res[i][2]}, {res[i][3]}')
