from abc import ABC, abstractmethod
from tkinter import *
import weather_finder


class IWidgetFactory(ABC):
    @abstractmethod
    def get_frame(self): pass

    @abstractmethod
    def get_list_box(self): pass

    @abstractmethod
    def get_entry(self): pass

    @abstractmethod
    def get_label(self): pass


class WidgetLightThemeFactory(IWidgetFactory):
    def get_frame(self):
        return LightThemeFrameProduct().create_frame()

    def get_list_box(self):
        return LightThemeListBoxProduct().create_list_box()

    def get_entry(self):
        return LightThemeEntryProduct().create_entry()

    def get_label(self):
        return LightThemeLabelProduct().create_label()


class WidgetDarkThemeFactory(IWidgetFactory):
    def get_frame(self):
        return DarkThemeFrameProduct().create_frame()

    def get_list_box(self):
        return DarkThemeListBoxProduct().create_list_box()

    def get_entry(self):
        return DarkThemeEntryProduct().create_entry()

    def get_label(self):
        return DarkThemeLabelProduct().create_label()


class AButtonsProduct(ABC):
    @abstractmethod
    def create_list_box(self): pass


class AEntryProduct(ABC):
    @abstractmethod
    def create_entry(self): pass


class ALabelProduct(ABC):
    @abstractmethod
    def create_label(self): pass


class AFrameProduct(ABC):
    @abstractmethod
    def create_frame(self): pass


class DarkThemeListBoxProduct(AButtonsProduct):
    def create_list_box(self):
        city = Variable(value=['Volgograd', 'Paris', 'London', 'New-York', 'Kazan'])
        city_box = Listbox(listvariable=city, bg='grey')
        return city_box


class LightThemeListBoxProduct(AButtonsProduct):
    def create_list_box(self):
        city = Variable(value=['Volgograd', 'Paris', 'London', 'New-York', 'Kazan'])
        city_box = Listbox(listvariable=city, bg='white')
        return city_box


class DarkThemeLabelProduct(ALabelProduct):
    def create_label(self):
        label = Label(text='Погодная информация', bg='grey', font=('Arial', 13))
        return label


class LightThemeLabelProduct(ALabelProduct):
    def create_label(self):
        label = Label(text='Погодная информация', bg='white', font=('Arial', 12))
        return label


class DarkThemeEntryProduct(AEntryProduct):
    def create_entry(self):
        entry = Entry(bg='grey', font=20)
        return entry


class LightThemeEntryProduct(AEntryProduct):
    def create_entry(self):
        entry = Entry(bg='white', font=20)
        return entry


class DarkThemeFrameProduct(AFrameProduct):
    def create_frame(self):
        frame = Frame(bg='grey', bd=5)
        return frame


class LightThemeFrameProduct(AFrameProduct):
    def create_frame(self):
        frame = Frame(bg='white', bd=5)
        return frame