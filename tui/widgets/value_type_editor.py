from textual.containers import HorizontalGroup
from textual.widgets import Input, Select

from converter.internal.length_type_value import LengthTypeValue, ValueType


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

    def __init__(self, value_type: LengthTypeValue | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__value = value_type

    def compose(self):
        yield Input(value=self.__value.value)
        yield Select(
            [
                ("Binary Or Unspecified", ValueType.BinaryOrUnspecified),
                ("BCD+", ValueType.BCDPlus),
                ("ASCII 6bit", ValueType.ASCII6bit),
                ("Language Dependent", ValueType.LanguageCodeDependent),
            ],
            prompt="No Value",
            value=self.__value.length_type.type if self.__value else None,
        )
