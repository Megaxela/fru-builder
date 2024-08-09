import ctypes
import dataclasses
import typing as tp

from converter.internal.internal_use_area import InternalUseArea
from converter.internal.chassis_info_area import ChassisInfoArea
from converter.internal.board_info_area import BoardInfoArea
from converter.internal.product_info_area import ProductInfoArea
from converter.internal.multi_record_area import MultiRecordArea
from converter.internal.checksum import calculate_checksum
from converter.internal.errors import (
    YamlFormatError,
    FruValidationError,
)
import converter.internal.yaml_names as yaml_names

OFFSET_MUL = 8  # bytes

FRU_FORMAT_VERSION = 0b0000_0001
COMMON_HEADER_SIZE = 8  # bytes


class CommonHeaderStructure(ctypes.Structure):
    _fields_ = [
        ("format_version", ctypes.c_uint8),
        ("internal_use_area_starting_offset", ctypes.c_uint8),
        ("chassis_info_area_starting_offset", ctypes.c_uint8),
        ("board_area_starting_offset", ctypes.c_uint8),
        ("product_info_area_starting_offset", ctypes.c_uint8),
        ("multirecord_area_starting_offset", ctypes.c_uint8),
        ("pad", ctypes.c_uint8),
        ("header_checksum", ctypes.c_uint8),
    ]


@dataclasses.dataclass()
class FruData:
    internal_info: tp.Optional[InternalUseArea]
    chassis_info: tp.Optional[ChassisInfoArea]
    board_info: tp.Optional[BoardInfoArea]
    product_info: tp.Optional[ProductInfoArea]
    multirecord_area: tp.Optional[MultiRecordArea]

    def to_binary(self) -> bytes:
        result = bytearray()

        def serialize(result, area) -> int:
            if area is not None:
                data = area.to_binary()
                if data is not None:
                    offset = len(result) + COMMON_HEADER_SIZE
                    result += data
                    return offset // OFFSET_MUL
            return 0

        internal_use_offset = serialize(result, self.internal_info)
        chassis_info_offset = serialize(result, self.chassis_info)
        board_info_offset = serialize(result, self.board_info)
        product_info_offset = serialize(result, self.product_info)
        multirecord_offset = serialize(result, self.multirecord_area)

        common_header = CommonHeaderStructure(
            format_version=FRU_FORMAT_VERSION,
            internal_use_area_starting_offset=internal_use_offset,
            chassis_info_area_starting_offset=chassis_info_offset,
            board_area_starting_offset=board_info_offset,
            product_info_area_starting_offset=product_info_offset,
            multirecord_area_starting_offset=multirecord_offset,
            pad=0,
            header_checksum=0,
        )

        common_header.header_checksum = calculate_checksum(bytes(common_header))

        return bytes(bytearray(common_header) + result)

    def to_yaml(self) -> tp.Any:
        result = {}

        def parse(field, name):
            if field is not None:
                result[name] = field.to_yaml()
            else:
                result[name] = None

        parse(self.internal_info, yaml_names.AREA_INTERNAL_USE_KEY)
        parse(self.chassis_info, yaml_names.AREA_CHASSIS_INFO_KEY)
        parse(self.board_info, yaml_names.AREA_BOARD_INFO_KEY)
        parse(self.product_info, yaml_names.AREA_PRODUCT_INFO_KEY)
        parse(self.multirecord_area, yaml_names.AREA_MULTIRECORD_KEY)

        # todo: move global key to yaml converter
        return {yaml_names.ROOT_AREAS_KEY: result}

    @staticmethod
    def from_binary(data: bytes) -> "FruData":
        # Parsing common header
        common_header = CommonHeaderStructure.from_buffer_copy(data, 0)

        format_version = common_header.format_version & 0b0000_1111
        # if format_version != FRU_FORMAT_VERSION:
        #     raise FruValidationError(
        #         f"Fru format version '{format_version}' != '{FRU_FORMAT_VERSION}'"
        #     )

        internal_use_area: tp.Optional[InternalUseArea] = None
        if common_header.internal_use_area_starting_offset:
            internal_use_area = InternalUseArea.from_binary(
                data[common_header.internal_use_area_starting_offset * OFFSET_MUL :]
            )

        # Offsetting to chassis info and parsing it
        chassis_info_area: tp.Optional[ChassisInfoArea] = None
        if common_header.chassis_info_area_starting_offset:
            chassis_info_area = ChassisInfoArea.from_binary(
                data[common_header.chassis_info_area_starting_offset * OFFSET_MUL :]
            )

        # Offsetting to board info and parsing it
        board_info_area: tp.Optional[BoardInfoArea] = None
        if common_header.board_area_starting_offset:
            board_info_area = BoardInfoArea.from_binary(
                data[common_header.board_area_starting_offset * OFFSET_MUL :]
            )

        # Offsetting to product info area and parsing it
        product_info_area: tp.Optional[ProductInfoArea] = None
        if common_header.product_info_area_starting_offset:
            product_info_area = ProductInfoArea.from_binary(
                data[common_header.product_info_area_starting_offset * OFFSET_MUL :]
            )

        # Offsetting to multirecord area and parsing it
        multirecord_area: tp.Optional[MultiRecordArea] = None
        if common_header.multirecord_area_starting_offset:
            multirecord_area = MultiRecordArea.from_binary(
                data[common_header.multirecord_area_starting_offset * OFFSET_MUL :]
            )
        return FruData(
            internal_info=internal_use_area,
            chassis_info=chassis_info_area,
            board_info=board_info_area,
            product_info=product_info_area,
            multirecord_area=multirecord_area,
        )

    @staticmethod
    def from_yaml(data: tp.Any) -> "FruData":
        # todo: Probably mode this section to converter
        if yaml_names.ROOT_AREAS_KEY not in data:
            raise YamlFormatError(f"No root key '{yaml_names.ROOT_AREAS_KEY}'")
        data = data[yaml_names.ROOT_AREAS_KEY]

        mandatory_fields = [
            yaml_names.AREA_INTERNAL_USE_KEY,
            yaml_names.AREA_CHASSIS_INFO_KEY,
            yaml_names.AREA_BOARD_INFO_KEY,
            yaml_names.AREA_PRODUCT_INFO_KEY,
            yaml_names.AREA_MULTIRECORD_KEY,
        ]
        for field in mandatory_fields:
            if field not in data:
                raise YamlFormatError(f"Fru has no mandatory field '{field}'")

        def parse_with(cls, key):
            if not data[key]:
                return None
            return cls.from_yaml(data[key])

        return FruData(
            internal_info=parse_with(
                InternalUseArea,
                yaml_names.AREA_INTERNAL_USE_KEY,
            ),
            chassis_info=parse_with(
                ChassisInfoArea,
                yaml_names.AREA_CHASSIS_INFO_KEY,
            ),
            board_info=parse_with(
                BoardInfoArea,
                yaml_names.AREA_BOARD_INFO_KEY,
            ),
            product_info=parse_with(
                ProductInfoArea,
                yaml_names.AREA_PRODUCT_INFO_KEY,
            ),
            multirecord_area=parse_with(
                MultiRecordArea,
                yaml_names.AREA_MULTIRECORD_KEY,
            ),
        )
