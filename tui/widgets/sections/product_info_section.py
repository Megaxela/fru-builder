from tui.widgets.basic_section import BasicSection
from converter.internal.product_info_area import ProductInfoArea
from tui.language_code import language_code_to_text


class ProductInfoSection(BasicSection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.section_name = "Product Info"

    def description_fields(self):
        fields = [
            ("Language Code", language_code_to_text(self.data.language_code)),
        ]

        self._add_ltvalue_to_fields(fields, "Manufacturer", self.area.manufacturer_name)
        self._add_ltvalue_to_fields(fields, "Product Name", self.area.product_name)
        self._add_ltvalue_to_fields(fields, "Part Number", self.area.part_number)
        self._add_ltvalue_to_fields(
            fields, "Product Version", self.area.product_version
        )
        self._add_ltvalue_to_fields(fields, "Serial Number", self.area.serial_number)
        self._add_ltvalue_to_fields(fields, "Asset Tag", self.area.asset_tag)
        self._add_ltvalue_to_fields(fields, "Fru File ID", self.area.fru_file_id)

        for custom_field in self.area.custom_info_fields:
            self._add_ltvalue_to_fields(fields, "Custom Info", custom_field)

        return fields

    @property
    def area(self) -> ProductInfoArea:
        return self.data
