from tkinter import *
from themes_factory import WidgetLightThemeFactory, WidgetDarkThemeFactory
from tkinter.messagebox import showinfo
import weather_finder


class Window(Tk):
    def __init__(self):
        super().__init__()

        self.factory = WidgetLightThemeFactory

        self.make_window(self.factory)

    def change_factory(self, factory):
        if factory == WidgetLightThemeFactory:
            self.factory = WidgetDarkThemeFactory
        else:
            self.factory = WidgetLightThemeFactory
        self.make_window(self.factory)

    def make_window(self, factory):
        frame = factory().get_frame()
        label = factory().get_label()
        city_box = factory().get_list_box()

        def get_weather():
            index = city_box.curselection()
            if not index:
                showinfo(title='No city', message='Выберите город')
            else:
                data = weather_finder.get_weather(city_box.get(index))
                label['text'] = f'температура: {data[0]},' \
                                f' влажность: {data[1]},\n ' \
                                f'давление: {data[2]}, ' \
                                f'скорость ветра{data[3]}'

        def update(data):
            label['text'] = f'температура: {data[0]}, ' \
                            f'влажность: {data[1]}, ' \
                            f'давление: {data[2]}, ' \
                            f'скорость ветра{data[3]}'

        def change_style():
            self.change_factory(self.factory)

        frame.place(relwidth=1, relheight=1)

        button_update = Button(frame, text='Посмотреть погоду', font=80, command=get_weather)
        button_update.place(relx=0.5, rely=0.7, anchor="center", width=190, height=25)

        button_change_style = Button(frame, text='Поменять стиль', font=(0, 8), command=change_style)
        button_change_style.place(relx=0.5, rely=0.9, anchor="s", width=190, height=25)

        label.place(relx=0.5, rely=0.2, anchor="s", width=290, height=50)

        city_box.place(relx=0.5, rely=0.4, anchor="center", width=90, height=125)


































#
# def start_app():
#     c
#
#     canvas = Canvas(root, height=200, width=200, bg='green', bd=0)
#     canvas.pack()
#
#     frame = Frame(canvas, bg='black')
#     frame.place(relx=0.25, rely=0.9, relheight=0.7, relwidth=0.5)
#
#
#     root.mainloop()
#
# start_app()




# # Эта библиотека нужна для работы с отправкой URL запросов
# import requests
#
# # Создаем главный объект (по сути окно приложения)
# root = Tk()
#
#
# # Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
# def get_weather():
#     # Получаем данные от пользователя
#     city = cityField.get()

    # # данные о погоде будем брать с сайта openweathermap.org
    # # ниже пропишите свой API ключ, который получите в кабинете пользователя на сайте openweathermap.org
    # key = 'ВАШ КЛЮЧ'
    # # ссылка, с которой мы получим все данные в формате JSON
    # url = 'http://api.openweathermap.org/data/2.5/weather'
    # # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
    # params = {'APPID': key, 'q': city, 'units': 'metric'}
    # # Отправляем запрос по определенному URL
    # result = requests.get(url, params=params)
    # # Получаем JSON ответ по этому URL
    # weather = result.json()

#     # Полученные данные добавляем в текстовую надпись для отображения пользователю
#     info['text'] = f'{city} 777'
#
#
# # Настройки главного окна
#
# # Указываем фоновый цвет
# root['bg'] = '#fafafa'
# # Указываем название окна
# root.title('Погодное приложение')
# # Указываем размеры окна
# root.geometry('300x250')
# # Делаем невозможным менять размеры окна
# root.resizable(width=False, height=False)
#
# # Создаем фрейм (область для размещения других объектов)
# # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
# frame_top = Frame(root, bg='#ffb700', bd=5)
# # Также указываем его расположение
# frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
#
# # Все то-же самое, но для второго фрейма
# frame_bottom = Frame(root, bg='#ffb700', bd=5)
# frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
#
# # Создаем текстовое поле для получения данных от пользователя
# cityField = Entry(frame_top, bg='white', font=30)
# cityField.pack()  # Размещение этого объекта, всегда нужно прописывать
#
# # Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
# btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
# btn.pack()
#
# # Создаем текстовую надпись, в которую будет выводиться информация о погоде
# info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
# info.pack()
#
# # Запускаем постоянный цикл, чтобы программа работала
# root.mainloop()