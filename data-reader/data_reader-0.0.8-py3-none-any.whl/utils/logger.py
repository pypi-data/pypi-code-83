from datetime import datetime


class Logger:

    @staticmethod
    def info(text):
        text = f'[{Logger.__get_datetime()}][info] {text}'
        print(text)

    @staticmethod
    def success(text):
        text = f'{Logger.__green()}[{Logger.__get_datetime()}][success] {text}{Logger.__end()}'
        print(text)

    @staticmethod
    def error(text):
        text = f'{Logger.__red()}[{Logger.__get_datetime()}][error] {text}{Logger.__end()}'
        print(text)

    @staticmethod
    def warning(text):
        text = f'{Logger.__yellow()}[{Logger.__get_datetime()}][warning] {text}{Logger.__end()}'
        print(text)

    @staticmethod
    def __green():
        return '\x1b[42m'

    @staticmethod
    def __red():
        return '\x1b[41m'

    @staticmethod
    def __yellow():
        return '\x1b[43m'

    @staticmethod
    def __end():
        return '\x1B[0m'

    @staticmethod
    def __get_datetime():
        return '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
