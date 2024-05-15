from abc import ABC, abstractmethod
from tkinter import *


class IWidgetFactory(ABC):
    @abstractmethod
    def create_frame(self): pass

    @abstractmethod
    def create_weather_button(self, command): pass

    @abstractmethod
    def create_city_box(self): pass

    @abstractmethod
    def create_label(self): pass

    @abstractmethod
    def create_style_button(self, command): pass


class LightWidgetFactory(IWidgetFactory):
    def create_frame(self):
        return LightFrameProduct()

    def create_weather_button(self, command):
        return LightButtonWeatherProduct(command)

    def create_city_box(self):
        return LightListboxProduct()

    def create_label(self):
        return LightLabelProduct()

    def create_style_button(self, command):
        return LightButtonStyleProduct(command)


class DarkWidgetFactory(IWidgetFactory):
    def create_frame(self):
        return DarkFrameProduct()

    def create_weather_button(self, command):
        return DarkButtonWeatherProduct(command)

    def create_city_box(self):
        return DarkListboxProduct()

    def create_label(self):
        return DarkLabelProduct()

    def create_style_button(self, command):
        return DarkButtonStyleProduct(command)


class IFrameProduct(Frame):
    def __init__(self):
        super().__init__()


class IButtonWeatherProduct(Button):
    def __init__(self):
        super().__init__()


class IListboxProduct(Listbox):
    def __init__(self):
        super().__init__()


class ILabelProduct(Label):
    def __init__(self):
        super().__init__()


class IButtonStyleProduct(Button):
    def __init__(self):
        super().__init__()


class LightButtonWeatherProduct(IButtonWeatherProduct):
    def __init__(self, command):
        super().__init__()
        self.configure(text='Показать погоду', bg="orange", command=command)
        self.place(relx=0.5, rely=0.7, anchor="center", width=190, height=25)


class DarkButtonWeatherProduct(IButtonWeatherProduct):
    def __init__(self, command):
        super().__init__()
        self.configure(text='Показать погоду', bg="#edba13", command=command)
        self.place(relx=0.5, rely=0.7, anchor="center", width=190, height=25)


class LightButtonStyleProduct(IButtonStyleProduct):
    def __init__(self, command):
        super().__init__()
        self.configure(text='Поменять стиль', bg="orange", command=command)
        self.place(relx=0.5, rely=0.8, anchor="center", width=190, height=25)


class DarkButtonStyleProduct(IButtonStyleProduct):
    def __init__(self, command):
        super().__init__()
        self.configure(text='Поменять стиль', bg="#edba13", command=command)
        self.place(relx=0.5, rely=0.8, anchor="center", width=190, height=25)


class LightFrameProduct(IFrameProduct):
    def __init__(self):
        super().__init__()
        self.configure(bg="green")
        self.place(relwidth=1, relheight=1)


class DarkFrameProduct(IFrameProduct):
    def __init__(self):
        super().__init__()
        self.configure(bg='#4C1C24')
        self.place(relwidth=1, relheight=1)


class LightListboxProduct(IListboxProduct):
    def __init__(self):
        super().__init__()
        self.lst = Variable(value=['Volgograd', 'Paris', 'London',
                                   'New-York', 'Kazan', 'Vladivostok',
                                   'Volzhsky', 'Kamyshin'])
        self.configure(bg="yellow", listvariable=self.lst)
        self.place(relx=0.5, rely=0.4, anchor="center", width=90, height=132)


class DarkListboxProduct(IListboxProduct):
    def __init__(self):
        super().__init__()
        self.lst = Variable(value=['Volgograd', 'Paris', 'London',
                                   'New-York', 'Kazan', 'Vladivostok',
                                   'Volzhsky', 'Kamyshin'])
        self.configure(bg='#edba13', listvariable=self.lst)
        self.place(relx=0.5, rely=0.4, anchor="center", width=90, height=132)


class LightLabelProduct(ILabelProduct):
    def __init__(self):
        super().__init__()
        self.configure(text='Погодная информация', bg='yellow', font=("Arial", 12))
        self.place(relx=0.5, rely=0.2, anchor="s", width=290, height=50)


class DarkLabelProduct(ILabelProduct):
    def __init__(self):
        super().__init__()
        self.configure(text='Погодная информация', bg='#edba13', font=("Arial", 12))
        self.place(relx=0.5, rely=0.2, anchor="s", width=290, height=50)

