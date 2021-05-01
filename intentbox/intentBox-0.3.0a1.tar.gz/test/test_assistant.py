import unittest
from intentBox import IntentAssistant
from os.path import join, dirname


class TestSamples(unittest.TestCase):
    def setUp(self) -> None:
        self.assistant = IntentAssistant()

    def compare(self, a, b):
        def fix_dict(c):
            for k, v in c.items():
                if isinstance(v, list):
                    c[k] = fix_list(v)
                if isinstance(v, dict):
                    c[k] = fix_dict(v)
            return c

        def fix_list(c):
            for idx, d in enumerate(c):
                if isinstance(d, list):
                    c[idx] = fix_list(d)
                if isinstance(d, dict):
                    c[idx] = fix_dict(d)
            try:
                c = set(c)
            except:
                pass
            return c

        if isinstance(a, list):
            a = fix_list(a)
        if isinstance(b, list):
            b = fix_list(b)
        self.assertEqual(a, b)

    def test_samples(self):
        test_folder = join(dirname(__file__), "intents")

        def test_intent(intents, intent, expected):
            intents = [v[0] for i, v in intents.items()
                       if i == intent]
            self.compare(intents, expected)

        def test_entities(intents, intent, expected):
            intents = [v[0]['entities'] for i, v in intents.items()
                       if i == intent and v[0]['entities']]
            self.compare(intents, expected)

        self.assistant.load_folder(test_folder)
        test_intent(self.assistant.intent_samples, 'test',
                    [{'entities': {},
                       'samples': {'another test sentence',
                                   'test sentence',
                                   'this is same test',
                                   'this is the same test',
                                   'very simple test sentence',
                                   'yet another test'}}])

        test_intent(self.assistant.intent_samples, 'parantheses_test',
                    [{'entities': {},
                      'samples': {'i  like  mycroft',
                                  'i  love  mycroft',
                                  'i love like mycroft',
                                  'mycroft is  free ',
                                  'mycroft is  open ',
                                  'mycroft is  private ',
                                  'mycroft is open free private'}}])

        test_intent(self.assistant.intent_samples, 'optional_test',
                    [{'entities': {'location': {'canada',
                                                'china',
                                                'england',
                                                'france',
                                                'italy',
                                                'portugal'}},
                      'samples': {'how is the weather like ',
                                  'how is the weather like  in * ',
                                  'how is the weather like  in canada ',
                                  'how is the weather like  in china ',
                                  'how is the weather like  in england ',
                                  'how is the weather like  in france ',
                                  'how is the weather like  in italy ',
                                  'how is the weather like  in portugal ',
                                  'how is weather like location',
                                  'tell me the weather ',
                                  'tell me the weather  at * ',
                                  'tell me the weather  at canada ',
                                  'tell me the weather  at china ',
                                  'tell me the weather  at england ',
                                  'tell me the weather  at france ',
                                  'tell me the weather  at italy ',
                                  'tell me the weather  at portugal ',
                                  'tell me the weather  in * ',
                                  'tell me the weather  in canada ',
                                  'tell me the weather  in china ',
                                  'tell me the weather  in england ',
                                  'tell me the weather  in france ',
                                  'tell me the weather  in italy ',
                                  'tell me the weather  in portugal ',
                                  'tell me weather location location',
                                  "what ' s weather like canada france portugal",
                                  "what's the weather like ",
                                  "what's the weather like  in canada ",
                                  "what's the weather like  in france ",
                                  "what's the weather like  in portugal "}}])
        test_entities(self.assistant.intent_samples, 'optional_test',
                      [{'location': {'france', 'england', 'canada', 'italy', 'china', 'portugal'}}])

        test_intent(self.assistant.intent_samples, 'regex_test',
                    [{'entities': {},
                      'samples': {'repeat *',
                                  'repeat * to me',
                                  'repeat something',
                                  'repeat something to me',
                                  'say *',
                                  'say * to me',
                                  'say something',
                                  'say something to me'}}])


