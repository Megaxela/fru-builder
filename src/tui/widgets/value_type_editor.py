from textual import on
from textual.containers import HorizontalGroup
from textual.widgets import Input, Select, Label
from textual.widget import Widget
from textual.validation import ValidationResult

from converter.internal.length_type_value import LengthTypeValue, ValueType
from tui.widgets.validators.bcd_validator import BcdValidator
from tui.widgets.validators.ascii_6bit_validator import ASCII6bitValidator


class ValueTypeEditor(Widget):
    DEFAULT_CSS = """
    ValueTypeEditor {
        width: 100%;
    height: auto;
    }

    ValueTypeEditor HorizontalGroup {
        width: 100%;
    }

    ValueTypeEditor HorizontalGroup Input {
        width: 70%;
    }

    ValueTypeEditor HorizontalGroup Select {
        width: 30%;
    }

    ValueTypeEditor Label {
        color: $foreground-darken-3;
    }

    ValueTypeEditor Label.-error {
        color: $error;
    }
    """

    def __init__(self, value_type: LengthTypeValue | None = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__value = value_type
        self.__type_validators = {
            ValueType.BinaryOrUnspecified: [],
            ValueType.BCDPlus: [BcdValidator()],
            ValueType.ASCII6bit: [ASCII6bitValidator()],
            ValueType.LanguageCodeDependent: [],
        }

    def compose(self):
        with HorizontalGroup():
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
        yield Label("")

    @on(Input.Changed)
    def __on_input_changed(self, event: Input.Changed) -> None:
        if event.validation_result:
            if self.__show_error(event.validation_result):
                return

        self.__value.value = event.input.value

    def __show_error(self, result: ValidationResult | None) -> None:
        label: Label = self.query_one(Label)
        if result is not None and not result.is_valid:
            label.update("\n".join(result.failure_descriptions))
            label.add_class("-error")
            return True
        else:
            label.remove_class("-error")
            label.update("")
            return False

    @on(Select.Changed)
    def __convert_value(self, event: Select.Changed) -> None:
        input_widget: Input = self.query_one(Input)
        input_widget.validators = self.__type_validators.get(
            self.query_one(Select).value, list()
        )
        self.__show_error(input_widget.validate(input_widget.value))
