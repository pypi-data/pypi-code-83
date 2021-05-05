from unittest.case import TestCase

from mmcc_framework.exceptions import CallbackException, DescriptionException, MissingCallbackException


class TestDescriptionException(TestCase):
    def setUp(self) -> None:
        self.cause = "cause"
        self.message = "message"
        self.value = DescriptionException(self.cause, self.message)

    def test_init(self):
        self.assertIs(self.value.cause, self.cause, "The cause is correctly set")
        self.assertIs(self.value.args[0], self.message, "The message is correctly set")

    def test_str(self):
        self.assertEqual(self.value.__str__(), f"{self.message} The cause of the exception was: {self.cause}")


class TestCallbackException(TestCase):
    def setUp(self) -> None:
        self.cause = "cause"
        self.message = "message"
        self.value = CallbackException(self.cause, self.message)

    def test_init(self):
        self.assertIs(self.value.cause, self.cause, "The cause is correctly set")
        self.assertIs(self.value.args[0], self.message, "The message is correctly set")

    def test_str(self):
        self.assertEqual(self.value.__str__(), f"{self.message} The cause of the exception was: {self.cause}")


class TestMissingCallbackException(TestCase):
    def setUp(self) -> None:
        self.cause = "cause"
        self.value = MissingCallbackException(self.cause)

    def test_init(self):
        self.assertIs(self.value.cause, self.cause)
        self.assertEqual(self.value.args[0], "Accessing a non existing callback.")

    def test_str(self):
        self.assertEqual(self.value.__str__(), f"Accessing a non existing callback. The cause of the exception was: {self.cause}")
