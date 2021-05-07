from time import sleep
import random, sys
from pydventure.variables import WRITING_SLEEP_DURATION

def writing_sleep():
    """
        return a random sleep time between 0 and the writing speed variable
    """
    return sleep(random.uniform(0.001, WRITING_SLEEP_DURATION))


def write(text, interactive=False):
    """
        Display provided text with typing effect. 
        If <interactive> set to True, it will prompt input and return Player command.

        :param text: str
        :param interactive: Boolean
        :return: nothing or str based on interactive param
    """
    # for char in text:
    #     writing_sleep()
    #     sys.stdout.write(char)
    #     sys.stdout.flush()
    sys.stdout.write(text)
    print("")
    if interactive:
        writing_sleep()
        te = str(input(">> "))
        return te
    return 