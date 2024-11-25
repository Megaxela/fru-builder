from tui.widgets.basic_section import BasicSection
from converter.internal.board_info_area import BoardInfoArea
from tui.language_code import language_code_to_text


class BoardInfoSection(BasicSection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.section_name = "Board Info"

    def description_fields(self):
        fields = [
            ("Language Code", language_code_to_text(self.area.language_code)),
        ]

        if self.area.manufacturing_datetime is not None:
            fields.append(
                ("Manufacturing Datetime", str(self.area.manufacturing_datetime))
            )

        self._add_ltvalue_to_fields(fields, "Manufacturer", self.area.manufacturer)
        self._add_ltvalue_to_fields(fields, "Product Name", self.area.product_name)
        self._add_ltvalue_to_fields(fields, "Serial Number", self.area.serial_number)
        self._add_ltvalue_to_fields(fields, "Part Number", self.area.part_number)
        self._add_ltvalue_to_fields(fields, "Fru File ID", self.area.fru_file_id)

        for custom_field in self.area.custom_manufacturing_fields:
            self._add_ltvalue_to_fields(fields, "Custom Info", custom_field)

        return fields

    @property
    def area(self) -> BoardInfoArea:
        return self.data
