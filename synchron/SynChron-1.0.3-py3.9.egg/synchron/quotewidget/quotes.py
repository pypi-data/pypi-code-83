import json
import random
from pkg_resources import resource_filename
from os import path
cwd = path.dirname(__file__)
package_name = "synchronicity"
import quotes_list

try:
    from .. import utils
except:
    from synchron import utils

def get_random_quote():
    return random.choice(quotes_list.quotes)

def create_random_tweet():
    quote = get_random_quote()
    tweet = """{} - {}""".format(quote['quoteText'], quote['quoteAuthor'])
    return tweet

def test():
    print("Test quotes.")

def get_update():
    return {'tweet':create_random_tweet()}

def get_multiple(count=1):
    res = []
    for i in range(count):
        res.append(get_update())
    return res
    
if(__name__ == "__main__"):
    print("Running in: "+cwd)
    print(get_update())