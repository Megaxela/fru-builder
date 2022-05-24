import typing as tp

from .basic_converter import BasicConverter
from .internal.fru_data import FruData


class BinaryConverter(BasicConverter):
    def __init__(self):
        pass

    def to_internal(self, path: str) -> FruData:
        with open(path, "rb") as f:
            data = f.read()

        return FruData.from_binary(data)

    def from_internal(self, path: str, internal_data: FruData):
        with open(path, "wb") as f:
            f.write(internal_data.to_binary())
