import dataclasses
import typing as tp
import datetime

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

PRODUCT_INFO_AREA_VERSION = 0b0000_0001
MAX_AREA_SIZE = 255


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

    def to_binary(self) -> bytes:
        result = bytearray()

        # 1 byte of product info area version
        result.append(PRODUCT_INFO_AREA_VERSION)

        # 1 byte of product info area version
        total_length = sum(
            (
                1,  # Product area format version
                1,  # Product area length
                1,  # Language code
                self.manufacturer_name.get_size(self.language_code),
                self.product_name.get_size(self.language_code),
                self.part_number.get_size(self.language_code),
                self.product_version.get_size(self.language_code),
                self.serial_number.get_size(LanguageCode.English),
                self.asset_tag.get_size(self.language_code),
                self.fru_file_id.get_size(self.language_code),
                sum(
                    (
                        field.get_size(self.language_code)
                        for field in self.custom_info_fields
                    )
                ),
                1,  # 0xC1 - no more fields
                1,  # Checksum
            )
        )
        aligned_length = total_length + (8 - (total_length % 8))

        if aligned_length > MAX_AREA_SIZE:
            raise FruValidationError(
                f"Total Product Info Area size {aligned_length} > {MAX_AREA_SIZE}"
            )

        result.append(aligned_length // 8)

        # 1 byte language code
        result.append(language_code_to_index(self.language_code))

        # 1 + N bytes of manufacturer name
        result += self.manufacturer_name.to_binary(self.language_code)

        # 1 + M bytes of product name
        result += self.product_name.to_binary(self.language_code)

        # 1 + O bytes of product part/model number
        result += self.part_number.to_binary(self.language_code)

        # 1 + R bytes of product version
        result += self.product_version.to_binary(self.language_code)

        # 1 + P bytes of serial number
        result += self.serial_number.to_binary(LanguageCode.English)

        # 1 + Q bytes of asset tag
        result += self.asset_tag.to_binary(self.language_code)

        # 1 + R bytes of fru file id
        result += self.fru_file_id.to_binary(self.language_code)

        # Custom fields
        for field in self.custom_info_fields:
            result += field.to_binary(self.language_code)

        # No more fields
        result.append(0xC1)

        # Add zeroes
        result += bytes([0x00]) * (aligned_length - total_length)

        # Add checksum
        result.append(calculate_checksum(result))

        return bytes(result)

    def to_yaml(self) -> tp.Any:
        return {
            yaml_names.PRODUCT_INFO_LANGUAGE_CODE_KEY: language_code_to_str(
                self.language_code
            ),
            yaml_names.PRODUCT_INFO_MANUFACTURER_NAME_KEY: self.manufacturer_name.to_yaml(),
            yaml_names.PRODUCT_INFO_PRODUCT_NAME_KEY: self.product_name.to_yaml(),
            yaml_names.PRODUCT_INFO_PART_NUMBER_KEY: self.part_number.to_yaml(),
            yaml_names.PRODUCT_INFO_PRODUCT_VERSION_KEY: self.product_version.to_yaml(),
            yaml_names.PRODUCT_INFO_SERIAL_NUMBER_KEY: self.serial_number.to_yaml(),
            yaml_names.PRODUCT_INFO_ASSET_TAG_KEY: self.asset_tag.to_yaml(),
            yaml_names.PRODUCT_INFO_FRU_FILE_ID_KEY: self.fru_file_id.to_yaml(),
            yaml_names.PRODUCT_INFO_CUSTOM_INFO_FIELDS_KEY: [
                field.to_yaml() for field in self.custom_info_fields
            ],
        }

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
