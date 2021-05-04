import os
from dotenv import load_dotenv

from functools import wraps

load_dotenv()


def check_api_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_token = ""
        if "api_token" in kwargs:
            return func(*args, **kwargs)
        elif args[-1] is not None:
            return func(*args, **kwargs)
        elif os.getenv("DROPBOX_API_TOKEN"):
            api_token = os.getenv("DROPBOX_API_TOKEN")
            new_args = list(args[:])
            new_args[-1] = api_token
            return func(*new_args, **kwargs)
        else:
            raise TypeError

    return wrapper
