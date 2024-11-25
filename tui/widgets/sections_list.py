from textual.app import ComposeResult
from textual.widgets import Placeholder
from textual.containers import VerticalScroll
from textual import on

from converter.internal.fru_data import FruData

from tui.widgets.basic_section import BasicSection
from tui.widgets.sections.internal_info_section import InternalInfoSection
from tui.widgets.sections.chassis_info_section import ChassisInfoSection
from tui.widgets.sections.product_info_section import ProductInfoSection
from tui.widgets.sections.board_info_section import BoardInfoSection


FIELD_TO_SECTION = {
    "internal_info": InternalInfoSection,
    "chassis_info": ChassisInfoSection,
    "board_info": BoardInfoSection,
    "product_info": ProductInfoSection,
    "multirecord_area": BasicSection,
}


class SectionsList(VerticalScroll):
    DEFAULT_CSS = """
    SectionsList {
        height: 100%;
        dock: left;
        width: 30%;
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__fru_data: FruData | None = None

    def compose(self) -> ComposeResult:
        if self.__fru_data is None:
            return

        for name, section_type in FIELD_TO_SECTION.items():
            section_data = getattr(self.__fru_data, name)
            if section_data is not None:
                yield section_type(data=section_data)

    def set_fru_data(self, data: FruData | None):
        self.__fru_data = data
        self.refresh(recompose=True)

    @on(BasicSection.Pressed)
    def on_section_chosen(self, message: BasicSection.Pressed):
        for child in self.query(BasicSection):
            child.set_selected(False)

        message.section.set_selected(True)
