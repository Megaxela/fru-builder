from textual.app import ComposeResult
from textual.containers import VerticalGroup
from textual.widgets import Label, Select, MaskedInput

from tui.widgets.basic_section_editor import BasicSectionEditor
from tui.widgets.section_ids import BOARD_INFO_ID
from tui.language_code import LANGUAGE_CODE_TEXT_TO_VALUE_MAP
from tui.widgets.value_type_editor import ValueTypeEditor
from tui.widgets.datetime_editor import DateTimeEditor


class BoardInfoSectionEditor(BasicSectionEditor):
    SECTION_ID = BOARD_INFO_ID

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        with VerticalGroup():
            yield Label("Language Code")
            yield Select(
                sorted(LANGUAGE_CODE_TEXT_TO_VALUE_MAP.items(), key=lambda x: x[0]),
                allow_blank=False,
                value=self.section.language_code,
            )

        with VerticalGroup():
            yield Label("Manufacturing Datetime")
            yield DateTimeEditor(self.section.manufacturing_datetime)

        with VerticalGroup():
            yield Label("Manufacturer")
            yield ValueTypeEditor(self.section.manufacturer)

        with VerticalGroup():
            yield Label("Product Name")
            yield ValueTypeEditor(self.section.product_name)

        with VerticalGroup():
            yield Label("Serial Number")
            yield ValueTypeEditor(self.section.serial_number)

        with VerticalGroup():
            yield Label("Part Number")
            yield ValueTypeEditor(self.section.part_number)

        with VerticalGroup():
            yield Label("Fru File ID")
            yield ValueTypeEditor(self.section.fru_file_id)
