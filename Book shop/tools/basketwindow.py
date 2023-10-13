from tkinter import *
import sqlite3
from datetime import datetime


class BasketWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.resizable(0, 0)
        width, height = 550, 208
        self.geometry(f'{width}x{height}')
        self.title('Корзина')

        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            self.empl = cur.execute(
                "SELECT employee_name FROM employees WHERE id = ?",\
                    (self.parent.cur_employee, )).fetchone()[0]

        if self.parent.cur_employee == -1:
            e = f'    Продавец:'
        else:
            e = f'    Продавец: {self.empl}'

        self.book_title_label = Label(self,
                text = e, font = ('Calibri', 12, 'bold'))
        self.book_title_label.grid(row = 0, column = 0, sticky = W)
        scroll_bar = Scrollbar(self)
        scroll_bar.grid(row = 0, column = 2, rowspan = 2)

        src = []
        for x in self.parent.cur_books:
            src.append(f'{x[1]}, {x[2]}, {x[3]}')

        books_var = Variable(value = src)
        mylist = Listbox(self, listvariable = books_var,
                yscrollcommand = scroll_bar.set, height = 8, width = 75)
        mylist.grid(row = 1, column = 0)

        scroll_bar.config(command = mylist.yview)

        su = '    Сумма: ' + str(sum([x[3]\
                                for x in self.parent.cur_books]))
        sum_label = Label(self, text = su, fg = 'red',
                            font = ('Calibri', 16, 'bold'))
        sum_label.grid(row = 2, column = 0, sticky = W)


        self.btn = Button(self, text = "Ok", width = 5,
                            font = ('Calibri', 14, 'bold'),\
                            command = self.buy)
        self.btn.grid(row = 2, column = 0, pady = 5)

    def buy(self):
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS sales (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    sale_date TEXT,
                    books_id INTEGER,
                    employee_id INTEGER,
                    FOREIGN KEY (books_id) REFERENCES books(id),
                    FOREIGN KEY (employee_id) REFERENCES employees(id)
                );
            ''')

            y, m, d = str(datetime.now().date()).split('-')
            for i in self.parent.cur_books:
                cur.execute("INSERT INTO sales (sale_date, books_id,\
                            employee_id) VALUES (?, ?, ?);",\
                            (f'{d}.{m}.{y}', i[0], self.parent.cur_employee))

        self.parent.cur_books = []
        self.parent.cur_employee = -1
        print('\a')
