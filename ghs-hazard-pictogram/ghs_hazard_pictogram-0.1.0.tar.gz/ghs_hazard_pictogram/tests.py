"""
GHS Fazard pictograms tests
"""
import unittest

from . import Hazard, UnknownHazard


class HazardTest(unittest.TestCase):
    """
    Hazard test cases
    """

    def testAll(self):
        """
        Test all hazards length
        """
        all_hazards = Hazard.all()
        self.assertEqual(len(all_hazards), 32)

    def testClass8Hazard(self):
        """
        Test loading Class8 hazard
        """
        hazard = Hazard('Class8')
        self.assertEqual(hazard.code, 'Class8')

    def testUnknownHazard(self):
        """
        Test loading unknown hazard
        """
        self.assertRaises(UnknownHazard, Hazard, 'foo')

    def testSearch(self):
        """
        Test searching for hazards
        """
        self.assertEqual(len(Hazard.search('class8')), 1)

    def testEmptySearch(self):
        """
        Test search with no argument
        """
        self.assertRaises(TypeError, Hazard.search)


if __name__ == '__main__':
    unittest.main()