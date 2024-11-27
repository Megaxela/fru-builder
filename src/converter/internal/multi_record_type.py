from aenum import Enum


def make_multirecord_type_id(manufacturer_id, type_id):
    return type_id | (manufacturer_id << 8)


class MultiRecordType(Enum):
    # Default Values from specification
    PowerSupplyInformation = 0x00
    DCOutput = 0x01
    DCLoad = 0x02
    ManagementAccessRecord = 0x03
    BaseCompatibilityRecord = 0x04
    ExtendedCompatibilityRecord = 0x05
    ExtendedDCOutput = 0x06
    ExtendedDCLoad = 0x07


MULTI_RECORD_TYPE_TO_NAME_MAP = {
    # Default Values from specification
    MultiRecordType.PowerSupplyInformation: "power_supply_information",
    MultiRecordType.DCOutput: "dc_output",
    MultiRecordType.DCLoad: "dc_load",
    MultiRecordType.ManagementAccessRecord: "management_access",
    MultiRecordType.BaseCompatibilityRecord: "base_compatibility",
    MultiRecordType.ExtendedCompatibilityRecord: "extended_compatibility",
    MultiRecordType.ExtendedDCOutput: "extended_dc_output",
    MultiRecordType.ExtendedDCLoad: "extended_dc_load",
}

NAME_TO_MULTI_RECORD_TYPE_MAP = {
    MULTI_RECORD_TYPE_TO_NAME_MAP[  #
        MultiRecordType.PowerSupplyInformation  #
    ]: MultiRecordType.PowerSupplyInformation,
    MULTI_RECORD_TYPE_TO_NAME_MAP[  #
        MultiRecordType.DCOutput  #
    ]: MultiRecordType.DCOutput,
    MULTI_RECORD_TYPE_TO_NAME_MAP[  #
        MultiRecordType.DCLoad  #
    ]: MultiRecordType.DCLoad,  #
    MULTI_RECORD_TYPE_TO_NAME_MAP[  #
        MultiRecordType.ManagementAccessRecord  #
    ]: MultiRecordType.ManagementAccessRecord,
    MULTI_RECORD_TYPE_TO_NAME_MAP[  #
        MultiRecordType.BaseCompatibilityRecord  #
    ]: MultiRecordType.BaseCompatibilityRecord,
    MULTI_RECORD_TYPE_TO_NAME_MAP[  #
        MultiRecordType.ExtendedCompatibilityRecord
    ]: MultiRecordType.ExtendedCompatibilityRecord,
    MULTI_RECORD_TYPE_TO_NAME_MAP[  #
        MultiRecordType.ExtendedDCOutput  #
    ]: MultiRecordType.ExtendedDCOutput,
    MULTI_RECORD_TYPE_TO_NAME_MAP[  #
        MultiRecordType.ExtendedDCLoad  #
    ]: MultiRecordType.ExtendedDCLoad,
}


def str_to_multi_record_type(name: str) -> MultiRecordType | None:
    lc_name = name.lower()
    val = NAME_TO_MULTI_RECORD_TYPE_MAP.get(lc_name)
    if val is None:
        raise ValueError(
            f"Unknown multirecord type '{lc_name}'. Available values: [{', '.join(NAME_TO_MULTI_RECORD_TYPE_MAP.keys())}]"
        )
    return val


def multi_record_type_to_str(t: MultiRecordType) -> str:
    return MULTI_RECORD_TYPE_TO_NAME_MAP.get(t)


def multi_record_type_to_index(t: MultiRecordType) -> int:
    return t.value & 0xFF


def index_to_multi_record_type(
    index: int,
    manufacturer_id: int = 0,
) -> MultiRecordType | None:
    return MultiRecordType(make_multirecord_type_id(manufacturer_id, index))
