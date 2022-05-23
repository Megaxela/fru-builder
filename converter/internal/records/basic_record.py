import abc


class BasicRecord(abc.ABC):
    @abc.abstractmethod
    def from_binary(data: bytes) -> "BasicRecord":
        pass
