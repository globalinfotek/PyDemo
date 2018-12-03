import re
import json


class JsonConverter:
    _UNDERSCORE_PATTERN = re.compile(r'_([a-z])')

    def __init__(self):
        pass

    @staticmethod
    def convert(to_be_converted):
        return json.dumps(JsonConverter._convert_json(to_be_converted.__dict__, JsonConverter._underscore_to_camel))

    # Converts a single filed name from underscore format to camel-case.
    @staticmethod
    def _underscore_to_camel(name):
        text_without_underscores = JsonConverter._UNDERSCORE_PATTERN.sub(lambda x: x.group(1).upper(), name)
        return JsonConverter._lower_first(text_without_underscores)

    @staticmethod
    def _lower_first(text):
        return text[:1].lower() + text[1:] if text else ''

    # Converts an instance of an object to a camel-case formatted JSON string.
    @staticmethod
    def _convert_json(d, convert):
        new_d = {}
        for k, v in d.items():
            new_d[convert(k)] = JsonConverter._convert_json(v, convert) if isinstance(v, dict) else v
        return new_d
