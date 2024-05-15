from src.observer import weather_maker


def subscribe(app):
    weather_maker.attach(app)


def unsubscribe(app):
    weather_maker.detach(app)
