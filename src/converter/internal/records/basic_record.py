from abc import ABC, abstractproperty, abstractmethod
from typing import Any

from converter.internal.multi_record_type import MultiRecordType


class BasicRecord(ABC):
    @abstractproperty
    def record_type(self):
        return None

    @abstractmethod
    def to_binary(self, data: bytes) -> bytes:
        pass

    @abstractmethod
    def to_yaml(self):
        pass

    @abstractmethod
    def from_binary(self, data: bytes) -> "BasicRecord":
        pass

    @abstractmethod
    def from_yaml(self, data: Any) -> "BasicRecord":
        pass
