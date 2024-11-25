from textual.widget import Widget
from textual.widgets import Label, Select, MaskedInput, Input
from textual.containers import HorizontalGroup, VerticalGroup

from tui.language_code import LANGUAGE_CODE_TEXT_TO_VALUE_MAP


class ValueTypeEditor(HorizontalGroup):
    DEFAULT_CSS = """
    ValueTypeEditor {
        width: 100%;
    }

    ValueTypeEditor Input {
        width: 70%;
    }

    ValueTypeEditor Select {
        width: 30%;
    }
    """

    def compose(self):
        yield Input()
        yield Select(
            [
                ("Binary Or Unspecified", 0),
                ("BCD+", 1),
                ("ASCII 6bit", 2),
                ("Language Dependent", 3),
            ]
        )


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

    def compose(self):
        with VerticalGroup():
            yield Label("Language Code")
            yield Select(
                sorted(LANGUAGE_CODE_TEXT_TO_VALUE_MAP.items(), key=lambda x: x[0])
            )

        with VerticalGroup():
            yield Label("Manufacturing Datetime")
            yield MaskedInput("99-99-9999 99:99:99")

        with VerticalGroup():
            yield Label("Manufacturer")
            yield ValueTypeEditor()
