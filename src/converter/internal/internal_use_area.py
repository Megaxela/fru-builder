from __future__ import annotations
from dataclasses import dataclass
from typing import Any

import converter.internal.yaml_names as yaml_names
from converter.internal.language_codes import (
    LanguageCode,
    index_to_language_code,
    str_to_language_code,
    language_code_to_str,
    language_code_to_index,
)
from converter.internal.length_type_value import LengthTypeValue
from converter.internal.checksum import calculate_checksum
from converter.internal.errors import (
    FruValidationError,
    YamlFormatError,
)

MAX_AREA_SIZE = 255


@dataclass()
class InternalUseArea:
    body: bytearray

    def to_binary(self) -> bytes:
        return bytes(self.body)

    def to_yaml(self) -> Any:
        return self.body.hex()

    @staticmethod
    def from_binary(data: bytes) -> InternalUseArea:
        return InternalUseArea(body=bytearray(data))

    @staticmethod
    def from_yaml(data: Any) -> InternalUseArea:
        return InternalUseArea(body=bytearray.fromhex(data))
