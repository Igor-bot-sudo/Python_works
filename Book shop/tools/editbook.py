from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import sqlite3


class EditBookWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            self.books = cur.execute(
                "SELECT * FROM books").fetchall()
        self.index = 0
        self.resizable(0, 0)
        width, height = 750, 160
        self.geometry(f'{width}x{height}')
        self.title('Редактирование данных книги')
        self.book_title_label = Label(self, text = "    Книга:",
                            font = ('Calibri', 12, 'bold'))
        self.book_title_label.pack(anchor = NW)
        self.combobox = ttk.Combobox(self, font = ('Calibri', 12, 'bold'))
        self.combobox.pack(padx = 5, side = TOP, fill = X, anchor = NW)
        self.combobox.bind("<<ComboboxSelected>>", self.get_index)
        self.update_combobox()
        f = Frame(self)
        f.pack(pady = 10)
        author_column_width = 36
        title_column_width = 50
        price_column_width = 5
        header = {'Название книги': title_column_width,\
                'Автор': author_column_width,\
                'Цена': price_column_width}
        i = 0
        self.var = []
        for k, v in header.items():
            l = Label(f, width = v, fg = '#00008b', borderwidth = 2,\
                    relief = GROOVE, font = ('Calibri', 12, 'bold'))
            l.grid(row = 0, column = i)
            l['text'] = k
            self.var.append(StringVar())
            e = Entry(f, width = v, font = ('Calibri', 12, 'bold'),\
                    textvariable = self.var[i])
            e.grid(row = 1, column = i)
            i += 1
        self.btn = Button(self, text = "Изменить",
                            command = self.edit_book)
        self.btn.pack(pady = 5)

    def get_index(self, *args):
        self.index = self.combobox.current()
        for i in range(1, len(self.books[self.index])):
            self.var[i - 1].set(self.books[self.index][i])

    def update_combobox(self):
        self.books = sorted(self.books, key = lambda item: item[3])
        self.combobox_src = []
        for x in self.books:
            self.combobox_src.append(f'{x[1]}, {x[2]}, {x[3]}')
        self.combobox.config(values = self.combobox_src)
        self.combobox.set(self.combobox_src[0])

    def edit_book(self):
        title = self.var[0].get()
        author = self.var[1].get()
        price = self.var[2].get()
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            cur.execute(
                "UPDATE books SET book_title = ?, author = ?,\
                price = ? WHERE\
                book_title = ? AND author = ?;", (title, author, price,\
                            self.books[self.index][1],\
                            self.books[self.index][2]))
        self.books[self.index] = (self.books[self.index][0], title,\
                                author, int(price))
        self.update_combobox()
        [x.set('') for x in self.var]
        showinfo('', f'Изменения внесены в БД')
