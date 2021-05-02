"""Get information on langauges from pycountry."""
from pycountry import languages


def get_lang_dict():
    """Get a dict with code: name for each language that is in pycountry.

    Returns:
        dict: code: name for each alpha_3 code in pycountry
    """
    langdict = {}
    for lang in languages:
        langdict[lang.alpha_3] = lang.name
    return langdict


def get_available_languages(message_location):
    """Get a dict with code: name for each language that is in pycountry.

    Args:
        message_location (str): path to messages.  Example: /path/{}.json

    Returns:
        list: list of valid lanuages that have a file in messagelocation.
    """
    available_languages = []
    for langcode in get_lang_dict():
        try:
            open(message_location.format(langcode), 'r')
            available_languages.append(langcode)
        except (OSError, IOError):  # https://stackoverflow.com/a/15032444
            pass
    return available_languages
