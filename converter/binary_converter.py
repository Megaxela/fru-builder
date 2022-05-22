import ctypes
import typing as tp

from .basic_converter import BasicConverter
from .internal.chassis_info_area import ChassisInfoArea


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
        print(
            ChassisInfoArea.from_binary(
                data[common_header.chassis_info_area_starting_offset * 8 :]
            )
        )

    def from_internal(self, path: str, internal_data: tp.Any):
        pass
