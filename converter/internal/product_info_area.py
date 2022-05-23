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

PRODUCT_INFO_AREA_VERSION = 0b0000_0001


@dataclasses.dataclass()
class ProductInfoArea:
    language_code: LanguageCode
    manufacturer_name: LengthTypeValue
    product_name: LengthTypeValue
    part_number: LengthTypeValue
    product_version: LengthTypeValue
    serial_number: LengthTypeValue
    asset_tag: LengthTypeValue
    fru_file_id: LengthTypeValue
    custom_info_fields: tp.List[LengthTypeValue]

    @staticmethod
    def from_binary(data: bytes) -> "ProductInfoArea":
        # Validate version
        pointer = 0
        if data[pointer] != PRODUCT_INFO_AREA_VERSION:
            raise FruValidationError(
                f"Product Info Area version {data[0]} is not {PRODUCT_INFO_AREA_VERSION}"
            )
        pointer += 1

        # We do not use this
        # structure_length_bytes = data[pointer] * 8
        pointer += 1

        language_code = index_to_language_code(data[pointer])
        pointer += 1

        manufacturer_name = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + manufacturer_name.length_type.number_of_data_bytes

        product_name = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + product_name.length_type.number_of_data_bytes

        part_number = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + part_number.length_type.number_of_data_bytes

        product_version = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + product_version.length_type.number_of_data_bytes

        serial_number = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=LanguageCode.English,
        )
        pointer += 1 + serial_number.length_type.number_of_data_bytes

        asset_tag = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + asset_tag.length_type.number_of_data_bytes

        fru_file_id = LengthTypeValue.from_binary(
            length_type_ptr=data[pointer : pointer + 1],
            value_ptr=data[pointer + 1 :],
            language_code=language_code,
        )
        pointer += 1 + fru_file_id.length_type.number_of_data_bytes

        custom_info_fields = []
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
            custom_info_fields.append(result)

        return ProductInfoArea(
            language_code=language_code,
            manufacturer_name=manufacturer_name,
            product_name=product_name,
            part_number=part_number,
            product_version=product_version,
            serial_number=serial_number,
            asset_tag=asset_tag,
            fru_file_id=fru_file_id,
            custom_info_fields=custom_info_fields,
        )

    @staticmethod
    def from_yaml(data: tp.Any) -> "ProductInfoArea":
        mandatory_fields = [
            yaml_names.PRODUCT_INFO_LANGUAGE_CODE_KEY,
            yaml_names.PRODUCT_INFO_MANUFACTURER_NAME_KEY,
            yaml_names.PRODUCT_INFO_PRODUCT_NAME_KEY,
            yaml_names.PRODUCT_INFO_PART_NUMBER_KEY,
            yaml_names.PRODUCT_INFO_PRODUCT_VERSION_KEY,
            yaml_names.PRODUCT_INFO_SERIAL_NUMBER_KEY,
            yaml_names.PRODUCT_INFO_ASSET_TAG_KEY,
            yaml_names.PRODUCT_INFO_FRU_FILE_ID_KEY,
            yaml_names.PRODUCT_INFO_CUSTOM_INFO_FIELDS_KEY,
        ]

        for field in mandatory_fields:
            if field not in data:
                raise YamlFormatError(
                    f"Product Info Area has no mandatory field '{field}'"
                )

        return ProductInfoArea(
            language_code=str_to_language_code(
                data[yaml_names.PRODUCT_INFO_LANGUAGE_CODE_KEY]
            ),
            manufacturer_name=LengthTypeValue.from_yaml(
                data[yaml_names.PRODUCT_INFO_MANUFACTURER_NAME_KEY]
            ),
            product_name=LengthTypeValue.from_yaml(
                data[yaml_names.PRODUCT_INFO_PRODUCT_NAME_KEY]
            ),
            part_number=LengthTypeValue.from_yaml(
                data[yaml_names.PRODUCT_INFO_PART_NUMBER_KEY]
            ),
            product_version=LengthTypeValue.from_yaml(
                data[yaml_names.PRODUCT_INFO_PRODUCT_VERSION_KEY]
            ),
            serial_number=LengthTypeValue.from_yaml(
                data[yaml_names.PRODUCT_INFO_SERIAL_NUMBER_KEY]
            ),
            asset_tag=LengthTypeValue.from_yaml(
                data[yaml_names.PRODUCT_INFO_ASSET_TAG_KEY]
            ),
            fru_file_id=LengthTypeValue.from_yaml(
                data[yaml_names.PRODUCT_INFO_FRU_FILE_ID_KEY]
            ),
            custom_info_fields=[
                LengthTypeValue.from_yaml(field)
                for field in data[yaml_names.PRODUCT_INFO_CUSTOM_INFO_FIELDS_KEY]
            ],
        )
