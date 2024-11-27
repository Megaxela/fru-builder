from textual import on
from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Button

from converter.internal.fru_data import FruData
from tui.widgets.sections_list import SectionsList
from tui.widgets.basic_section import BasicSection
from tui.widgets.add_section_modal import AddSectionModal


class SectionsEditor(Widget):
    DEFAULT_CSS = """
    SectionsEditor {
        width: 30%;
        dock: left;
    }

    SectionsList {
        height: 100%;
    }

    SectionsEditor Button {
        width: 100%;
        margin: 0 1 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Button("Add Section", id="add_section")
        yield SectionsList()

    def set_fru_data(self, data: FruData | None):
        self.query_one(SectionsList).set_fru_data(data)

    @on(Button.Pressed, "#add_section")
    def on_add_section(self, ev: Button.Pressed):
        self.app.push_screen(AddSectionModal(), callback=self.add_section_by_id)

    def add_section_by_id(self, section_id):
        pass
