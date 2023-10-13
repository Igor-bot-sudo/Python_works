from tkinter import *
from tkinter.messagebox import showerror, showinfo
import sqlite3


class NewBookWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.resizable(0, 0)
        width, height = 500, 200
        self.geometry(f'{width}x{height}')
        self.title('Новая книга')
        self.book_title_label = Label(self, text = "    Название книги:",
                            font = ('Calibri', 12, 'bold'))
        self.book_title_label.pack(anchor = NW)
        self.book_title_var = StringVar()
        self.book_title_entry = Entry(self, font = ('Calibri', 12, 'bold'),
                                    textvariable = self.book_title_var)
        self.book_title_entry.pack(padx = 10, side = TOP, fill = X,\
                            anchor = NW)
        self.author_label = Label(self, text = "    Автор:",
                            font = ('Calibri', 12, 'bold'))
        self.author_label.pack(anchor = NW)
        self.author_var = StringVar()
        self.author_entry = Entry(self, font = ('Calibri', 12, 'bold'),
                                    textvariable = self.author_var)
        self.author_entry.pack(padx = 10, side = TOP, fill = X, anchor = NW)
        self.price_label = Label(self, text = "    Стоимость книги:",
                            font = ('Calibri', 12, 'bold'))
        self.price_label.pack(anchor = NW)
        self.price_var = IntVar()
        self.price_entry = Entry(self, font = ('Calibri', 12, 'bold'),
                                    textvariable = self.price_var)
        self.price_entry.pack(padx = 10, side = TOP, fill = X, anchor = NW)
        self.add_btn = Button(self, text = "Добавить",
                            command = self.add_book)
        self.add_btn.pack(padx = 10, pady = 10)

    def add_book(self):
        title = self.book_title_var.get()
        author = self.author_var.get()
        price = self.price_var.get()
        with sqlite3.connect("bookshop.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO books (book_title, author, price)\
                VALUES (?, ?, ?)", (title, author, price))
        showinfo('', f'Книга {title} автора {author} добавлена в БД')
        self.book_title_var.set(value = '')
        self.author_var.set(value = '')
        self.price_var.set(value = '')
