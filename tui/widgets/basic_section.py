from typing import List, Tuple

from textual.app import ComposeResult
from textual.widgets import Placeholder, Static, Button
from textual.widget import Widget
from textual.reactive import reactive
from textual.pad import HorizontalPad
from textual.strip import Strip
from textual.message import Message
from rich.segment import Segment, Style
from rich.table import Table
from rich.text import Text
from textual.events import Click

from converter.internal.length_type_value import LengthTypeValue


class SectionTitle(Static):
    DEFAULT_CSS = """
    SectionTitle {
        text-style: bold;
        width: 100%;
        height: 1;
        content-align: center middle;
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BasicSection(Widget):
    class Pressed(Message):
        def __init__(self, section: "BasicSection"):
            super().__init__()
            self.section = section

    DEFAULT_CSS = """
    BasicSection {
        height: auto;
        margin: 1 1 0 1;
        padding: 0 1 0 1;

        background: $surface;
        border: none;
        border-top: tall $surface-lighten-1;
        border-bottom: tall $surface-darken-1;

        &:hover {
            border-top: tall $surface;
            background: $surface-darken-1;
        }

        &.-toggled {
            border-bottom: tall $surface;
            background: $surface-lighten-1;
        }
    }
    """

    section_name = reactive(None)
    data = reactive(None)

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.section_name = "Basic Section"

    @property
    def section_id(self):
        return self.SECTION_ID

    def set_selected(self, value: bool):
        if value:
            self.add_class("-toggled")
        else:
            self.remove_class("-toggled")

    def render(self):
        table = Table.grid(expand=True)

        table.add_row(
            Text(
                self.section_name,
                justify="center",
                style="bold",
                overflow="crop",
            )
        )

        fields = self.description_fields()
        if not fields:
            return table

        properties_table = Table.grid(expand=True)
        table.add_row(properties_table)

        for name, value in fields:
            properties_table.add_row(
                Text(
                    name,
                    justify="left",
                    style="bold",
                    overflow="crop",
                ),
                Text(
                    value,
                    justify="right",
                    style="bold",
                    overflow="crop",
                ),
            )

        return table

    def description_fields(self):
        return list()

    async def _on_click(self, event: Click) -> None:
        event.stop()
        self.post_message(BasicSection.Pressed(self))

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
