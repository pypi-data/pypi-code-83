import unittest

from araugment import augment

class TestSimple(unittest.TestCase):

    def test_run(self):
        augment.back_translate("اهلا وسهلا كيف حالك؟")


if __name__ == '__main__':
    unittest.main()
