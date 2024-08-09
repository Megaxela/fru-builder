import unittest
import dataclasses
import typing as tp
import enum

from converter.internal.length_type import LengthType, ValueType
from converter.internal.bcd import bcd_to_str, str_to_bcd
from converter.internal.ascii_6bit import ascii_6bit_to_str, str_to_ascii_6bit
from converter.internal.language_codes import LanguageCode
from converter.internal.errors import YamlFormatError, BinaryConversionError
import converter.internal.yaml_names as yaml_names


class ParseHint(enum.Enum):
    ByteArray = enum.auto()


def parse_value(data: str, hint: ParseHint = None):
    def parse_as_bytearray():
        v = data.lower().split(" ")
        if len(v) == 0 or max(*list(map(lambda x: len(x), v))) > 2:
            raise ValueError()

        return bytes(map(lambda x: int(x, 16), data.lower().split(" ")))

    if hint == ParseHint.ByteArray:
        return parse_as_bytearray()

    try:
        return parse_as_bytearray()
    except:
        pass
    return data


def value_to_yaml(data: tp.Any):
    if isinstance(data, bytes):
        return data.hex(" ")
    return data


@dataclasses.dataclass()
class LengthTypeValue:
    length_type: LengthType
    value: tp.Optional[tp.Union[str, bytes]]

    def get_size(self, language_code: tp.Optional[LanguageCode] = None) -> int:
        return len(self.to_binary(language_code))

    def to_binary(self, language_code: tp.Optional[LanguageCode] = None) -> bytes:
        if language_code is None:
            language_code = LanguageCode.English

        if self.value is None:
            self.length_type.number_of_data_bytes = 0
            return bytes([self.length_type.to_binary()])

        # Converting value to bytes
        converted_value = None
        if self.length_type.type == ValueType.BinaryOrUnspecified:
            if isinstance(self.value, bytes):
                converted_value = self.value
            elif isinstance(self.value, str):
                converted_value = self.value.encode("utf-8")
            else:
                raise BinaryConversionError(
                    f"Length/Type value has unknown type '{type(self.value)}'"
                )
        elif self.length_type.type == ValueType.BCDPlus:
            if not isinstance(self.value, str):
                raise BinaryConversionError("BCD PLUS value should be string")
            converted_value = str_to_bcd(self.value)
        elif self.length_type.type == ValueType.ASCII6bit:
            if not isinstance(self.value, str):
                raise BinaryConversionError("ASCII 6bit value should be string")
            converted_value = str_to_ascii_6bit(self.value)
        elif self.length_type.type == ValueType.LanguageCodeDependent:
            if not isinstance(self.value, str):
                raise BinaryConversionError(
                    f"Language Dependent value should be string, but it's {self.value} ({type(self.value).__name__})"
                )

            if language_code == LanguageCode.English:
                try:
                    converted_value = self.value.encode("latin-1")
                except UnicodeEncodeError as e:
                    raise BinaryConversionError(
                        f"Unable to convert '{self.value}' to latin-1 (language code: {language_code}): {e}"
                    )
            else:
                try:
                    converted_value = self.value.encode("utf-16be")
                except UnicodeEncodeError as e:
                    raise BinaryConversionError(
                        f"Unable to convert '{self.value}' to utf-16 (language code: {language_code}): {e}"
                    )

        # Bumping number of data bytes
        self.length_type.number_of_data_bytes = len(converted_value)

        # Generating bytes
        return bytes([self.length_type.to_binary()]) + converted_value

    def to_yaml(self) -> tp.Any:
        return {
            yaml_names.LENGTH_TYPE_TYPE_KEY: self.length_type.to_yaml(),
            yaml_names.LENGTH_TYPE_VALUE_KEY: value_to_yaml(self.value),
        }

    @staticmethod
    def from_yaml(data: tp.Any):
        if yaml_names.LENGTH_TYPE_VALUE_KEY not in data:
            raise YamlFormatError(
                f"There is no '{yaml_names.LENGTH_TYPE_VALUE_KEY}' key in length/type value field"
            )

        type_str = data.get(yaml_names.LENGTH_TYPE_TYPE_KEY)
        if type_str is None:
            raise YamlFormatError(
                f"No '{yaml_names.LENGTH_TYPE_TYPE_KEY}' key in type/length value field"
            )

        lt = LengthType.from_yaml(type_str)
        return LengthTypeValue(
            length_type=lt,
            value=parse_value(
                data[yaml_names.LENGTH_TYPE_VALUE_KEY],
                (
                    ParseHint.ByteArray
                    if lt.type == ValueType.BinaryOrUnspecified
                    else None
                ),
            ),
        )

    @staticmethod
    def from_binary(
        length_type_ptr: bytes,
        value_ptr: bytes,
        language_code: tp.Optional[LanguageCode] = None,
    ) -> tp.Optional["LengthTypeValue"]:
        lt = LengthType.from_binary(length_type_ptr)
        if lt.is_end_of_fields():
            return None  # ???

        if language_code is None:
            language_code = LanguageCode.English

        if lt.empty():
            return LengthTypeValue(length_type=lt, value=None)

        values_raw = value_ptr[: lt.number_of_data_bytes]

        if lt.type == ValueType.BinaryOrUnspecified:
            return LengthTypeValue(length_type=lt, value=values_raw)
        elif lt.type == ValueType.BCDPlus:
            return LengthTypeValue(length_type=lt, value=bcd_to_str(values_raw))
        elif lt.type == ValueType.ASCII6bit:
            return LengthTypeValue(length_type=lt, value=ascii_6bit_to_str(values_raw))
        elif lt.type == ValueType.LanguageCodeDependent:
            if language_code == LanguageCode.English:
                return LengthTypeValue(
                    length_type=lt,
                    value=values_raw.decode("latin-1"),
                )
            else:
                # Specification declares this values as 2 byte unicode,
                # but it's essentially utf-16 BE. Using it for native conversion.
                return LengthTypeValue(
                    length_type=lt,
                    value=values_raw.decode("utf-16be"),
                )
        else:
            raise RuntimeError("Unknown value type to parse")


