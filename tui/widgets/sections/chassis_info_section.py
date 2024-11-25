from tui.widgets.basic_section import BasicSection
from converter.internal.chassis_info_area import ChassisInfoArea
from converter.internal.chassis_type import (
    CHASSIS_TYPE_TO_NAME_MAP,
)  # todo: replace it with human readable types


class ChassisInfoSection(BasicSection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.section_name = "Chassis Info"

    def description_fields(self):
        fields = [
            ("Chassis Type", CHASSIS_TYPE_TO_NAME_MAP[self.data.chassis_type]),
        ]

        self._add_ltvalue_to_fields(fields, "Part Number", self.area.part_number)
        self._add_ltvalue_to_fields(fields, "Serial Number", self.area.serial_number)

        for custom_field in self.area.custom_info_fields:
            self._add_ltvalue_to_fields(fields, "Custom Info", custom_field)

        return fields

    @property
    def area(self) -> ChassisInfoArea:
        return self.data
