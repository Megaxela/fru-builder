import dataclasses
import typing as tp

from aenum import extend_enum

from converter.internal.records.basic_record import BasicRecord
from converter.internal.multi_record_type import (
    MultiRecordType,
    MULTI_RECORD_TYPE_TO_NAME_MAP,
    NAME_TO_MULTI_RECORD_TYPE_MAP,
    make_multirecord_type_id,
)
from converter.internal.multi_record_area import MULTIRECORD_TYPE_TO_RECORD
from converter.internal.errors import YamlFormatError


def register_generic_multirecord_processors():
    # Extend MultiRecordType Enum with all possible values, that we are not supporting
    # Note: oem vendor record types will be ignored, because they contains vendor id
    for i in range(0xFF):
        if i not in MultiRecordType:
            extend_enum(MultiRecordType, f"Generic{i:02X}", i)

        generic_name = f"generic_{i:02x}"
        generic_enum = MultiRecordType(i)
        if generic_enum not in MULTI_RECORD_TYPE_TO_NAME_MAP:
            MULTI_RECORD_TYPE_TO_NAME_MAP[generic_enum] = generic_name
            NAME_TO_MULTI_RECORD_TYPE_MAP[generic_name] = generic_enum

        if generic_enum not in MULTIRECORD_TYPE_TO_RECORD:
            MULTIRECORD_TYPE_TO_RECORD[generic_enum] = make_generic_record(i)


YAML_NAME_RECORD_ID_KEY = "record_id"
YAML_NAME_DATA_KEY = "data"


def make_generic_record(record_id):
    @dataclasses.dataclass()
    class GenericRecord(BasicRecord):
        data: bytearray

        @property
        def record_type(self):
            return MultiRecordType(record_id)

        def to_binary(self) -> bytes:
            return bytes(self.data)

        def to_yaml(self):
            return {
                YAML_NAME_RECORD_ID_KEY: record_id,
                YAML_NAME_DATA_KEY: self.data.hex(),
            }

        def from_binary(data: bytes) -> "GenericRecord":
            return GenericRecord(
                data=data,
            )

        def from_yaml(data: tp.Any) -> "GenericRecord":
            mandatory_fields = [
                YAML_NAME_DATA_KEY,
                YAML_NAME_RECORD_ID_KEY,
            ]
            for field in mandatory_fields:
                if field not in data:
                    raise YamlFormatError(
                        f"Generic Multirecord Record has no mandatory field '{field}'"
                    )

            data_record_id = data[YAML_NAME_RECORD_ID_KEY]
            if data_record_id != record_id:
                raise RuntimeError(
                    f"Somehow ID from Yaml differs from ID from parser, wtf?"
                )

            return GenericRecord(data=bytearray.fromhex(data[YAML_NAME_DATA_KEY]))

    return GenericRecord
