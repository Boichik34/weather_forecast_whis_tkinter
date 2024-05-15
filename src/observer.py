from abc import ABC, abstractmethod
from src.shluzzz_in_app import mailing


class IWeatherMakerSubject(ABC):
    @abstractmethod
    def attach(self, app): pass

    @abstractmethod
    def detach(self, app): pass

    @abstractmethod
    def notify(self): pass


class IWeatherMaker(ABC):
    @abstractmethod
    def get_weather(self, city): pass


class WeatherMaker(IWeatherMakerSubject, IWeatherMaker):
    def __init__(self):
        super().__init__()
        self.observer_list = []

    def attach(self, app):
        if app in self.observer_list:
            return
        self.observer_list.append(app)
        self.notify()

    def detach(self, app):
        if app not in self.observer_list:
            return
        self.observer_list.remove(app)

    def notify(self):
        if not self.observer_list:
            return
        for observer in self.observer_list:
            Apps.update(observer)

    def get_weather(self, city):
        data = f'в горде {city} погода норм'
        return data


class IApp(ABC):
    @staticmethod
    @abstractmethod
    def update(app): pass


class Apps(IApp):

    @staticmethod
    def update(app):
        weather = weather_maker.get_weather(app.city)
        mailing(app, weather)

    @staticmethod
    def add(app):
        weather_maker.attach(app)

    @staticmethod
    def remove(app):
        weather_maker.detach(app)


weather_maker = WeatherMaker()
