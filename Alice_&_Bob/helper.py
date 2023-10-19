from tkinter import *
import sqlite3
import socket
from threading import Thread
from utils.caesar import *
from utils.atbash import *
from utils.keyword import *
from utils.vernam import *


HOST = "127.0.0.1"
PORT = 65432


class Receiver(Thread):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            while True:
                conn, addr = s.accept()
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        t = data.decode('utf-8').split('&')
                        self.parent.recv_msg['text'] = t[0]
                        self.parent.algorithm = t[1]
                        conn.sendall(b"Decrypted")


class App(Tk):
    def __init__(self):
        super().__init__()
        self.algorithm = ''

        with sqlite3.connect("messages.db") as con:
            cur = con.cursor()
            sqlite_query = '''
                    CREATE TABLE IF NOT EXISTS encrypted (
                        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        algorithm TEXT,
                        msg_text TEXT
                    );

                    CREATE TABLE IF NOT EXISTS decrypted (
                        msg_id INTEGER,
                        msg_text TEXT,
                        FOREIGN KEY (msg_id) REFERENCES encrypted(id)
                    );
                '''
            cur.executescript(sqlite_query)

        self.resizable(0, 0)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width, height = 450, 395
        x = (screen_width//4) - (width//2)
        y = (screen_height//2) - (height//2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.title('Боб')

        self.recv_label = Label(self, fg = 'green',\
                                text = "Принятое сообщение:",\
                                font = ('Calibri', 12, 'bold'))
        self.recv_label.grid(row = 0, column = 0, sticky = W)
        self.recv_label.pack()

        self.recv_msg = Label(self, bg = 'white', font = ('Calibri', 12, 'bold'),\
                            wraplength = 440, anchor = NW, justify = LEFT, width = 440, height = 8)
        self.recv_msg.pack(padx = 5)

        self.btn = Button(self, text = "Расшифровать", width = 30,\
                        font = ('Calibri', 14, 'bold'),\
                        command = self.decrypt_message)
        self.btn.pack(pady = 5)

        self.decrypted_msg = Label(self, bg = 'white',\
                            font = ('Calibri', 12, 'bold'),\
                            wraplength = 440, anchor = NW, justify = LEFT,\
                            width = 440, height = 8)
        self.decrypted_msg.pack(padx = 5)

        Receiver(self).start()

    def decrypt_message(self):
        if self.algorithm == 'Caesar':
            c = Caesar(5)
        elif self.algorithm == 'Atbash':
            c = Atbash()
        elif self.algorithm == 'Keyword':
            c = KeyWord('Секрет')
        else:
            c = Vernam()
        self.decrypted_msg['text'] = c.decode(self.recv_msg.cget("text"))
        self.update_db()

    def update_db(self):
        with sqlite3.connect("messages.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO encrypted (algorithm, msg_text) VALUES (?, ?);",\
                (self.algorithm, self.recv_msg.cget("text")))
            msg_id = cur.execute(
                "SELECT COUNT(*) FROM encrypted;").fetchone()[0]
            cur.execute(
                "INSERT INTO decrypted (msg_id, msg_text) VALUES (?, ?);",\
                (msg_id, self.decrypted_msg.cget("text")))


if __name__ == "__main__":
    app = App()
    app.mainloop()
