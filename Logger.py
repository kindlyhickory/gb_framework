import time
import datetime

from reusepatterns.singletones import SingletonByName


class Logger(metaclass=SingletonByName):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        with open(f'{self.name}_log.txt', 'w+', encoding='utf-8') as f:
            f.write(f'{text} - {datetime.datetime.now()}')
            print(f'log {text}')


def debug(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('DEBUG:', func.__name__, end - start)
        return result
    return wrapper
