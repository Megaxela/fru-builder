from tui.widgets.basic_section import BasicSection
from tui.widgets.section_ids import INTERNAL_INFO_ID


class InternalInfoSection(BasicSection):
    SECTION_ID = INTERNAL_INFO_ID

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.section_name = "Internal Info"
