from dataclasses import dataclass
from typing import List, Any

import converter.internal.yaml_names as yaml_names
from converter.internal.checksum import calculate_checksum
from converter.internal.language_codes import LanguageCode
from converter.internal.length_type_value import LengthTypeValue
from converter.internal.chassis_type import (
    ChassisType,
    value_to_chassis_type,
    name_to_chassis_type,
    chassis_type_to_name,
    chassis_type_to_value,
)
from converter.internal.errors import (
    FruValidationError,
    YamlFormatError,
)

CHASSIS_INFO_AREA_VERSION = 0b0000_0001
MAX_AREA_SIZE = 255


@dataclass()
class ChassisInfoArea:
    chassis_type: ChassisType
    part_number: LengthTypeValue
    serial_number: LengthTypeValue
    custom_info_fields: List[LengthTypeValue]

    def to_binary(self) -> bytes:
        result = bytearray()

        # 1 byte of chassis info area version
        result.append(CHASSIS_INFO_AREA_VERSION)

        # 1 byte of chassis info area length
        total_length = sum(
            (
                1,  # Chassis info area version
                1,  # Chassis info area length
                1,  # Chassis type
                self.part_number.get_size(LanguageCode.English),
                self.serial_number.get_size(LanguageCode.English),
                sum(
                    [
                        field.get_size(LanguageCode.English)
                        for field in self.custom_info_fields
                    ]
                ),
                1,  # 0xC1 - no more fields
                1,  # Checksum
            )
        )
        aligned_length = total_length + (8 - (total_length % 8))

        if aligned_length > MAX_AREA_SIZE:
            raise FruValidationError(
                f"Total Chassis Info Area size {aligned_length} > {MAX_AREA_SIZE}"
            )

        result.append(aligned_length // 8)

        # 1 byte chassis type
        result.append(chassis_type_to_value(self.chassis_type))

        # 1 + N bytes of chassis part number
        result += self.part_number.to_binary()

        # 1 + M bytes of chassis serial number
        result += self.serial_number.to_binary(LanguageCode.English)

        # Extra fields
        for field in self.custom_info_fields:
            result += field.to_binary()

        # No more fields
        result.append(0xC1)

        # Add zeroes
        result += bytes([0x00]) * (aligned_length - total_length)

        # Add checksum
        result.append(calculate_checksum(result))

        return bytes(result)

    def to_yaml(self) -> Any:
        return {
            yaml_names.CHASSIS_INFO_CHASSIS_TYPE_KEY: chassis_type_to_name(
                self.chassis_type
            ),
            yaml_names.CHASSIS_INFO_PART_NUMBER_KEY: self.part_number.to_yaml(),
            yaml_names.CHASSIS_INFO_SERIAL_NUMBER_KEY: self.serial_number.to_yaml(),
            yaml_names.CHASSIS_INFO_CUSTOM_INFO_FIELDS_KEY: [
                field.to_yaml() for field in self.custom_info_fields
            ],
        }

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
    def from_yaml(data: Any) -> "ChassisInfoArea":
        mandatory_fields = [
            yaml_names.CHASSIS_INFO_CHASSIS_TYPE_KEY,
            yaml_names.CHASSIS_INFO_PART_NUMBER_KEY,
            yaml_names.CHASSIS_INFO_SERIAL_NUMBER_KEY,
            yaml_names.CHASSIS_INFO_CUSTOM_INFO_FIELDS_KEY,
        ]
        for field in mandatory_fields:
            if field not in data:
                raise YamlFormatError(
                    f"Chassis Info Area has no mandatory field '{field}'"
                )

        return ChassisInfoArea(
            chassis_type=name_to_chassis_type(
                data[yaml_names.CHASSIS_INFO_CHASSIS_TYPE_KEY]
            ),
            part_number=LengthTypeValue.from_yaml(
                data[yaml_names.CHASSIS_INFO_PART_NUMBER_KEY]
            ),
            serial_number=LengthTypeValue.from_yaml(
                data[yaml_names.CHASSIS_INFO_SERIAL_NUMBER_KEY]
            ),
            custom_info_fields=[
                LengthTypeValue.from_yaml(field)
                for field in data[yaml_names.CHASSIS_INFO_CUSTOM_INFO_FIELDS_KEY]
            ],
        )