class TestIntents(unittest.TestCase):
    def setUp(self) -> None:
        self.assistant = IntentAssistant()

    def compare(self, a, b):
        def fix_dict(c):
            for k, v in c.items():
                if isinstance(v, list):
                    c[k] = fix_list(v)
                if isinstance(v, dict):
                    c[k] = fix_dict(v)
            return c

        def fix_list(c):
            for idx, d in enumerate(c):
                if isinstance(d, list):
                    c[idx] = fix_list(d)
                if isinstance(d, dict):
                    c[idx] = fix_dict(d)
            try:
                c = set(c)
            except:
                pass
            return c

        if isinstance(a, list):
            a = fix_list(a)
        if isinstance(b, list):
            b = fix_list(b)
        self.assertEqual(a, b)

    def test_samples(self):
        test_folder = join(dirname(__file__), "intents")

        def test_intent(intents, intent, expected):
            intents = [v[0] for i, v in intents.items()
                       if i == intent]
            self.compare(intents, expected)

        def test_entities(intents, intent, expected):
            intents = [v[0]['entities'] for i, v in intents.items()
                       if i == intent and v[0]['entities']]
            self.compare(intents, expected)

        self.assistant.load_folder(test_folder)
        test_intent(self.assistant.padatious_intents, 'test',
                    [{'entities': [],
                       'samples': {'another test sentence',
                                   'test sentence',
                                   'this is same test',
                                   'this is the same test',
                                   'very simple test sentence',
                                   'yet another test'}}])

        test_intent(self.assistant.padatious_intents, 'parantheses_test',
                    [{'entities': [],
                      'samples': {'i  like  mycroft',
                                  'i  love  mycroft',
                                  'i love like mycroft',
                                  'mycroft is  free ',
                                  'mycroft is  open ',
                                  'mycroft is  private ',
                                  'mycroft is open free private'}}])

        test_intent(self.assistant.padatious_intents, 'optional_test',
                    [{'entities': [{'location': {'canada',
                                                 'china',
                                                 'england',
                                                 'france',
                                                 'italy',
                                                 'portugal'}}],
                      'samples': {'how is the weather like ',
                                  'how is the weather like  in { location } ',
                                  'how is weather like location',
                                  'tell me the weather ',
                                  'tell me the weather  at { location } ',
                                  'tell me the weather  in { location } ',
                                  'tell me weather location location',
                                  "what ' s weather like canada france portugal",
                                  "what's the weather like ",
                                  "what's the weather like  in canada ",
                                  "what's the weather like  in france ",
                                  "what's the weather like  in portugal "}}])
        test_entities(self.assistant.padatious_intents, 'optional_test',
                      [[{'location': {'italy', 'france', 'portugal', 'canada', 'china', 'england'}}]])

        test_intent(self.assistant.padatious_intents, 'regex_test',
                    [{'entities': [],
                      'samples': {'repeat something',
                                  'repeat something to me',
                                  'repeat { something }',
                                  'repeat { something } to me',
                                  'say something',
                                  'say something to me',
                                  'say { something }',
                                  'say { something } to me'}}])


