import ctypes
import dataclasses
import typing as tp

from converter.internal.multi_record_type import (
    MultiRecordType,
    str_to_multi_record_type,
    index_to_multi_record_type,
)
from converter.internal.errors import (
    FruValidationError,
)
from converter.internal.records.basic_record import BasicRecord
from converter.internal.records.management_access_record import ManagementAccessRecord

MULTIRECORD_RECORD_VERSION = 0b000_0010
MULTIRECORD_HEADER_SIZE = 5  # bytes
MULTIRECORD_TYPE_TO_RECORD = {
    MultiRecordType.ManagementAccessRecord: ManagementAccessRecord,
}


@dataclasses.dataclass()
class MultiRecordAreaRecordHeader:
    record_type_id: MultiRecordType
    end_of_list: bool
    record_length: int

    @staticmethod
    def from_binary(data: bytes) -> "MultiRecordAreaRecordHeader":
        version = data[1] & 0b0000_1111
        if version != MULTIRECORD_RECORD_VERSION:
            raise FruValidationError(
                f"Multirecord version {version} is not {MULTIRECORD_RECORD_VERSION}"
            )

        return MultiRecordAreaRecordHeader(
            record_type_id=index_to_multi_record_type(data[0]),
            end_of_list=(data[1] & 0b1000_0000) != 0,
            record_length=data[2],
        )


@dataclasses.dataclass()
class MultiRecordArea:
    records: tp.List[BasicRecord]

    @staticmethod
    def from_binary(data: bytes) -> "MultiRecordArea":
        result: tp.List[BasicRecord] = []
        pointer = 0
        while True:
            header = MultiRecordAreaRecordHeader.from_binary(data[pointer:])

            cls = MULTIRECORD_TYPE_TO_RECORD.get(header.record_type_id)
            if cls is not None:
                result.append(
                    cls.from_binary(
                        data[
                            MULTIRECORD_HEADER_SIZE : MULTIRECORD_HEADER_SIZE
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
    def from_yaml(data: tp.Any) -> "MultiRecordArea":
        pass
