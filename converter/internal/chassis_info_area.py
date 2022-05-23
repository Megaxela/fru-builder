import enum
import dataclasses
import typing as tp

import converter.internal.yaml_names as yaml_names
from converter.internal.language_codes import LanguageCode
from converter.internal.length_type_value import LengthTypeValue
from converter.internal.chassis_type import (
    ChassisType,
    value_to_chassis_type,
    name_to_chassis_type,
)
from converter.internal.errors import (
    FruValidationError,
    YamlFormatError,
)

CHASSIS_INFO_AREA_VERSION = 0b0000_0001


@dataclasses.dataclass()
class ChassisInfoArea:
    chassis_type: ChassisType
    part_number: LengthTypeValue
    serial_number: LengthTypeValue
    custom_info_fields: tp.List[LengthTypeValue]

    @staticmethod
    def from_binary(data: bytes) -> "ChassisInfoArea":
        # Validate version
        pointer = 0
        if data[pointer] != CHASSIS_INFO_AREA_VERSION:
            raise FruValidationError(
                f"Chassis Info Area version {data[0]} is not {CHASSIS_INFO_AREA_VERSION}"
            )
        pointer += 1

        # We do not use this.
        # structure_length_bytes = data[pointer] * 8
        pointer += 1

        chassis_type = value_to_chassis_type(data[pointer])
        pointer += 1

        part_number = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=LanguageCode.English,  # Chassis Info is always English
        )
        pointer += 1 + part_number.length_type.number_of_data_bytes

        serial_number = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=LanguageCode.English,  # Chassis Info is always English
        )
        pointer += 1 + serial_number.length_type.number_of_data_bytes

        # Iterating through custom fields
        custom_fields = []
        while True:
            result = LengthTypeValue.from_binary(
                length_type_ptr=data[pointer : pointer + 1],
                value_ptr=data[pointer + 1 :],
                language_code=LanguageCode.English,  # Chassis Info is always English
            )
            # None at end of fields.
            if result is None:
                pointer += 1
                break
            pointer += 1 + result.length_type.number_of_data_bytes
            custom_fields.append(result)
        # Filler zeros and checksum are ignored for now.
        # todo: add checksum validation

        return ChassisInfoArea(
            chassis_type=chassis_type,
            part_number=part_number,
            serial_number=serial_number,
            custom_info_fields=custom_fields,
        )

    @staticmethod
    def from_yaml(data: tp.Any) -> "ChassisInfoArea":
        mandatory_fields = [
            yaml_names.CHASSIS_INFO_CHASSIS_TYPE_YAML_KEY,
            yaml_names.CHASSIS_INFO_PART_NUMBER_YAML_KEY,
            yaml_names.CHASSIS_INFO_SERIAL_NUMBER_YAML_KEY,
            yaml_names.CHASSIS_INFO_CUSTOM_INFO_FIELDS_YAML_KEY,
        ]
        for field in mandatory_fields:
            if field not in data:
                raise YamlFormatError(
                    f"Chassis Info Area has no mandatory field '{field}'"
                )

        return ChassisInfoArea(
            chassis_type=name_to_chassis_type(
                data[yaml_names.CHASSIS_INFO_CHASSIS_TYPE_YAML_KEY]
            ),
            part_number=LengthTypeValue.from_yaml(
                data[yaml_names.CHASSIS_INFO_PART_NUMBER_YAML_KEY]
            ),
            serial_number=LengthTypeValue.from_yaml(
                data[yaml_names.CHASSIS_INFO_SERIAL_NUMBER_YAML_KEY]
            ),
            custom_info_fields=[
                LengthTypeValue.from_yaml(field)
                for field in data[yaml_names.CHASSIS_INFO_CUSTOM_INFO_FIELDS_YAML_KEY]
            ],
        )

    def to_binary(self):
        pass
