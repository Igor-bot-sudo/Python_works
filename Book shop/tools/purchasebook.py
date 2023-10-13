from tkinter import *
from tkinter import ttk
import sqlite3


class PurchaseBookWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            self.books = cur.execute(
                "SELECT * FROM books").fetchall()
            self.books = sorted(self.books, key = lambda item: item[3])
            self.employees = cur.execute(
                "SELECT * FROM employees").fetchall()
        self.parent = parent
        self.book_index = 0
        self.employee_index = 0
        self.resizable(0, 0)
        width, height = 800, 194
        self.geometry(f'{width}x{height}')
        self.title('Покупка книги')
        Label(self, text = "    Продавец:",
                font = ('Calibri', 12, 'bold')).pack(anchor = NW)
        self.combobox_employee_src = []
        for x in self.employees:
            self.combobox_employee_src.append(f'{x[1]}')
        self.cur_employee_sel = StringVar(value =\
                                        self.combobox_employee_src[0])
        self.cur_employee_sel.trace('w', self.get_employee_index)
        self.combobox_employee = ttk.Combobox(self,\
                        font = ('Calibri', 12, 'bold'),
                        values = self.combobox_employee_src,\
                        textvariable = self.cur_employee_sel)
        self.combobox_employee.pack(padx = 10, side = TOP,\
                                    fill = X, anchor = NW)
        self.combobox_employee.bind("<<ComboboxSelected>>",\
                                    self.get_employee_index)
        self.book_title_label = Label(self, text = "    Книга:",
                            font = ('Calibri', 12, 'bold'))
        self.book_title_label.pack(anchor = NW)
        self.combobox_book_src = []
        for x in self.books:
            self.combobox_book_src.append(f'{x[1]}, {x[2]}, {x[3]}')
        self.cur_book_sel = StringVar(value = self.combobox_book_src[0])
        self.cur_book_sel.trace('w', self.get_book_index)
        self.combobox_book = ttk.Combobox(self,\
                        font = ('Calibri', 12, 'bold'),
                        values = self.combobox_book_src,\
                        textvariable = self.cur_book_sel)
        self.combobox_book.pack(padx = 10, side = TOP, fill = X, anchor = NW)
        self.combobox_book.bind("<<ComboboxSelected>>", self.get_book_index)
        self.btn = Button(self, text = "Добавить в корзину",
                            command = self.add_to_basket)
        self.btn.pack(pady = 10)

    def get_book_index(self, *args):
        self.book_index = self.combobox_book.current()

    def get_employee_index(self, *args):
        self.employee_index = self.combobox_employee.current()

    def add_to_basket(self):
        self.parent.cur_books.append(self.books[self.book_index])
        if self.parent.cur_employee == -1:
            self.parent.cur_employee = self.employees[self.employee_index][0]
        print('\a')

        bg_clr = self.btn.cget('bg')
        fg_clr = self.btn.cget('fg')
        txt = self.btn.cget('text')
        def set_back_btn():
            self.btn.config(bg = bg_clr, fg = fg_clr, text = txt)
        self.btn.config(bg = 'red', fg = 'yellow', text = 'Добавлено')
        self.btn.after(1000, set_back_btn)
