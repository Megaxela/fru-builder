from datetime import datetime

from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Input, Label
from textual import on
from textual.validation import ValidationResult
from textual.reactive import reactive

from tui.widgets.validators.datetime_validator import DateTimeValidator


class DateTimeEditor(Widget):
    DEFAULT_CSS = """
    DateTimeEditor {
        height: auto;
    }

    DateTimeEditor Label {
        color: $foreground-darken-3;
    }

    DateTimeEditor Label.-error {
        color: $error;
    }
    """

    value: datetime | None = reactive(None)

    def __init__(self, value: datetime | None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = value

    def compose(self):
        yield Input(
            self.value.strftime("%d-%m-%Y %H:%M") if self.value is not None else None,
            placeholder=datetime.now().strftime("%d-%m-%Y %H:%M"),
            validators=[
                DateTimeValidator(),
            ],
        )
        yield Label("")

    @on(Input.Changed)
    def __on_input_changed(self, event: Input.Changed) -> None:
        print(event)
        if event.validation_result:
            if self.__show_error(event.validation_result):
                return

        label: Label = self.query_one(Label)
        label.remove_class("-error")
        label.update("")

        if event.input.value:
            self.value = datetime.strptime(event.input.value, "%d-%m-%Y %H:%M")
        else:
            self.value = None

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
