from tui.widgets.basic_section import BasicSection


class InternalInfoSection(BasicSection):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.section_name = "Internal Info"
