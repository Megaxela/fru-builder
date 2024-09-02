import abc
import typing as tp

from converter.internal.multi_record_type import MultiRecordType


class BasicInternalUse(abc.ABC):

    @abc.abstractmethod
    def probe(self, data: bytes) -> bool:
        pass

    @abc.abstractmethod
    def to_binary(self, data: bytes) -> bytes:
        pass

    @abc.abstractmethod
    def to_yaml(self):
        pass

    @abc.abstractmethod
    def from_binary(self, data: bytes) -> "BasicInternalUse":
        pass

    @abc.abstractmethod
    def from_yaml(self, data: tp.Any) -> "BasicInternalUse":
        pass
