from dataclasses import dataclass

from converter.internal.records.basic_record import BasicRecord


@dataclass()
class PowerSupplyInformationRecord(BasicRecord):
    def from_binary(data: bytes) -> "PowerSupplyInformationRecord":
        pass
