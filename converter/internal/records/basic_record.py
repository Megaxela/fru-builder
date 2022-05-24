import abc

from converter.internal.multi_record_type import MultiRecordType


class BasicRecord(abc.ABC):
    @abc.abstractproperty
    def record_type(self):
        return None

    @abc.abstractmethod
    def from_binary(data: bytes) -> "BasicRecord":
        pass
