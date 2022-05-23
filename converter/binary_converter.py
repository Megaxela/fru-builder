import ctypes
import typing as tp
import pprint

from .basic_converter import BasicConverter
from .internal.chassis_info_area import ChassisInfoArea
from .internal.board_info_area import BoardInfoArea
from .internal.product_info_area import ProductInfoArea
from .internal.multi_record_area import MultiRecordArea

OFFSET_MUL = 8


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


class BinaryConverter(BasicConverter):
    def __init__(self):
        pass

    def to_internal(self, path: str) -> tp.Any:
        with open(path, "rb") as f:
            data = f.read()

        # Parsing common header
        common_header = CommonHeaderStructure.from_buffer_copy(data, 0)

        # Offsetting to chassis info and parsing it
        chassis_info: tp.Optional[ChassisInfoArea] = None
        if common_header.chassis_info_area_starting_offset:
            chassis_info = ChassisInfoArea.from_binary(
                data[common_header.chassis_info_area_starting_offset * OFFSET_MUL :]
            )

        # Offsetting to board info and parsing it
        board_info_area: tp.Optional[BoardInfoArea] = None
        if common_header.board_area_starting_offset:
            board_info_area = BoardInfoArea.from_binary(
                data[common_header.board_area_starting_offset * OFFSET_MUL :]
            )

        product_info_area: tp.Optional[ProductInfoArea] = None
        if common_header.product_info_area_starting_offset:
            product_info_area = ProductInfoArea.from_binary(
                data[common_header.product_info_area_starting_offset * OFFSET_MUL :]
            )

        multirecord_area: tp.Optional[MultiRecordArea] = None
        if common_header.multirecord_area_starting_offset:
            multirecord_area = MultiRecordArea.from_binary(
                data[common_header.multirecord_area_starting_offset * OFFSET_MUL :]
            )

        pprint.pprint(chassis_info)
        pprint.pprint(board_info_area)
        pprint.pprint(product_info_area)
        pprint.pprint(multirecord_area)

    def from_internal(self, path: str, internal_data: tp.Any):
        pass
