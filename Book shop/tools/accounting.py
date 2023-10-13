from tkinter import *
import sqlite3


class AccountingWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.cur_employee = parent.cur_employee
        self.resizable(0, 0)
        width, height = 740, 587
        self.geometry(f'{width}x{height}')
        self.title('Учет продаж')

        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            self.sales = cur.execute(
                '''
                    SELECT sale_date, books.book_title, author, price,
                    employees.employee_name FROM sales
                    JOIN books JOIN employees WHERE
                    employees.id = sales.employee_id AND
                    books.id = sales.books_id
                ''').fetchall()

        scroll_bar = Scrollbar(self)
        scroll_bar.grid(row = 1, column = 1, rowspan = 2, sticky = E)

        src = []
        for x in self.sales:
            src.append(f'{x[0]}, {x[1]}, {x[2]}, {x[3]}, {x[4]}')

        result_var = Variable(value = src)
        self.result_list = Listbox(self, height = 36, width = 100,
                            yscrollcommand = scroll_bar.set,\
                            listvariable = result_var)
        self.result_list.grid(row = 2, column = 0, padx = 5, sticky = W)
        scroll_bar.config(command = self.result_list.yview)