class TestLengthTypeValue(unittest.TestCase):
    def test_to_binary(self):
        self.assertEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BinaryOrUnspecified,
                    number_of_data_bytes=None,
                ),
                value=bytes([0x01, 0x02]),
            ).to_binary(),
            bytes([0b00_000010, 0x01, 0x02]),
        )

        # BCD Plus
        self.assertEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BCDPlus,
                    number_of_data_bytes=None,
                ),
                value="1234",
            ).to_binary(),
            bytes([0b01_000010, 0x12, 0x34]),
        )

        # 6bit ASCII
        self.assertEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.ASCII6bit,
                    number_of_data_bytes=None,  # despite value is 4 bytes
                ),
                value="IPMI",
            ).to_binary(),
            bytes([0b10_000011, 0x29, 0xDC, 0xA6]),
        )

        # Language Specific (eng)
        self.assertEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.LanguageCodeDependent,
                    number_of_data_bytes=None,
                ),
                value="abc",
            ).to_binary(LanguageCode.English),
            bytes([0b11_000011, 0x61, 0x62, 0x63]),
        )

        # Language Specific (other)
        self.assertEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.LanguageCodeDependent,
                    number_of_data_bytes=None,
                ),
                value="чел",
            ).to_binary(LanguageCode.Polish),
            bytes([0b11_000110, 0x04, 0x47, 0x04, 0x35, 0x04, 0x3B]),
        )

    def test_to_yaml(self):
        self.assertDictEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BinaryOrUnspecified,
                    number_of_data_bytes=2,
                ),
                value=bytes([0x01, 0x02]),
            ).to_yaml(),
            {
                "type": "binary_or_unspecified",
                "value": "01 02",
            },
        )

        # BCD Plus
        self.assertDictEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BCDPlus,
                    number_of_data_bytes=2,
                ),
                value="1234",
            ).to_yaml(),
            {
                "type": "bcd_plus",
                "value": "1234",
            },
        )

        # 6bit ASCII
        self.assertDictEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.ASCII6bit,
                    number_of_data_bytes=3,  # despite value is 4 bytes
                ),
                value="IPMI",
            ).to_yaml(),
            {
                "type": "6bit_ascii",
                "value": "IPMI",
            },
        )

        # Language Specific
        self.assertDictEqual(
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.LanguageCodeDependent,
                    number_of_data_bytes=3,
                ),
                value="abc",
            ).to_yaml(),
            {
                "type": "language_dependent",
                "value": "abc",
            },
        )

    def test_from_yaml(self):
        # Binary or Unspecified
        self.assertEqual(
            LengthTypeValue.from_yaml(
                {
                    "type": "binary_or_unspecified",
                    "value": "01 02",
                }
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BinaryOrUnspecified,
                    number_of_data_bytes=None,
                ),
                value=bytes([0x01, 0x02]),
            ),
        )

        # BCD Plus
        self.assertEqual(
            LengthTypeValue.from_yaml(
                {
                    "type": "bcd_plus",
                    "value": "1234",
                }
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BCDPlus,
                    number_of_data_bytes=None,
                ),
                value="1234",
            ),
        )

        # 6bit ASCII
        self.assertEqual(
            LengthTypeValue.from_yaml(
                {
                    "type": "6bit_ascii",
                    "value": "IPMI",
                }
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.ASCII6bit,
                    number_of_data_bytes=None,
                ),
                value="IPMI",
            ),
        )

        # Language Specific (eng)
        self.assertEqual(
            LengthTypeValue.from_yaml(
                {
                    "type": "language_dependent",
                    "value": "abc",
                }
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.LanguageCodeDependent,
                    number_of_data_bytes=None,
                ),
                value="abc",
            ),
        )

    def test_from_binary(self):
        # Empty
        self.assertEqual(
            LengthTypeValue.from_binary(
                length_type_ptr=bytes([0b00000000]),
                value_ptr=bytes([]),
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BinaryOrUnspecified,
                    number_of_data_bytes=0,
                ),
                value=None,
            ),
        )

        # Binary or Unspecified
        self.assertEqual(
            LengthTypeValue.from_binary(
                length_type_ptr=bytes([0b00000010]),
                value_ptr=bytes([0x01, 0x02, 0x03, 0x04]),
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BinaryOrUnspecified,
                    number_of_data_bytes=2,
                ),
                value=bytes([0x01, 0x02]),
            ),
        )

        # BCD Plus
        self.assertEqual(
            LengthTypeValue.from_binary(
                length_type_ptr=bytes([0b01000010]),
                value_ptr=bytes([0x12, 0x34]),
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.BCDPlus,
                    number_of_data_bytes=2,
                ),
                value="1234",
            ),
        )

        # 6bit ASCII
        self.assertEqual(
            LengthTypeValue.from_binary(
                length_type_ptr=bytes([0b10000011]),
                value_ptr=bytes([0x29, 0xDC, 0xA6]),
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.ASCII6bit,
                    number_of_data_bytes=3,  # despite value is 4 bytes
                ),
                value="IPMI",
            ),
        )

        # Language Specific (eng)
        self.assertEqual(
            LengthTypeValue.from_binary(
                length_type_ptr=bytes([0b11000011]),
                value_ptr=bytes([0x61, 0x62, 0x63]),
                language_code=LanguageCode.English,
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.LanguageCodeDependent,
                    number_of_data_bytes=3,
                ),
                value="abc",
            ),
        )

        # Language Specific (other)
        self.assertEqual(
            LengthTypeValue.from_binary(
                length_type_ptr=bytes([0b11010110]),
                value_ptr=bytes(
                    [
                        0x04,
                        0x3F,
                        0x04,
                        0x40,
                        0x04,
                        0x38,
                        0x04,
                        0x32,
                        0x04,
                        0x35,
                        0x04,
                        0x42,
                        0x00,
                        0x20,
                        0x04,
                        0x47,
                        0x04,
                        0x35,
                        0x04,
                        0x3B,
                        0x04,
                        0x3B,
                    ]
                ),
                language_code=LanguageCode.Polish,
            ),
            LengthTypeValue(
                length_type=LengthType(
                    type=ValueType.LanguageCodeDependent,
                    number_of_data_bytes=22,
                ),
                value="привет челл",
            ),
        )


if __name__ == "__main__":
    unittest.main()
