import time
import datetime

from reusepatterns.singletones import SingletonByName


class ConsoleWriter:

    @staticmethod
    def write(text):
        print(f'CONSOLE LOGGER ---> {text}')


class FileWriter:

    def __init__(self, name):
        self.name = name

    def write(self, text):
        with open(f'{self.name}_log.txt', 'w+', encoding='utf-8') as f:
            f.write(f'{text} - {datetime.datetime.now()}')
            print(f'log {text}')


class Logger(metaclass=SingletonByName):

    def __init__(self, name, writer=ConsoleWriter):
        self.name = name
        self.writer = writer

    def log(self, text):
        self.writer.write(text)


def debug(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('DEBUG:', func.__name__, end - start)
        return result

    return wrapper
