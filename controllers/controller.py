import aiohttp
from functools import wraps


class Controller:
    def __init__(self):
        None
    @staticmethod
    def authorized(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if 1 == 2:
                return f(*args, **kwargs)
            else:
                print('Acesso inválido')
        return wrapper