class TestAdapt(unittest.TestCase):
    def setUp(self) -> None:
        self.assistant = IntentAssistant()

    def compare(self, a, b):
        def fix_dict(c):
            for k, v in c.items():
                if isinstance(v, list):
                    c[k] = fix_list(v)
                if isinstance(v, dict):
                    c[k] = fix_dict(v)
            return c

        def fix_list(c):
            for idx, d in enumerate(c):
                if isinstance(d, list):
                    c[idx] = fix_list(d)
                if isinstance(d, dict):
                    c[idx] = fix_dict(d)
            try:
                c = set(c)
            except:
                pass
            return c

        if isinstance(a, list):
            a = fix_list(a)
        if isinstance(b, list):
            b = fix_list(b)
        self.assertEqual(a, b)

    def test_adapt(self):
        test_folder = join(dirname(__file__), "intents")

        def test_intent(intents, intent, expected):
            intents = [v[0]['intent'] for i, v in intents.items()
                       if v[0]['intent']["name"] == intent]
            self.compare(intents, expected)

        def test_entities(intents, intent, expected):
            intents = [v[0]['entities'] for i, v in intents.items()
                       if v[0]['intent']["name"] == intent]
            self.compare(intents, expected)

        self.assistant.load_folder(test_folder)
        test_intent(self.assistant.keyword_intents, 'test',
                    [{'at_least_one': [],
                      'name': 'test',
                      'optional': [],
                      'requires': [('required_kw', 'required_kw'),
                                   ('end_kw', 'end_kw')]}])
        test_entities(self.assistant.keyword_intents, 'test',
                      [[{'name': 'required_kw',
                         'required': True,
                         'samples': ['test',
                                     'this is the same',
                                     'this is same',
                                     'another test',
                                     'yet another',
                                     'very simple test']},
                        {'name': 'end_kw', 'required': True,
                         'samples': ['sentence', 'test']}]])

        test_intent(self.assistant.keyword_intents, 'parantheses_test',
                    [{'at_least_one': [],
                      'name': 'parantheses_test',
                      'optional': [],
                      'requires': [('start_kw', 'start_kw'),
                                   ('required_kw', 'required_kw')]}])
        test_entities(self.assistant.keyword_intents, 'parantheses_test',
                      [[{'name': 'start_kw', 'required': True,
                         'samples': {'mycroft', 'i'}},
                        {'name': 'required_kw',
                         'required': True,
                         'samples': {'is  free',
                                     'is  open',
                                     'is  private',
                                     'is open free private',
                                     'like  mycroft',
                                     'love  mycroft',
                                     'love like mycroft'}}]])

        test_intent(self.assistant.keyword_intents, 'optional_test',
                    [{'at_least_one': [],
                      'name': 'optional_test',
                      'optional': [('end_chunk_kw', 'end_chunk_kw'),
                                   ('location_rx', 'location_rx'),
                                   ('location_optional_rx_helper',
                                    'location_optional_rx_helper')],
                      'requires': [('entity_kw_weather', 'entity_kw_weather'),
                                   ('start_chunk_kw', 'start_chunk_kw')]}])
        test_entities(self.assistant.keyword_intents, 'optional_test',
                      [[{'name': 'entity_kw_weather', 'required': True,
                         'samples': {'weather'}},
                        {'name': 'start_chunk_kw',
                         'required': True,
                         'samples': {'how is',
                                     'how is the',
                                     'tell me',
                                     'tell me the',
                                     "what ' s",
                                     "what's the"}},
                        {'name': 'end_chunk_kw',
                         'required': False,
                         'samples': {'like',
                                     'like  in canada',
                                     'like  in france',
                                     'like  in portugal',
                                     'like canada france portugal',
                                     'like location',
                                     'location location'}},
                        {'entity': 'location',
                         'name': 'location_rx',
                         'regex': True,
                         'required': False,
                         'samples': {
                             '^\\W*how\\W+is\\W+the\\W+weather\\W+like\\W+in\\W+(?P<location>.*?\\w.*?)\\W*$'}},
                        {'name': 'location_optional_rx_helper',
                         'required': False,
                         'samples': {'how the weather like',
                                     'how weather like location',
                                     'tell the weather',
                                     'tell weather location location',
                                     'what weather like canada france portugal',
                                     "what's the weather like",
                                     "what's the weather like canada",
                                     "what's the weather like france",
                                     "what's the weather like portugal"}}]])

        test_intent(self.assistant.keyword_intents, 'regex_test',
                    [{'at_least_one': [],
                      'name': 'regex_test',
                      'optional': [('something_rx', 'something_rx'),
                                   ('something_optional_rx_helper',
                                    'something_optional_rx_helper')],
                      'requires': [('start_kw', 'start_kw'),
                                   ('required_kw', 'required_kw')]}])
        test_entities(self.assistant.keyword_intents, 'regex_test',
                      [[{'name': 'start_kw', 'required': True,
                         'samples': {'say', 'repeat'}},
                        {'name': 'required_kw',
                         'required': True,
                         'samples': {'something', 'something to me'}},
                        {'entity': 'something',
                         'name': 'something_rx',
                         'regex': True,
                         'required': False,
                         'samples': {
                             '^\\W*repeat\\W+(?P<something>.*?\\w.*?)\\W+to\\W+me\\W*$'}},
                        {'name': 'something_optional_rx_helper',
                         'required': False,
                         'samples': {'say something', 'repeat something'}}]])

