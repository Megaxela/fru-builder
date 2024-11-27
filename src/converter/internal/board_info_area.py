from dataclasses import dataclass
from typing import List, Any
from datetime import datetime, timedelta

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

BOARD_INFO_AREA_VERSION = 0b0000_0001
MANUFACTURING_START_DATE = datetime(1996, 1, 1, 0, 0)
MAX_AREA_SIZE = 255


@dataclass()
class BoardInfoArea:
    language_code: LanguageCode
    manufacturing_datetime: datetime | None
    manufacturer: LengthTypeValue
    product_name: LengthTypeValue
    serial_number: LengthTypeValue
    part_number: LengthTypeValue
    fru_file_id: LengthTypeValue
    custom_manufacturing_fields: List[LengthTypeValue]

    def to_binary(self) -> bytes:
        result = bytearray()

        # 1 byte of board info area format version
        result.append(BOARD_INFO_AREA_VERSION)

        # 1 byte of board info area length
        total_length = sum(
            (
                1,  # Board info area version
                1,  # Board info area length
                1,  # Language code
                3,  # Manufacturing datetime
                self.manufacturer.get_size(self.language_code),
                self.product_name.get_size(self.language_code),
                self.serial_number.get_size(LanguageCode.English),
                self.part_number.get_size(self.language_code),
                self.fru_file_id.get_size(LanguageCode.English),
                sum(
                    (
                        field.get_size(self.language_code)
                        for field in self.custom_manufacturing_fields
                    )
                ),
                1,  # 0xC1 - no more fields
                1,  # Checksum
            )
        )
        aligned_length = total_length + (8 - (total_length % 8))

        if aligned_length > MAX_AREA_SIZE:
            raise FruValidationError(
                f"Total Board Info Area size {aligned_length} > {MAX_AREA_SIZE}"
            )

        result.append(aligned_length // 8)

        # 1 byte language code
        result.append(language_code_to_index(self.language_code))

        # 3 bytes manufacturing date/time
        if self.manufacturing_datetime is not None:
            if self.manufacturing_datetime < MANUFACTURING_START_DATE:
                raise FruValidationError(
                    f"Date {self.manufacturing_datetime} is less than {MANUFACTURING_START_DATE}"
                )

            minutes = (
                int(
                    (
                        self.manufacturing_datetime - MANUFACTURING_START_DATE
                    ).total_seconds()
                )
                // 60
            )
            result += int.to_bytes(minutes, 3, byteorder="little", signed=False)
        else:
            result += bytes([0x00, 0x00, 0x00])

        # 1 + P bytes of board manufacturer
        result += self.manufacturer.to_binary(self.language_code)

        # 1 + Q bytes of board product name
        result += self.product_name.to_binary(self.language_code)

        # 1 + N bytes of board serial number
        result += self.serial_number.to_binary(LanguageCode.English)

        # 1 + M bytes of board part number
        result += self.part_number.to_binary(self.language_code)

        # 1 + R bytes of FRU File ID
        result += self.fru_file_id.to_binary(LanguageCode.English)

        # Extra fields
        for field in self.custom_manufacturing_fields:
            result += field.to_binary(self.language_code)

        # No more fields
        result.append(0xC1)

        # Add zeroes
        result += bytes([0x00]) * (aligned_length - total_length)

        # Add checksum
        result.append(calculate_checksum(result))

        return bytes(result)

    def to_yaml(self) -> Any:
        result = {
            yaml_names.BOARD_INFO_LANGUAGE_CODE_KEY: language_code_to_str(
                self.language_code
            ),
        }

        if self.manufacturing_datetime is not None:
            result[yaml_names.BOARD_INFO_MANUFACTURING_DATETIME_KEY] = (
                self.manufacturing_datetime
            )

        result.update(
            {
                yaml_names.BOARD_INFO_MANUFACTURER_KEY: self.manufacturer.to_yaml(),
                yaml_names.BOARD_INFO_PRODUCT_NAME_KEY: self.product_name.to_yaml(),
                yaml_names.BOARD_INFO_SERIAL_NUMBER_KEY: self.serial_number.to_yaml(),
                yaml_names.BOARD_INFO_PART_NUMBER_KEY: self.part_number.to_yaml(),
                yaml_names.BOARD_INFO_FRU_FILE_ID_KEY: self.fru_file_id.to_yaml(),
                yaml_names.BOARD_INFO_CUSTOM_INFO_FIELDS_KEY: [
                    field.to_yaml() for field in self.custom_manufacturing_fields
                ],
            }
        )

        return result

    @staticmethod
    def from_binary(data: bytes) -> "BoardInfoArea":
        # Validate version
        pointer = 0
        if data[pointer] != BOARD_INFO_AREA_VERSION:
            raise FruValidationError(
                f"Board Info Area version {data[0]} is not {BOARD_INFO_AREA_VERSION}"
            )
        pointer += 1

        # We do not use this
        # structure_length_bytes = data[pointer] * 8
        pointer += 1

        language_code = index_to_language_code(data[pointer])
        pointer += 1

        manufacturing_datetime = None
        if data[pointer : pointer + 3] != b"\x00\x00\x00":
            # Minutes since 0:00 01-01-1996
            minutes = int.from_bytes(data[pointer : pointer + 3], byteorder="little")
            manufacturing_datetime = MANUFACTURING_START_DATE + timedelta(
                minutes=minutes
            )
        pointer += 3

        manufacturer = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + manufacturer.length_type.number_of_data_bytes

        product_name = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + product_name.length_type.number_of_data_bytes

        serial_number = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=LanguageCode.English,
        )
        pointer += 1 + serial_number.length_type.number_of_data_bytes

        part_number = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + part_number.length_type.number_of_data_bytes

        fru_file_id = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=LanguageCode.English,
        )
        pointer += 1 + fru_file_id.length_type.number_of_data_bytes

        custom_manufacturing_fields = []
        while True:
            result = LengthTypeValue.from_binary(
                length_type_ptr=data[pointer : pointer + 1],
                value_ptr=data[pointer + 1 :],
                language_code=language_code,
            )
            # None at end of fields.
            if result is None:
                pointer += 1
                break
            pointer += 1 + result.length_type.number_of_data_bytes
            custom_manufacturing_fields.append(result)
        # Fillr zeros and checksum are ignored for now.
        # todo: add checksum validation

        return BoardInfoArea(
            language_code=language_code,
            manufacturing_datetime=manufacturing_datetime,
            manufacturer=manufacturer,
            product_name=product_name,
            serial_number=serial_number,
            part_number=part_number,
            fru_file_id=fru_file_id,
            custom_manufacturing_fields=custom_manufacturing_fields,
        )

    @staticmethod
    def from_yaml(data: Any) -> "BoardInfoArea":
        mandatory_fields = [
            # yaml_names.BOARD_INFO_MANUFACTURING_DATETIME_KEY,
            yaml_names.BOARD_INFO_MANUFACTURER_KEY,
            yaml_names.BOARD_INFO_PRODUCT_NAME_KEY,
            yaml_names.BOARD_INFO_SERIAL_NUMBER_KEY,
            yaml_names.BOARD_INFO_PART_NUMBER_KEY,
            yaml_names.BOARD_INFO_FRU_FILE_ID_KEY,
            yaml_names.BOARD_INFO_CUSTOM_INFO_FIELDS_KEY,
        ]
        for field in mandatory_fields:
            if field not in data:
                raise YamlFormatError(
                    f"Board Info Area has no mandatory field '{field}'"
                )

        # todo: validate that datetime is actually datetime

        return BoardInfoArea(
            language_code=str_to_language_code(
                data[yaml_names.BOARD_INFO_LANGUAGE_CODE_KEY]
            ),
            manufacturing_datetime=data.get(
                yaml_names.BOARD_INFO_MANUFACTURING_DATETIME_KEY
            ),
            manufacturer=LengthTypeValue.from_yaml(
                data[yaml_names.BOARD_INFO_MANUFACTURER_KEY]
            ),
            product_name=LengthTypeValue.from_yaml(
                data[yaml_names.BOARD_INFO_PRODUCT_NAME_KEY]
            ),
            serial_number=LengthTypeValue.from_yaml(
                data[yaml_names.BOARD_INFO_SERIAL_NUMBER_KEY]
            ),
            part_number=LengthTypeValue.from_yaml(
                data[yaml_names.BOARD_INFO_PART_NUMBER_KEY]
            ),
            fru_file_id=LengthTypeValue.from_yaml(
                data[yaml_names.BOARD_INFO_FRU_FILE_ID_KEY]
            ),
            custom_manufacturing_fields=[
                LengthTypeValue.from_yaml(field)
                for field in data[yaml_names.BOARD_INFO_CUSTOM_INFO_FIELDS_KEY]
            ],
        )
