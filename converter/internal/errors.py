class FormatError(Exception):
    pass


class YamlFormatError(FormatError):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message

    def __repr__(self):
        return self._message


class FruValidationError(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message

    def __repr__(self):
        return self._message


class BinaryConversionError(FormatError):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message

    def __repr__(self):
        return self._message
