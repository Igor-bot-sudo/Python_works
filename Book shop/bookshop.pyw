from tkinter import *
import sqlite3
from tools.newbook import *
from tools.deletebook import *
from tools.findbook import *
from tools.editbook import *
from tools.purchasebook import *
from tools.employees import *
from tools.basketwindow import *
from tools.accounting import *


with sqlite3.connect("bookshop.db") as con:
    cur = con.cursor()
    sqlite_query = '''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                book_title TEXT,
                author TEXT,
                price INTEGER
            );

            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                employee_name TEXT
            );
        '''
    cur.executescript(sqlite_query)


class App(Tk):
    def __init__(self):
        super().__init__()

        self.cur_books = []
        self.cur_employee = -1
        self.resizable(0, 0)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width, height = 450, 450
        x = (screen_width//2) - (width//2)
        y = (screen_height//2) - (height//2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.title('Книжный магазин')
        Label(self, text = "Главное меню", fg = 'green',
                font = ('Calibri', 18, 'bold')).pack(pady = 10)
        self.btn1 = Button(self, text = "Добавить новую книгу в БД",\
                        width = 30, font = ('Calibri', 14, 'bold'),\
                        command = lambda: NewBookWindow(self).grab_set())
        self.btn1.pack(pady = 4)
        self.btn2 = Button(self, text = "Удалить книгу из БД", width = 30,
                        font = ('Calibri', 14, 'bold'),\
                        command = lambda: DeleteBookWindow(self).grab_set())
        self.btn2.pack(pady = 4)
        self.btn3 = Button(self, text = "Поиск книг", width = 30,
                        font = ('Calibri', 14, 'bold'),
                        command = lambda: FindBookWindow(self).grab_set())
        self.btn3.pack(pady = 4)
        self.btn4 = Button(self, text = "Редактирование данных", width = 30,
                        font = ('Calibri', 14, 'bold'),\
                        command = lambda: EditBookWindow(self).grab_set())
        self.btn4.pack(pady = 4)
        self.btn5 = Button(self, text = "Покупка", width = 30,
                        font = ('Calibri', 14, 'bold'),\
                        command = lambda: PurchaseBookWindow(self).grab_set())
        self.btn5.pack(pady = 4)
        self.btn6 = Button(self, text = "Корзина", width = 30,
                        font = ('Calibri', 14, 'bold'),\
                        command = lambda: BasketWindow(self).grab_set())
        self.btn6.pack(pady = 4)
        self.btn7 = Button(self, text = "Учет продаж", width = 30,
                        font = ('Calibri', 14, 'bold'),\
                        command = lambda: AccountingWindow(self).grab_set())
        self.btn7.pack(pady = 4)
        self.btn8 = Button(self, text = "Учет сотрудников", width = 30,
                        font = ('Calibri', 14, 'bold'),\
                        command = lambda: EmployeesWindow(self).grab_set())
        self.btn8.pack(pady = 4)


if __name__ == "__main__":
    app = App()
    app.mainloop()
