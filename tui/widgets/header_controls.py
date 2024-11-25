from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Static
from textual.reactive import Reactive
from rich.text import Text, TextType
from textual import events


class HeaderControls(Static):
    DEFAULT_CSS = """
    HeaderControls {
        content-align: center middle;
        text-align: center;
        width: 5;
        dock: right;

        &:hover {
            background: $surface-darken-1;
        }
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__("X", *args, **kwargs)

    async def _on_click(self, event: events.Click) -> None:
        event.stop()
        # self.action_press()
