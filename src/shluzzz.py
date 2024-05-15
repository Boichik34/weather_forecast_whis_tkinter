from src.observer import Apps


def subscribe(app):
    Apps.add(app)


def unsubscribe(app):
    Apps.remove(app)
