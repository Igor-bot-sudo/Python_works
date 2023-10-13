from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import sqlite3


class EmployeesWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            self.res = cur.execute(
                "SELECT * FROM employees").fetchall()
        self.employee_index = 0
        self.resizable(0, 0)
        width, height = 800, 194
        self.geometry(f'{width}x{height}')
        self.title('Продавцы')
        self.title_label = Label(self, text = "    Сотрудник:",
                            font = ('Calibri', 12, 'bold'))
        self.title_label.pack(anchor = NW)

        self.combobox_src = []
        for x in self.res:
            self.combobox_src.append(f'{x[1]}')
        self.cur_sel = StringVar(value = self.combobox_src[0])
        self.cur_sel.trace('w', self.get_index)
        self.combobox = ttk.Combobox(self, font = ('Calibri', 12, 'bold'),
                        values = self.combobox_src,\
                        textvariable = self.cur_sel)
        self.combobox.pack(padx = 10, side = TOP, fill = X, anchor = NW)
        self.combobox.bind("<<ComboboxSelected>>", self.get_index)
        self.delete_btn = Button(self, text = "Удалить данные сотрудника",
                            command = self.delete_employee)
        self.delete_btn.pack(pady = 10)
        self.add_employee_label = Label(self,\
                            text = "    Добавление сотрудника, Ф.И.О.:",
                            font = ('Calibri', 12, 'bold'))
        self.add_employee_label.pack(anchor = NW)
        self.employee_var = StringVar()
        self.employee_entry = Entry(self, font = ('Calibri', 12, 'bold'),\
                                    width = 50,\
                                    textvariable = self.employee_var)
        self.employee_entry.pack(padx = 10, side = TOP, anchor = NW,\
                                fill = X)
        self.add_btn = Button(self, text = "Добавить сотрудника",
                            command = self.add_employee)
        self.add_btn.pack(pady = 10)

    def get_index(self, *args):
        self.employee_index = self.combobox.current()

    def delete_employee(self):
        cs = self.cur_sel.get()
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            cur.execute(
                "DELETE FROM employees WHERE employee_name = ?",\
                (cs, ))
        del self.combobox_src[self.employee_index]
        self.cur_sel.set('')
        self.combobox.config(values = self.combobox_src)
        showinfo('', f'Данные сотрудника {cs} удалены из БД')

    def add_employee(self):
        cs = self.employee_var.get()
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO employees (employee_name) VALUES (?)",\
                (cs, ))
        self.combobox_src.append(cs)
        self.combobox.config(values = self.combobox_src)
        showinfo('', f'Данные сотрудника {cs} добавлены в БД')
