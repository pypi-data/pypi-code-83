"""
GHS Hazard class
"""
import os

from . import __file__
from .data import GHS_HAZARDS

__version__ = [0, 1, 0]


class UnknownHazard(Exception):
    """
    Exception raised when no Hazard is found
    """
    message = "Unknown hazard"


class Hazard:
    """
    Hazard class
    """
    code = None
    name = None
    hazard_type = None
    usage = None
    non_usage = None
    example = None
    pictogram = None
    note = None

    def __init__(self, code: str):
        """
        Initialize Hazard
        :param code: Code of the Hazard
        """
        try:
            hazard = [g for g in GHS_HAZARDS
                      if g['code'].lower() == code.lower()][0]
            self.code = code
            self.name = hazard['name']
            self.usage = hazard['usage']
            self.hazard_type = hazard['hazard_type']
            self.non_usage = hazard.get('non_usage', '')
            self.example = hazard.get('example', '')
            self.pictogram = hazard['pictogram']
            self.note = hazard.get('note', '')
        except IndexError as e:
            raise UnknownHazard() from e

    @classmethod
    def all(cls) -> []:
        """
        Return all hazards
        :return: [Hazard]
        """
        return [cls(h.get('code')) for h in GHS_HAZARDS]

    @classmethod
    def search(cls, term: str) -> []:
        """
        Search for Hazards on code, name, usage, non_usage, example, note
        Search is case insensitive and checks if attribute contains the term
        :param term: string to look for
        :return: List of Hazards
        """
        results = []
        for key in ['code', 'name', 'usage', 'non_usage', 'example', 'note']:
            for hazard in GHS_HAZARDS:
                if term.lower() in hazard.get(key, '').lower():
                    results.append(cls(hazard.get('code')))
        return results

    def get_pictogram(self):
        return os.path.join(os.path.dirname(__file__), 'pictograms',
                            self.pictogram)
