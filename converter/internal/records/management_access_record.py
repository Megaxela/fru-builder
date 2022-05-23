import dataclasses
import enum
import typing as tp

from converter.internal.records.basic_record import BasicRecord
import converter.internal.yaml_names as yaml_names
from converter.internal.length_type_value import parse_value


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
    def check(_, length):
        if not start <= (length + 1) <= end:
            raise ValueError(
                f"Value length {length} is out of range [{start - 1}, {end - 1}]"
            )

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
    data: bytes

    def from_binary(data: bytes) -> "ManagementAccessRecord":
        return ManagementAccessRecord(
            sub_type=ManagementAccessRecordType(data[0]),
            data=data[1:],
        )

    def from_yaml(data: tp.Any) -> "ManagementAccessRecord":
        return ManagementAccessRecord(
            sub_type=STRING_TO_MANAGEMENT_ACCESS_RECORD_TYPE.get(
                data[yaml_names.MANAGEMENT_ACCESS_RECORD_SUB_TYPE_KEY]
            ),
            data=parse_value(data[yaml_names.MANAGEMENT_ACCESS_RECORD_VALUE_KEY]),
        )
