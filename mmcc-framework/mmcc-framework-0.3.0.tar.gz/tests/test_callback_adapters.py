from unittest.case import TestCase

from mmcc_framework.callback_adapters import DictCallback, FunctionCallback
from mmcc_framework.exceptions import MissingCallbackException
from mmcc_framework.response import Response


class TestDictCallback(TestCase):
    def setUp(self) -> None:
        self.callbacks = {
            "first": lambda d, k, c, a: Response(k, c, True, utterance="first"),
            "second": lambda d, k, c, a: Response(k, c, True, utterance="second"),
            "third": lambda d, k, c, a: Response(k, c, True, utterance="third")
        }

    def test_get(self):
        my_callbacks = DictCallback(self.callbacks)
        self.assertEqual(my_callbacks.get("first"), self.callbacks["first"])
        self.assertEqual(my_callbacks.get("second"), self.callbacks["second"])
        self.assertEqual(my_callbacks.get("third"), self.callbacks["third"])

    def test_get_not_existing(self):
        my_callbacks = DictCallback(self.callbacks)
        self.assertRaises(MissingCallbackException,
                          lambda: my_callbacks.get("fourth"))

    def test_check(self):
        my_callbacks = DictCallback(self.callbacks)
        self.assertTrue(my_callbacks.check("first"))
        self.assertTrue(my_callbacks.check("second"))
        self.assertTrue(my_callbacks.check("third"))

    def test_check_not_existing(self):
        my_callbacks = DictCallback(self.callbacks)
        self.assertFalse(my_callbacks.check("fourth"))


class TestFunctionCallback(TestCase):
    def setUp(self) -> None:
        self.callbacks = {
            "first": lambda d, k, c, a: Response(k, c, True, utterance="first"),
            "second": lambda d, k, c, a: Response(k, c, True, utterance="second"),
            "third": lambda d, k, c, a: Response(k, c, True, utterance="third")
        }
        self.getter = lambda name: self.callbacks[name]

    def test_get(self):
        my_callbacks = FunctionCallback(self.getter)
        self.assertEqual(my_callbacks.get("first"), self.callbacks["first"])
        self.assertEqual(my_callbacks.get("second"), self.callbacks["second"])
        self.assertEqual(my_callbacks.get("third"), self.callbacks["third"])

    def test_get_not_existing(self):
        my_callbacks = FunctionCallback(self.getter)
        self.assertRaises(MissingCallbackException,
                          lambda: my_callbacks.get("fourth"))

    def test_check(self):
        my_callbacks = FunctionCallback(self.getter)
        self.assertTrue(my_callbacks.check("first"))
        self.assertTrue(my_callbacks.check("second"))
        self.assertTrue(my_callbacks.check("third"))

    def test_check_not_existing(self):
        my_callbacks = FunctionCallback(self.getter)
        self.assertFalse(my_callbacks.check("fourth"))
