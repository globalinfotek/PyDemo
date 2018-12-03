from unittest import TestCase

from source.json_converter import JsonConverter


class TestJsonConverter(TestCase):

    def test_convert(self):
        data = self.SimpleThing()
        result = JsonConverter.convert(data)
        self.assertIsNotNone(result)
        self.assertEqual('{"firstField": "thing", "second": 100}', result)

    class SimpleThing:
        def __init__(self):
            self._first_field = 'thing'
            self._second = 100
