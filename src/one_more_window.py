import tkinter
from tkinter import *
import src.shluzzz


class OneMoreWindow(Tk):
    def __init__(self):
        super().__init__()

        self.title = "one more tkinter"
        self.geometry('350x450')

        self.city_box = None
        self.label = None
        self.city = 'City'

        self.make_window()

    def make_window(self):

        def click_button():
            src.shluzzz.unsubscribe(self)
            src.shluzzz.subscribe(self)

        frame = Frame(bg='purple')
        frame.place(relwidth=1, relheight=1)

        self.label = Label(bg='purple', text='Погодная информация', font=("Arial", 12))
        self.label.place(relx=0.5, rely=0.2, anchor="s", width=290, height=50)

        button = Button(text='Подписаться на погоду', bg='purple', command=click_button)
        button.place(relx=0.5, rely=0.8, anchor="center", width=190, height=25)

    def update_label(self, data):
        self.label['text'] = data

    def run(self):
        self.mainloop()