import abc
import typing as tp


class BasicConverter(abc.ABC):
    @abc.abstractmethod
    def to_internal(self, path: str) -> tp.Any:
        pass

    @abc.abstractmethod
    def from_internal(self, path: str, internal_data: tp.Any):
        pass
