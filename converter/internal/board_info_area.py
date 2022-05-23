import dataclasses
import typing as tp
import datetime

import converter.internal.yaml_names as yaml_names
from converter.internal.language_codes import (
    LanguageCode,
    index_to_language_code,
    str_to_language_code,
)
from converter.internal.length_type_value import LengthTypeValue
from converter.internal.errors import (
    FruValidationError,
    YamlFormatError,
)

BOARD_INFO_AREA_VERSION = 0b0000_0001


@dataclasses.dataclass()
class BoardInfoArea:
    language_code: LanguageCode
    manufacturing_datetime: tp.Optional[datetime.datetime]
    manufacturer: LengthTypeValue
    product_name: LengthTypeValue
    serial_number: LengthTypeValue
    part_number: LengthTypeValue
    fru_file_id: LengthTypeValue
    custom_manufacturing_fields: tp.List[LengthTypeValue]

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
            minutes = int.from_bytes(data[pointer : pointer + 3], byteorder="big")
            manufacturing_datetime = datetime.datetime(
                1996, 1, 1, 0, 0
            ) + datetime.timedelta(minutes=minutes)
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
    def from_yaml(data: tp.Any) -> "BoardInfoArea":
        mandatory_fields = [
            yaml_names.BOARD_INFO_MANUFACTURING_DATETIME_KEY,
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
            manufacturing_datetime=data[
                yaml_names.BOARD_INFO_MANUFACTURING_DATETIME_KEY
            ],
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
