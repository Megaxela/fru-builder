from typing import Set
from dataclasses import dataclass

from textual import on
from textual.screen import ModalScreen
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, ListView, ListItem, Label

from tui.widgets.section_ids import (
    INTERNAL_INFO_ID,
    CHASSIS_INFO_ID,
    BOARD_INFO_ID,
    PRODUCT_INFO_ID,
)


@dataclass()
class SectionInfo:
    id: str
    name: str


DEFAULT_SECTIONS = [
    SectionInfo(id=INTERNAL_INFO_ID, name="Internal Info"),
    SectionInfo(id=CHASSIS_INFO_ID, name="Chassis Info"),
    SectionInfo(id=BOARD_INFO_ID, name="Board Info"),
    SectionInfo(id=PRODUCT_INFO_ID, name="Product Info"),
]


class Dialog(Vertical):
    pass


class InputBar(Horizontal):
    pass


class AddSectionModal(ModalScreen[str | None]):
    DEFAULT_CSS = """
    AddSectionModal {
        align: center middle;
    }

    AddSectionModal Dialog {
        width: 80%;
        height: 80%;
        border: panel $panel-lighten-2;
        background: $panel-lighten-1;
        border-title-color: $text;
        border-title-background: $panel-lighten-2;
        border-subtitle-color: $text;
        border-subtitle-background: $error;
    }

    AddSectionModal Dialog ListView {
        height: 1fr;
    }

    AddSectionModal Dialog ListView ListItem Label {
        padding: 1 1 1 1;
    }

    AddSectionModal InputBar {
        height: auto;
        align: right middle;
        padding-top: 1;
        padding-right: 1;
        padding-bottom: 1;
    }
    """

    def __init__(self, disabled_sections: Set[str] | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disabled_sections = {BOARD_INFO_ID}
        self.__disabled_sections = disabled_sections

    def compose(self):
        with Dialog() as dialog:
            dialog.border_title = "Add Section"
            with ListView():
                for default_section_info in DEFAULT_SECTIONS:
                    if (
                        self.__disabled_sections
                        and default_section_info.id in self.__disabled_sections
                    ):
                        continue
                    with ListItem():
                        yield Label(default_section_info.name)

            with InputBar():
                yield Button("Add", id="accept")
                yield Button("Cancel", id="cancel")

    @on(Button.Pressed, "#accept")
    def _on_accept(self, ev: Button.Pressed):
        pass

    @on(Button.Pressed, "#cancel")
    def _on_cancel(self, ev: Button.Pressed):
        self.dismiss()
