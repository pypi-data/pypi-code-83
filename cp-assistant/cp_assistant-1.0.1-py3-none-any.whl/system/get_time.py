from datetime import datetime
import time


def get_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def digital_time():
    try:
        return time.strftime("%B %d, %Y %-I:%M %p")
    except:
        return get_time()


if __name__ == "__main__":
    print(get_time())
    print(digital_time())
