import dataclasses

from converter.internal.records.basic_record import BasicRecord


@dataclasses.dataclass()
class PowerSupplyInformationRecord(BasicRecord):
    def from_binary(data: bytes) -> "PowerSupplyInformationRecord":
        pass
