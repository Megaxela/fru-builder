from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

from converter.internal.multi_record_type import MultiRecordType


class BasicInternalUse(ABC):

    @abstractmethod
    def probe(self, data: bytes) -> bool:
        pass

    @abstractmethod
    def to_binary(self, data: bytes) -> bytes:
        pass

    @abstractmethod
    def to_yaml(self):
        pass

    @abstractmethod
    def from_binary(self, data: bytes) -> BasicInternalUse:
        pass

    @abstractmethod
    def from_yaml(self, data: Any) -> BasicInternalUse:
        pass
