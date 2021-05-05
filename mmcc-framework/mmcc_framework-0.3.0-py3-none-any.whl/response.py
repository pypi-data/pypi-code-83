import random
from typing import Any, Dict


class Response(object):
    def __init__(self,
                 kb: Dict[str, Any],
                 ctx: Dict[str, Any],
                 complete: bool,
                 utterance: str = None,
                 payload: Dict[str, Any] = None,
                 choice: str = None) -> None:
        """ Creates a Response with the provided parameters.

        If the current activity is one of ActivityType.get_require_choice(), and is completed, the Response will contain
        the choice of the user. This must be the id of one of the choices provided in the description.

        :param kb: the updated knowledge
        :param ctx: the updated context
        :param complete: whether the current activity is completed
        :param utterance: an optional utterance to be displayed
        :param payload: an optional payload to be returned to the caller
        :param choice: if the current activity is in ActivityType.get_require_choice() this can contain the user choice
        """
        self.kb = kb
        self.ctx = ctx
        self.complete = complete
        self.utterance = utterance if utterance is not None else ""
        self.payload = payload if payload is not None else {}
        self.choice = choice

    def to_dict(self) -> Dict[str, Any]:
        """ Returns a dictionary with utterance and payload, that can be returned to the caller. """
        return {"utterance": self.utterance, "payload": self.payload}

    def add_utterance(self, kb: Dict[str, Any], key: str, fallback: str = "") -> "Response":
        """ Adds an utterance to this response.

        The utterance is taken from the kb using the provided key,
        the corresponding value can be a string, a vector of strings or a dictionary.
        If it is a string, it will be used as is.
        If it is a vector of strings, one will be picked at random.
        If it is a dictionary, it can contain the key "initials",
        whose value can be a string or a vector of strings as above.
        If the provided key is not in the kb a fallback (empty by default) is used.

        If this response does not already contain an utterance,
        in the end it will contain the added utterance.
        If the utterance to add can not be found and a fallback is not provided, nothing is added.
        If an utterance is provided and one already exists, the new one is appended on a new line.

        :param kb: the kb from which to take the utterance to add
        :param key: the key to retrieve the utterance from the kb
        :param fallback: the value that is used if the key is not in the kb
        :return: the updated Response
        """
        # Prepare my_utt
        try:
            value = kb[key]
            if isinstance(value, dict):
                my_utt = _get_utterance(value["initials"])
            else:
                my_utt = _get_utterance(value)
        except KeyError:
            my_utt = fallback

        # Set the utterance
        if self.utterance == "":
            self.utterance = my_utt
        elif my_utt != "":
            self.utterance += "\n" + my_utt
        return self


def _get_utterance(source):
    """Returns an utterance from source which can be a string or a vector of strings."""
    if isinstance(source, list):
        return random.choice(source)
    return source
