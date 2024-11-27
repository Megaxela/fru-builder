from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Label, Select, MaskedInput, Input, Static
from textual.containers import HorizontalGroup, VerticalGroup

from converter.internal.fru_data import FruData

from tui.widgets.section_editors.board_info_section_editor import BoardInfoSectionEditor


SECTION_TO_EDITOR = {
    BoardInfoSectionEditor.SECTION_ID: BoardInfoSectionEditor,
}


class EditorPlaceholder(Widget):
    DEFAULT_CSS = """
    EditorPlaceholder {
        width: 100%;
        height: 100%;
        align: center middle;
    }

    Static {
        width: auto;
    }
    """

    def __init__(self, message: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__message = message

    def compose(self) -> ComposeResult:
        yield Static(self.__message)


class UiEditor(Widget):
    DEFAULT_CSS = """
    Editor {
        height: 100%;
        dock: right;
        width: 70%;
    }

    Label {
        margin-left: 1;
    }

    VerticalGroup {
        margin-bottom: 1;
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__fru_data: FruData | None = None
        self.__section_id: str | None = None

    def compose(self) -> ComposeResult:
        if self.__fru_data is None:
            yield EditorPlaceholder("No file opened")
            return
        elif self.__section_id is None:
            yield EditorPlaceholder("No section selected")
            return
        elif self.__section_id not in SECTION_TO_EDITOR:
            yield EditorPlaceholder("Section has no editor")
            return

        yield SECTION_TO_EDITOR[self.__section_id](self.__fru_data)

    def set_fru_data(self, data: FruData | None):
        self.__fru_data = data
        self.refresh(recompose=True)

    @property
    def section_id(self):
        return self.__section_id

    @section_id.setter
    def section_id(self, v: str):
        self.__section_id = v
        self.refresh(recompose=True)

    # def compose(self):
    #     with VerticalGroup():
    #         yield Label("Language Code")
    #         yield Select(
    #             sorted(LANGUAGE_CODE_TEXT_TO_VALUE_MAP.items(), key=lambda x: x[0])
    #         )

    #     with VerticalGroup():
    #         yield Label("Manufacturing Datetime")
    #         yield MaskedInput("99-99-9999 99:99:99")

    #     with VerticalGroup():
    #         yield Label("Manufacturer")
    #         yield ValueTypeEditor()
