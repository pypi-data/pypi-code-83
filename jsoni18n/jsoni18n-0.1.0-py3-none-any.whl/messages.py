"""Load messages from a folder into dict based on list of codes."""
from json import loads

from jsoni18n.languages import get_available_languages


def get_messages(language, messagefiles):
    """Get a dict with message-name: value for a language based on file. Default to english version if missing.

    Args:
        language (str): language to load
        messagefiles (str): path to messages.  Example: /path/{}.json

    Returns:
        dict: message-name: value for each detected message

    Raises:
        ValueError: 'language' parameter does not match a valid language with a file.
    """
    available_lang_codes = get_available_languages(messagefiles)
    with open(messagefiles.format('eng'), 'r') as messagefileeng:
        messages = loads(messagefileeng.read())
        if language in available_lang_codes:
            if language != 'eng':
                with open(messagefiles.format(language), 'r') as messagefilelangs:
                    filedata = loads(messagefilelangs.read())
                    for message in filedata.keys():
                        messages[message] = filedata[message]
        else:
            raise ValueError("Language is not available")
    return messages
