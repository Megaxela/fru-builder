from __future__ import annotations
from dataclasses import dataclass
from typing import List, Any

from converter.internal.multi_record_type import (
    MultiRecordType,
    str_to_multi_record_type,
    index_to_multi_record_type,
    multi_record_type_to_str,
    multi_record_type_to_index,
)
from converter.internal.errors import (
    FruValidationError,
    YamlFormatError,
    BinaryConversionError,
)
from converter.internal.records.basic_record import BasicRecord
from converter.internal.records.management_access_record import ManagementAccessRecord
from converter.internal.checksum import calculate_checksum
import converter.internal.yaml_names as yaml_names

MAX_RECORD_LENGTH = 255
MULTIRECORD_RECORD_VERSION = 0b0010
MULTIRECORD_HEADER_SIZE = 5  # bytes
MULTIRECORD_TYPE_TO_RECORD = {
    MultiRecordType.ManagementAccessRecord: ManagementAccessRecord,
}


@dataclass()
class MultiRecordAreaRecordHeader:
    record_type_id: MultiRecordType
    end_of_list: bool
    record_length: int
    record_checksum: int

    def to_binary(self) -> bytes:
        result = bytearray()

        # 1 byte of record type id
        result.append(multi_record_type_to_index(self.record_type_id))

        # 1 byte of bitfield
        bitfield = MULTIRECORD_RECORD_VERSION
        if self.end_of_list:
            bitfield |= 0b1000_0000
        result.append(bitfield)

        # 1 byte of record length
        if self.record_length > MAX_RECORD_LENGTH:
            raise FruValidationError(
                f"MultiRecord record size {self.record_length} > {MAX_RECORD_LENGTH}"
            )

        result.append(self.record_length)

        # 1 record checksum
        result.append(self.record_checksum)

        # 1 header checksum
        result.append(calculate_checksum(result))

        return bytes(result)

    @staticmethod
    def from_binary(data: bytes) -> MultiRecordAreaRecordHeader:
        version = data[1] & 0b0000_1111
        if version != MULTIRECORD_RECORD_VERSION:
            raise FruValidationError(
                f"Multirecord version {version} is not {MULTIRECORD_RECORD_VERSION}"
            )

        # Special parsing for OEM multirecord records
        manufacturer_id = 0x000000
        if data[0] >= 0xC0 and data[0] <= 0xFF:
            manufacturer_id = data[5] | (data[6] << 8) | (data[7] << 16)

        try:
            record_type_id = index_to_multi_record_type(data[0], manufacturer_id)
        except ValueError:
            # We can't parse this one. Removing manufacture id from equasion
            # And pretending, that it's just simple generic multirecord
            record_type_id = index_to_multi_record_type(data[0])

        return MultiRecordAreaRecordHeader(
            record_type_id=record_type_id,
            end_of_list=(data[1] & 0b1000_0000) != 0,
            record_length=data[2],
            record_checksum=data[3],
        )


@dataclass()
class MultiRecordArea:
    records: List[BasicRecord]

    def to_binary(self) -> tp.Optional[bytes]:
        if not self.records:
            return None

        result = bytearray()

        for index, record in enumerate(self.records):
            record_data = record.to_binary()

            result += MultiRecordAreaRecordHeader(
                record_type_id=record.record_type,
                end_of_list=(index == len(self.records) - 1),
                record_length=len(record_data),
                record_checksum=calculate_checksum(record_data),
            ).to_binary()
            result += record_data

        total_length = len(result)

        result += bytes([0x00]) * (8 - (total_length % 8))

        return bytes(result)

    def to_yaml(self) -> List[Any]:
        result = []

        for record in self.records:
            result.append(
                {
                    yaml_names.MULTIRECORD_TYPE_KEY: multi_record_type_to_str(
                        record.record_type
                    ),
                    yaml_names.MULTIRECORD_VALUE_KEY: record.to_yaml(),
                }
            )

        return result

    @staticmethod
    def from_binary(data: bytes) -> MultiRecordArea:
        result: List[BasicRecord] = []
        pointer = 0
        while True:
            header = MultiRecordAreaRecordHeader.from_binary(data[pointer:])

            # todo: throw if unknown type instead of ignoring
            cls = MULTIRECORD_TYPE_TO_RECORD.get(header.record_type_id)
            if cls is None:
                raise BinaryConversionError(
                    f"Unknown multirecord type 0x{header.record_type_id.value:02X} ({header.record_type_id})"
                )

            result.append(
                cls.from_binary(
                    data[
                        pointer
                        + MULTIRECORD_HEADER_SIZE : pointer
                        + MULTIRECORD_HEADER_SIZE
                        + header.record_length
                    ]
                )
            )
            pointer += MULTIRECORD_HEADER_SIZE + header.record_length

            if header.end_of_list:
                break
        return MultiRecordArea(
            records=result,
        )

    @staticmethod
    def from_yaml(data: tp.Any) -> MultiRecordArea:
        result: List[BasicRecord] = []

        record_mandatory_fields = [
            yaml_names.MULTIRECORD_TYPE_KEY,
            yaml_names.MULTIRECORD_VALUE_KEY,
        ]

        for record in data:
            for field in record_mandatory_fields:
                if field not in record:
                    raise YamlFormatError(
                        f"Multirecord area has no mandatory field '{field}'"
                    )

            try:
                record_type = str_to_multi_record_type(
                    record[yaml_names.MULTIRECORD_TYPE_KEY]
                )
            except ValueError as e:
                raise YamlFormatError(str(e))

            # todo: throw if unknown type instead of ignoring
            cls = MULTIRECORD_TYPE_TO_RECORD.get(record_type)
            if cls is not None:
                result.append(cls.from_yaml(record[yaml_names.MULTIRECORD_VALUE_KEY]))

        return MultiRecordArea(
            records=result,
        )
