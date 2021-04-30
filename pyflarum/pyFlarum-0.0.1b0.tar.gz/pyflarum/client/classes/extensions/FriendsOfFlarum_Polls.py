from typing import Iterable, Union
from datetime import datetime

from pyflarum.date_conversions import datetime_to_flarum, flarum_to_datetime
from pyflarum.exceptions import FlarumError


class FoF_PollOption(dict):
    """
        Represents a FoF poll option.
    """


    # Main:
    @property
    def type(self) -> Union[str, None]:
        return self.get('type', None)


    @property
    def id(self) -> Union[int, None]:
        return self.get('id')


    # Attributes:
    @property
    def attributes(self) -> dict:
        return self.get('attributes', {})


    @property
    def answer(self) -> Union[str, None]:
        return self.attributes.get('answer', None)

    @property
    def createdAt(self) -> datetime:
        try:
            return flarum_to_datetime(self['attributes']['createdAt'])
        except KeyError:
            return None

    @property
    def updatedAt(self) -> datetime:
        try:
            return flarum_to_datetime(self['attributes']['updatedAt'])
        except KeyError:
            return None


class FoF_Poll(dict):
    """
        A subclass of `dict` representing poll's JSON data.

        - `question (str)`: The poll's question (example: `"Do you like ducks?"`)
        - `options (list)`: A list containing all options for a poll (example: `["Yes", "No"]`).
        - `endDate (datetime)`: The date when the poll ends and no more votes can be cast.
        - `public (bool)`: Whether or not the poll is a public one (eg.: people can view who voted, defaults to `False`).
        # 
        - `raw_data (dict)`: The raw poll data, used when fetching the poll from an API. Either specify all the options above
        that will build the poll data for you, or just this one with already built poll data.
    """

    def __init__(self, question: str=None, options: list=None, endDate: datetime=None, public: bool=False, raw_data: dict=None):
        """
            Builds the poll data.

            - `question (str)`: The poll's question (example: `"Do you like ducks?"`)
            - `options (list)`: A list containing all options for a poll (example: `["Yes", "No"]`).
            - `endDate (datetime)`: The date when the poll ends and no more votes can be cast.
            - `public (bool)`: Whether or not the poll is a public one (eg.: people can view who voted, defaults to `False`).
            # 
            - `raw_data (dict)`: The raw poll data, used when fetching the poll from an API. Either specify all the options above
            that will build the poll data for you, or just this one with already built poll data.
        """
        
        if raw_data is None:
            if question is None or options is None or type(options) != list:
                raise FlarumError('A question and at least 1 option is required for polls. Options must also be a list')

            poll_data = {
                "question": question,
                "publicFoF_Poll": public,
                "relationships": {
                    "options": options
                }
            }

            if endDate is not None:
                poll_data['endDate'] = datetime_to_flarum(endDate)

            dict.__init__(self, poll_data)

        else:
            dict.__init__(self, raw_data)


    # Main:
    @property
    def type(self) -> str:
        try:
            return self['type']
        except KeyError:
            return None

    @property
    def id(self) -> int:
        try:
            return self['id']
        except KeyError:
            return None

    # Attributes:
    @property
    def question(self) -> str:
        try:
            return self['attributes']['question']
        except KeyError:
            return None

    @property
    def hasEnded(self) -> Union[bool, None]:
        return self.get('attributes', {}).get('hasEnded', None)

    @property
    def public(self) -> Union[bool, None]:
        self.get('attributes', {}).get('public_poll', None)

    @property
    def endDate(self) -> Union[datetime, None]:
        raw = self.get('attributes', {}).get('endDate', None)
        return flarum_to_datetime(raw)

    @property
    def createdAt(self) -> Union[datetime, None]:
        raw = self.get('attributes', {}).get('createdAt', None)
        return flarum_to_datetime(raw)

    @property
    def updatedAt(self) -> Union[datetime, None]:
        raw = self.get('attributes', {}).get('updatedAt', None)
        return flarum_to_datetime(raw)

    @property
    def relationship_options(self) -> list:
        return self.get('relationships', {}).get('options', {}).get('data', {})

    @property
    def relationship_votes(self) -> list:
        return self.get('relationships', {}).get('votes', {}).get('data', {})

    @property
    def _options(self) -> Iterable[FoF_PollOption]:
        try:
            options = []

            for option in self['_options']:
                options.append(FoF_PollOption(raw=option))

            return options

        except KeyError:
            return None

    def get_poll_option_by_id(self, id: Union[str, int]) -> FoF_PollOption:
        poll_option = None

        try:
            for option in self._options:
                if option['id'] == str(id):
                    poll_option = FoF_PollOption(option)

        except KeyError:
            raise

        finally:
            return poll_option
