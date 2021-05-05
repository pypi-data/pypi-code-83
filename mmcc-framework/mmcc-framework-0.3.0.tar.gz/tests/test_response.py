from unittest import TestCase

from mmcc_framework.response import Response

class TestResponse(TestCase):
    def setUp(self) -> None:
        self.my_kb = {"key": "value",
                      "key2": "value2",
                      "keyV": ["valueV"],
                      "keyVV": ["valueA", "valueB"],
                      "keyD": {"initials": "valueD"},
                      "keyDV": {"initials": ["valueDV"]},
                      "keyDVV": {"initials": ["valueDA", "valueDB"]},
                      "keyWrong": {"notinitials": "12345"}}
        self.my_ctx = {"c key": "c value"}
        self.my_bool = True
        self.my_utt = "An utt"
        self.my_payload = {"payload": "payload value"}
        self.my_choice = "A choice"

    def test_init(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)

        self.assertEqual(my_response.kb, self.my_kb, "The kb is correctly saved")
        self.assertEqual(my_response.ctx, self.my_ctx, "The ctx is correctly saved")
        self.assertEqual(my_response.complete, self.my_bool, "Completed is correctly saved")
        self.assertEqual(my_response.utterance, self.my_utt, "The utterance is correctly saved")
        self.assertEqual(my_response.payload, self.my_payload, "The payload is correctly saved")
        self.assertEqual(my_response.choice, self.my_choice, "The choice is correctly saved")

    def test_init_with_default(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool)
        self.assertEqual(my_response.kb, self.my_kb, "The kb is correctly saved")
        self.assertEqual(my_response.ctx, self.my_ctx, "The ctx is correctly saved")
        self.assertEqual(my_response.complete, self.my_bool, "Completed is correctly saved")
        self.assertEqual(my_response.utterance, "", "The default utterance is empty")
        self.assertEqual(my_response.payload, {}, "The default payload is empty")
        self.assertIsNone(my_response.choice, "The default choice is None")

    def test_to_dict(self):
        my_dict = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload,
                           self.my_choice).to_dict()

        self.assertEqual(my_dict["utterance"], self.my_utt, "The utterance is correctly passed to the dict")
        self.assertEqual(my_dict["payload"], self.my_payload, "The payload is correctly passed to the dict")

    def test_to_dict_with_default(self):
        my_dict = Response(self.my_kb, self.my_ctx, self.my_bool).to_dict()

        self.assertEqual(my_dict["utterance"], "", "The utterance is correctly passed to the dict")
        self.assertEqual(my_dict["payload"], {}, "The payload is correctly passed to the dict")

    def test_add_utterance_existing_with_fallback(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "key", "fallback")
        self.assertEqual(my_response.utterance, self.my_utt + "\n" + self.my_kb["key"])

    def test_add_utterance_existing_without_fallback(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "key")
        self.assertEqual(my_response.utterance, self.my_utt + "\n" + self.my_kb["key"])

    def test_add_utterance_not_existing_with_fallback(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "key3", "def")
        self.assertEqual(my_response.utterance, self.my_utt + "\n" + "def")

    def test_add_utterance_not_existing_without_fallback(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "key3")
        self.assertEqual(my_response.utterance, self.my_utt)

    def test_add_utterance_initially_empty(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool)
        my_response.add_utterance(self.my_kb, "key")
        self.assertEqual(my_response.utterance, self.my_kb["key"])

    def test_add_utterance_single_vector(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "keyV")
        self.assertEqual(my_response.utterance, self.my_utt + "\n" + self.my_kb["keyV"][0])

    def test_add_utterance_vector(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "keyVV")
        resp = my_response.utterance.splitlines()
        self.assertEqual(resp[0], self.my_utt)
        self.assertIn(resp[1], self.my_kb["keyVV"])

    def test_add_utterance_dict(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "keyD")
        self.assertEqual(my_response.utterance, self.my_utt + "\n" + self.my_kb["keyD"]["initials"])
    
    def test_add_utterance_dict_single_vector(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "keyDV")
        self.assertEqual(my_response.utterance, self.my_utt + "\n" + self.my_kb["keyDV"]["initials"][0])

    def test_add_utterance_dict_vector(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "keyDVV")
        resp = my_response.utterance.splitlines()
        self.assertEqual(resp[0], self.my_utt)
        self.assertIn(resp[1], self.my_kb["keyDVV"]["initials"])

    def test_add_utterance_dict_wrong(self):
        my_response = Response(self.my_kb, self.my_ctx, self.my_bool, self.my_utt, self.my_payload, self.my_choice)
        my_response.add_utterance(self.my_kb, "keyWrong")
        self.assertEqual(my_response.utterance, self.my_utt)