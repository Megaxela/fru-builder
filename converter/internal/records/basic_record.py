import abc
import typing as tp

from converter.internal.multi_record_type import MultiRecordType


class BasicRecord(abc.ABC):
    @abc.abstractproperty
    def record_type(self):
        return None

    @abc.abstractmethod
    def to_binary(self, data: bytes) -> bytes:
        pass

    @abc.abstractmethod
    def to_yaml(self):
        pass

    @abc.abstractmethod
    def from_binary(self, data: bytes) -> "BasicRecord":
        pass

    @abc.abstractmethod
    def from_yaml(self, data: tp.Any) -> "BasicRecord":
        pass
