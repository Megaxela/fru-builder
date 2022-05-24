import dataclasses
import enum
import typing as tp

from converter.internal.records.basic_record import BasicRecord
import converter.internal.yaml_names as yaml_names
from converter.internal.length_type_value import parse_value, value_to_yaml
from converter.internal.multi_record_type import MultiRecordType
from converter.internal.errors import BinaryConversionError


class ManagementAccessRecordType(enum.Enum):
    SystemManagementURL = 0x01  # String [16 - 256]
    SystemName = 0x02  # String [8 - 64]
    SystemPingAddress = 0x03  # String [8 - 64]
    ComponentManagementURL = 0x04  # String [16 - 256]
    ComponentName = 0x05  # String [8 - 256]
    ComponentPingAddress = 0x06  # String [8 - 64]
    SystemUniqueID = 0x07  # Binary [16]


MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING = {
    ManagementAccessRecordType.SystemManagementURL: "system_management_url",
    ManagementAccessRecordType.SystemName: "system_name",
    ManagementAccessRecordType.SystemPingAddress: "system_ping_address",
    ManagementAccessRecordType.ComponentManagementURL: "component_management_url",
    ManagementAccessRecordType.ComponentName: "component_name",
    ManagementAccessRecordType.ComponentPingAddress: "component_ping_address",
    ManagementAccessRecordType.SystemUniqueID: "system_unique_id",
}

STRING_TO_MANAGEMENT_ACCESS_RECORD_TYPE = {
    MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING[
        ManagementAccessRecordType.SystemManagementURL
    ]: ManagementAccessRecordType.SystemManagementURL,
    MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING[
        ManagementAccessRecordType.SystemName
    ]: ManagementAccessRecordType.SystemName,
    MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING[
        ManagementAccessRecordType.SystemPingAddress
    ]: ManagementAccessRecordType.SystemPingAddress,
    MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING[
        ManagementAccessRecordType.ComponentManagementURL
    ]: ManagementAccessRecordType.ComponentManagementURL,
    MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING[
        ManagementAccessRecordType.ComponentName
    ]: ManagementAccessRecordType.ComponentName,
    MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING[
        ManagementAccessRecordType.ComponentPingAddress
    ]: ManagementAccessRecordType.ComponentPingAddress,
    MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING[
        ManagementAccessRecordType.SystemUniqueID
    ]: ManagementAccessRecordType.SystemUniqueID,
}


def bound_check(start, end):
    def check(value):
        length = len(value)
        if not start <= length <= end:
            raise ValueError(f"Value length {length} is out of range [{start}, {end}]")
        return value

    return check


# Assuming, that FRU specification declares sizes WITH type byte.
# Also, specification declares, that record data may be 256 bytes long.
# But this is impossible due to 1 byte length.
VALUE_VALIDATORS = {
    ManagementAccessRecordType.SystemManagementURL: bound_check(16, 255),
    ManagementAccessRecordType.SystemName: bound_check(8, 64),
    ManagementAccessRecordType.SystemPingAddress: bound_check(8, 64),
    ManagementAccessRecordType.ComponentManagementURL: bound_check(16, 255),
    ManagementAccessRecordType.ComponentName: bound_check(8, 255),
    ManagementAccessRecordType.ComponentPingAddress: bound_check(8, 64),
    ManagementAccessRecordType.SystemUniqueID: bound_check(16, 16),
}


@dataclasses.dataclass()
class ManagementAccessRecord(BasicRecord):
    sub_type: ManagementAccessRecordType
    data: tp.Union[bytes, str]

    @property
    def record_type(self):
        return MultiRecordType.ManagementAccessRecord

    def to_binary(self) -> bytes:
        result = bytearray()

        # 1 byte sub-record type
        result.append(self.sub_type.value)

        # N bytes data
        if isinstance(self.data, str):
            try:
                result += self.data.encode("latin-1")
            except UnicodeEncodeError as e:
                raise BinaryConversionError(
                    f"Unable to convert '{self.data}' to latin-1: {e}"
                )
        elif isinstance(self.data, bytes):
            result += self.data

        return bytes(result)

    def to_yaml(self):
        return {
            yaml_names.MANAGEMENT_ACCESS_RECORD_SUB_TYPE_KEY: MANAGEMENT_ACCESS_RECORD_TYPE_TO_STRING[
                self.sub_type
            ],
            yaml_names.MANAGEMENT_ACCESS_RECORD_VALUE_KEY: value_to_yaml(self.data),
        }

    def from_binary(data: bytes) -> "ManagementAccessRecord":
        sub_type = ManagementAccessRecordType(data[0])

        value = data[1:]
        if sub_type == ManagementAccessRecordType.SystemUniqueID:
            value = " ".join(map(lambda x: f"{x:02x}", value))
        else:
            # Try to parse it as latin-1 string.
            # If failed - just let it be binary.
            try:
                value = value.decode("latin-1")
            except UnicodeDecodeError:
                pass

        return ManagementAccessRecord(sub_type=sub_type, data=value)

    def from_yaml(data: tp.Any) -> "ManagementAccessRecord":
        sub_type = STRING_TO_MANAGEMENT_ACCESS_RECORD_TYPE.get(
            data[yaml_names.MANAGEMENT_ACCESS_RECORD_SUB_TYPE_KEY]
        )
        return ManagementAccessRecord(
            sub_type=sub_type,
            data=VALUE_VALIDATORS[sub_type](
                parse_value(data[yaml_names.MANAGEMENT_ACCESS_RECORD_VALUE_KEY])
            ),
        )
