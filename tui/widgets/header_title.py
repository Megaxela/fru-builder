from textual.widget import Widget
from textual.reactive import Reactive
from rich.text import Text, TextType


class HeaderTitle(Widget):
    """Display the title / subtitle in the header."""

    DEFAULT_CSS = """
    HeaderTitle {
        content-align: center middle;
        width: 100%;
    }
    """

    text: Reactive[str] = Reactive("")
    """The main title text."""

    sub_text = Reactive("")
    """The sub-title text."""

    def render(self):
        """Render the title and sub-title.

        Returns:
            The value to render.
        """
        text = Text(self.text, no_wrap=True, overflow="ellipsis")
        if self.sub_text:
            text.append(" — ")
            text.append(self.sub_text, "dim")
        return text
