from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import sqlite3


class DeleteBookWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            self.res = cur.execute(
                "SELECT * FROM books").fetchall()
            self.res = sorted(self.res, key = lambda item: item[3])
        self.index = 0
        self.resizable(0, 0)
        width, height = 750, 96        
        self.geometry(f'{width}x{height}')
        self.title('Удаление книги') 
        self.book_title_label = Label(self, text = "    Книга:",
                             font = ( 'Calibri', 12, 'bold'))
        self.book_title_label.pack(anchor = NW)
        self.combobox_src = []
        for x in self.res:
            self.combobox_src.append(f'{x[1]}, {x[2]}, {x[3]}')
        self.cur_sel = StringVar(value = self.combobox_src[0])
        self.cur_sel.trace('w', self.get_index)
        self.combobox = ttk.Combobox(self, font = ('Calibri', 12, 'bold'),
                        values = self.combobox_src, \
                            textvariable = self.cur_sel)
        self.combobox.pack(padx = 10, side = TOP, fill = X, anchor = NW)
        self.combobox.bind("<<ComboboxSelected>>", self.get_index)
        self.btn = Button(self, text = "Удалить", 
                            command = self.delete_book)
        self.btn.pack(pady = 10)        

    def get_index(self, *args):
        self.index = self.combobox.current()

    def delete_book(self):
        cs = self.cur_sel.get()
        _ = cs.split(', ')
        title = _[0]
        author = _[1]
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            cur.execute(
                "DELETE FROM books WHERE book_title = ? AND author = ?",\
                (title, author))
        del self.combobox_src[self.index]
        self.cur_sel.set('')
        self.combobox.config(values = self.combobox_src)
        showinfo('', f'Книга {cs} удалена из БД')
