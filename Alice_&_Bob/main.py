from tkinter import *
from random import randint
import socket
import os
import asyncio
from utils.caesar import *
from utils.atbash import *
from utils.keyword import *
from utils.vernam import *


HOST = "127.0.0.1"
PORT = 65432


class App(Tk):
    def __init__(self):
        super().__init__()
        self.algorithms = ('Caesar', 'Atbash', 'Keyword', 'Vernam')
        self.msg = ''
        self.algorithm = 0

        with open('quotes.txt', encoding = "utf-8") as f:
            self.quotes = f.read().split('\n\n')

        self.resizable(0, 0)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width, height = 450, 395
        x = (screen_width*3//4) - (width//2)
        y = (screen_height//2) - (height//2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        self.title('Алиса')
        self.send_label = Label(self, fg = 'green',\
                                text = "Сообщение:",\
                                font = ('Calibri', 12, 'bold'))
        self.send_label.pack(pady = 5)
        self.send_msg = Label(self, bg = 'white',\
                            font = ('Calibri', 12, 'bold'),\
                            wraplength = 440, anchor = NW,\
                            justify = LEFT, width = 440, height = 9)
        self.send_msg.pack(padx = 5)
        self.btn = Button(self, text = "Отправить",\
                        width = 30, font = ('Calibri', 14, 'bold'),\
                        command = self.send_message)
        self.btn.pack(pady = 5)

        self.update()

        async def start_helper():  
            await asyncio.create_subprocess_exec('python',\
                            os.getcwd() + '/helper.py', shell = False)                      
        asyncio.run(start_helper())

    def send_message(self):
        if self.algorithm == 0:
            c = Caesar(5)
        elif self.algorithm == 1:
            c = Atbash()
        elif self.algorithm == 2:
            c = KeyWord('Секрет')
        else:
            c = Vernam()

        enrypted_msg = c.encode(self.msg.replace('\n', ' ')) + '&'\
            + self.algorithms[self.algorithm]

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(bytes(enrypted_msg, 'utf-8'))
            s.recv(1024)

        self.update()

    def update(self):
        i = randint(0, len(self.quotes)-1)
        self.msg = self.quotes[i]
        self.send_msg['text'] = self.msg
        self.algorithm = randint(0, len(self.algorithms)-1)
        crypt_title = ('Цезаря', 'Атбаш', 'Ключевое слово', 'Вернама')
        self.send_label['text'] = f'Шифр {crypt_title[self.algorithm]}'

if __name__ == "__main__":
    app = App()
    app.mainloop()
