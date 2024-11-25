from textual.app import ComposeResult
from textual.widget import Widget
from textual.widgets import Placeholder, Header
from textual.events import Click, Mount
from textual.dom import NoScreen

from tui.widgets.header_title import HeaderTitle
from tui.widgets.header_controls import HeaderControls


class Header(Widget):
    DEFAULT_CSS = """
    Header {
        height: 1;
        dock: top;
        background: $foreground 5%;
        color: $text;
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def compose(self) -> ComposeResult:
        yield HeaderTitle()
        yield HeaderControls()

    @property
    def screen_title(self) -> str:
        """The title that this header will display.

        This depends on [`Screen.title`][textual.screen.Screen.title] and [`App.title`][textual.app.App.title].
        """
        screen_title = self.screen.title
        title = screen_title if screen_title is not None else self.app.title
        return title

    @property
    def screen_sub_title(self) -> str:
        """The sub-title that this header will display.

        This depends on [`Screen.sub_title`][textual.screen.Screen.sub_title] and [`App.sub_title`][textual.app.App.sub_title].
        """
        screen_sub_title = self.screen.sub_title
        sub_title = (
            screen_sub_title if screen_sub_title is not None else self.app.sub_title
        )
        return sub_title

    def _on_mount(self, _: Mount) -> None:
        async def set_title() -> None:
            try:
                self.query_one(HeaderTitle).text = self.screen_title
            except NoScreen:
                pass

        async def set_sub_title() -> None:
            try:
                self.query_one(HeaderTitle).sub_text = self.screen_sub_title
            except NoScreen:
                pass

        self.watch(self.app, "title", set_title)
        self.watch(self.app, "sub_title", set_sub_title)
        self.watch(self.screen, "title", set_title)
        self.watch(self.screen, "sub_title", set_sub_title)
