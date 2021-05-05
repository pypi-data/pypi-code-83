import sys, os

BASE_DIR = os.path.abspath (os.path.dirname (__file__))

def __config__ (pref):
    import skitai
    from config import settings

    skitai.mount (settings.STATIC_URL, os.path.join (BASE_DIR, 'static'))
    skitai.log_off (settings.STATIC_URL)
    pref.config.SETTINGS = settings
