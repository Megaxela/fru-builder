from typing import List, Tuple

from textual.app import ComposeResult
from textual.widgets import Placeholder, Static, Button
from textual.widget import Widget
from textual.reactive import reactive
from textual.pad import HorizontalPad
from textual.strip import Strip
from textual.message import Message
from rich.segment import Segment, Style
from rich.console import Console
from rich.table import Table
from rich.text import Text
from textual.events import Click

from converter.internal.length_type_value import LengthTypeValue
from converter.internal.fru_data import FruData


class BasicSectionEditor(Widget):
    DEFAULT_CSS = """
    BasicSection {
        width: 100%;
        height: 100%;
    }
    """

    section_name = reactive(None)
    data = reactive(None)

    def __init__(self, fru_data: FruData | None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__fru_data: FruData | None = fru_data
        self.section_name = "Basic Section"

    @staticmethod
    def _ltvalue_description(length_type: LengthTypeValue):
        if isinstance(length_type.value, bytes):
            return length_type.value.hex(" ")
        return length_type.value

    @staticmethod
    def _add_ltvalue_to_fields(
        fields: List[Tuple[str, str]],
        field_name: str,
        ltvalue: LengthTypeValue,
    ):
        if ltvalue.value is not None:
            fields.append((field_name, BasicSection._ltvalue_description(ltvalue)))

    @property
    def section(self):
        # todo: use section query here
        return getattr(self.__fru_data, self.SECTION_ID)
