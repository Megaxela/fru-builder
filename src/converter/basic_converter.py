from abc import ABC, abstractmethod
from typing import Any


class BasicConverter(ABC):
    @abstractmethod
    def to_internal(self, path: str) -> Any:
        pass

    @abstractmethod
    def from_internal(self, path: str, internal_data: Any):
        pass
