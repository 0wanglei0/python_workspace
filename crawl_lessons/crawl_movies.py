import tkinter.messagebox as msgbox
import tkinter as tk
import webbrowser
import re
import json
import os
from urllib import parse


class App:
    def __init__(self, width=500, height = 300):
        self.w = width
        self.h = height
        self.title = "VIP视频获取"
        self.root= tk.Tk(className=self.title)
        self.url = tk.StringVar()
        self.v = tk.IntVar()
        self.v.set(1)

        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)
        frame_3 = tk.Frame(self.root)

        menu = tk.Menu(self.root)
        self.root.config(menu = menu)
        file_menu = tk.Menu(menu, tearoff=0)
        movie_menu = tk.Menu(menu, tearoff=0)

        group = tk.Label(frame_1, text="play channel choose", padx=10, pady=10)
        tb1 = tk.Radiobutton(frame_1, text="网通", variable=self.v, value=1, width=10, height=3)
        tb2 = tk.Radiobutton(frame_1, text="电信", variable=self.v, value=1, width=10, height=3)
        label1 = tk.Label(frame_2, text="play address")
        entry = tk.Entry(frame_2, textvariable=self.url, highlightcolor='Fuchsia', highlightthickness=1, width=35)
        label2 = tk.Label(frame_2, text=" ")
        play = tk.Button(frame_2, text="play with Computer", font=("黑体", 12), fg='Purple', width = 8, height=1, command=self.video_play)
        label3 = tk.Label(frame_2, text=" ")
        # Qr_code = tk.Button(frame_3, text="play with Phone", font=("黑体", 12), fg='Purple', width = 8, height=1, command=self.Qr_code_play)
        label_explain = tk.Label(frame_3, text="--------", font=("黑体", 12), fg='Green')

        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        group.grid(row=0, column=0)
        tb1.grid(row=0, column=1)
        tb2.grid(row=0, column=2)
        label1.grid(row=0, column=0)
        label2.grid(row=0, column=2)
        label3.grid(row=0, column=4)
        entry.grid(row=0, column=1)
        play.grid(row=0, column=3, ipadx=10, ipady=10)
        # Qr_code.grid(row=0, column=0)
        label_explain.grid(row=1, column=0)

    def loads_jsonp(self, _jsonp):
        try:
            _json = json.loads(re.match(".*?({.*}).*", _jsonp, re.S).group(1))
            return _json
        except:
            raise ValueError("invalid input")

    def video_play(self):
        port1 = 'https://jx.aidouer.net/?url='
        port2 = 'http://www.vipjiexi.com/tong.php/url='

        if re.match(r'^https?:/{2}\w.+$', self.url.get()):
            if self.v.get() == 1:
                ip = self.url.get()
                ip = parse.quote_plus(ip)
                webbrowser.open(port2 + self.url.get())
            elif self.v.get() == 2:
                ip = self.url.get()
                ip = parse.quote_plus(ip)


    def center(self):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = int((ws/ 2) - (self.w / 2))
        y = int((hs/ 2) - (self.h / 2))
        self.root.geometry('{}x{}+{}+{}'.format(self.w, self.h, x, y))

    def loop(self):
        self.root.resizable(False, False)
        self.center()
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.loop()
