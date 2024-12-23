from abc import abstractmethod, abstractproperty

from converter.internal.records.basic_record import BasicRecord


class BasicOemRecord(BasicRecord):
    @abstractproperty
    def manufacturer_id(self) -> int:
        pass

    def _build_oem_record_header(self) -> bytearray:
        result = bytearray()

        result.append(self.manufacturer_id >> 0 & 0xFF)
        result.append(self.manufacturer_id >> 8 & 0xFF)
        result.append(self.manufacturer_id >> 16 & 0xFF)

        return result

    @abstractmethod
    def from_binary(data: bytes) -> "BasicRecord":
        pass
