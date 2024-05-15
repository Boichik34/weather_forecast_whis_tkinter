from tkinter import *
from tkinter.messagebox import showinfo
from src.themes_factory import LightWidgetFactory, DarkWidgetFactory
import src.shluzzz


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.title = "tkinter"
        self.geometry('350x450')
        self.factory = LightWidgetFactory()

        self.city_box = None
        self.label = None
        self.city = None

        self.make_window(self.factory)

    def make_window(self, factory):
        factory.create_frame()
        factory.create_weather_button(self.get_weather)
        factory.create_style_button(self.change_style)
        self.city_box = factory.create_city_box()
        self.label = factory.create_label()

    def change_style(self):
        if self.factory.__class__ == LightWidgetFactory:
            self.factory = DarkWidgetFactory()
        else:
            self.factory = LightWidgetFactory()

        self.make_window(self.factory)

    def get_weather(self):
        index = self.city_box.curselection()
        if not index:
            showinfo(title='No city', message='Выберите город')
        else:
            self.city = self.city_box.get(index)

            src.shluzzz.unsubscribe(self)
            src.shluzzz.subscribe(self)

    def update_label(self, data):
        self.label['text'] = data

    def run(self):
        self.mainloop()
