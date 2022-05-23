import unittest
import dataclasses
import enum
import typing as tp

from converter.internal.errors import YamlFormatError


class ValueType(enum.Enum):
    BinaryOrUnspecified = 0b00
    BCDPlus = 0b01
    ASCII6bit = 0b10
    LanguageCodeDependent = 0b11


YAML_NAMES_VALUE_TYPE = {
    ValueType.BinaryOrUnspecified: "binary_or_unspecified",
    ValueType.BCDPlus: "bcd_plus",
    ValueType.ASCII6bit: "6bit_ascii",
    ValueType.LanguageCodeDependent: "language_dependent",
}


VALUE_TYPE_YAML_NAMES = {
    YAML_NAMES_VALUE_TYPE[ValueType.BinaryOrUnspecified]: ValueType.BinaryOrUnspecified,
    YAML_NAMES_VALUE_TYPE[ValueType.BCDPlus]: ValueType.BCDPlus,
    YAML_NAMES_VALUE_TYPE[ValueType.ASCII6bit]: ValueType.ASCII6bit,
    YAML_NAMES_VALUE_TYPE[
        ValueType.LanguageCodeDependent
    ]: ValueType.LanguageCodeDependent,
}


@dataclasses.dataclass()
class LengthType:
    type: ValueType
    number_of_data_bytes: tp.Optional[int]

    def is_end_of_fields(self) -> bool:
        return all(
            (
                self.type == ValueType.LanguageCodeDependent,
                self.number_of_data_bytes == 0b000001,
            )
        )

    def empty(self) -> bool:
        return self.number_of_data_bytes == 0

    def to_binary(self) -> int:
        return self.type.value << 6 | self.number_of_data_bytes

    def to_yaml(self) -> str:
        return YAML_NAMES_VALUE_TYPE.get(self.type)

    @staticmethod
    def from_binary(data: bytes) -> "LengthType":
        value = data[0]

        return LengthType(
            type=ValueType((value & 0b11000000) >> 6),
            number_of_data_bytes=(value & 0b00111111),
        )

    @staticmethod
    def from_yaml(data: str) -> "LengthType":
        type_enum = VALUE_TYPE_YAML_NAMES.get(data)
        if type_enum is None:
            raise YamlFormatError(
                f"Type value '{type_str}' not one of available types: [{', '.join(VALUE_TYPE_YAML_NAMES.keys())}]"
            )

        return LengthType(
            type=type_enum,
            number_of_data_bytes=None,
        )


class TestLengthType(unittest.TestCase):
    def test_from_binary(self):
        self.assertEqual(
            LengthType.from_binary(bytes([0b00101010])),
            LengthType(type=ValueType.BinaryOrUnspecified, number_of_data_bytes=42),
        )
        self.assertEqual(
            LengthType.from_binary(bytes([0b01101010])),
            LengthType(type=ValueType.BCDPlus, number_of_data_bytes=42),
        )
        self.assertEqual(
            LengthType.from_binary(bytes([0b10101010])),
            LengthType(type=ValueType.ASCII6bit, number_of_data_bytes=42),
        )
        self.assertEqual(
            LengthType.from_binary(bytes([0b11101010])),
            LengthType(type=ValueType.LanguageCodeDependent, number_of_data_bytes=42),
        )

    def test_from_yaml(self):
        self.assertEqual(
            LengthType.from_yaml("binary_or_unspecified"),
            LengthType(type=ValueType.BinaryOrUnspecified, number_of_data_bytes=None),
        )
        self.assertEqual(
            LengthType.from_yaml("bcd_plus"),
            LengthType(type=ValueType.BCDPlus, number_of_data_bytes=None),
        )
        self.assertEqual(
            LengthType.from_yaml("6bit_ascii"),
            LengthType(type=ValueType.ASCII6bit, number_of_data_bytes=None),
        )
        self.assertEqual(
            LengthType.from_yaml("language_dependent"),
            LengthType(type=ValueType.LanguageCodeDependent, number_of_data_bytes=None),
        )

    def test_to_binary(self):
        self.assertEqual(
            LengthType(
                type=ValueType.BinaryOrUnspecified,
                number_of_data_bytes=0b101010,
            ).to_binary(),
            0b00101010,
        )
        self.assertEqual(
            LengthType(
                type=ValueType.BCDPlus,
                number_of_data_bytes=0b101010,
            ).to_binary(),
            0b01101010,
        )
        self.assertEqual(
            LengthType(
                type=ValueType.ASCII6bit,
                number_of_data_bytes=0b101010,
            ).to_binary(),
            0b10101010,
        )
        self.assertEqual(
            LengthType(
                type=ValueType.LanguageCodeDependent,
                number_of_data_bytes=0b101010,
            ).to_binary(),
            0b11101010,
        )

    def test_to_yaml(self):
        self.assertEqual(
            LengthType(
                type=ValueType.BinaryOrUnspecified,
                number_of_data_bytes=0b101010,
            ).to_yaml(),
            "binary_or_unspecified",
        )
        self.assertEqual(
            LengthType(
                type=ValueType.BCDPlus,
                number_of_data_bytes=0b101010,
            ).to_yaml(),
            "bcd_plus",
        )
        self.assertEqual(
            LengthType(
                type=ValueType.ASCII6bit,
                number_of_data_bytes=0b101010,
            ).to_yaml(),
            "6bit_ascii",
        )
        self.assertEqual(
            LengthType(
                type=ValueType.LanguageCodeDependent,
                number_of_data_bytes=0b101010,
            ).to_yaml(),
            "language_dependent",
        )

    def test_end_of_field(self):
        self.assertFalse(
            LengthType(
                type=ValueType.LanguageCodeDependent,
                number_of_data_bytes=None,
            ).is_end_of_fields(),
        )
        self.assertTrue(
            LengthType(
                type=ValueType.LanguageCodeDependent,
                number_of_data_bytes=0b00000001,
            ).is_end_of_fields(),
        )

    def test_empty(self):

        self.assertFalse(
            LengthType(
                type=ValueType.BinaryOrUnspecified,
                number_of_data_bytes=1,
            ).empty(),
        )
        self.assertTrue(
            LengthType(
                type=ValueType.BinaryOrUnspecified,
                number_of_data_bytes=0,
            ).empty(),
        )


if __name__ == "__main__":
    unittest.main()
