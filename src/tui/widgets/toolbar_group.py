from textual.widgets import Static
from textual.binding import Binding
from textual.reactive import reactive
from rich.text import Text, TextType
from rich.console import RenderableType
from typing_extensions import Self
from textual.pad import HorizontalPad
from textual import events
from typing import List

from tui.widgets.toolbar_overlay import ToolbarOverlay
from tui.widgets.toolbar_data import ToolbarItem


class ToolbarGroup(Static, can_focus=False):
    DEFAULT_CSS = """
    ToolbarGroup {
        width: auto;
        height: 1;
        text-align: left;
        content-align: left middle;

        &:disabled {
            text-opacity: 0.6;
        }

        &:focus {
            text-style: $button-focus-text-style;
            background-tint: $foreground 5%;
        }
        &:hover {
            background: $surface-darken-1;
        }

        &.-toggled {
            background: $surface;
            tint: $background 30%;
        }
    }
    """

    BINDINGS = [Binding("enter", "press", "Toggle Group", show=False)]

    label: reactive[TextType] = reactive[TextType]("")

    def __init__(
        self,
        label: TextType | None = None,
        items: List["ToolbarItem"] | None = None,
        name: str | None = None,
        id: str | None = None,
        classes: str | None = None,
        disabled: bool = False,
        tooltip: RenderableType | None = None,
    ):
        super().__init__(name=name, id=id, classes=classes, disabled=disabled)
        if label is None:
            label = self.css_identifier_styled

        self.label = label
        self.items = items

    def render(self):
        assert isinstance(self.label, Text)
        label = self.label.copy()
        label.stylize_before(self.rich_style)
        return HorizontalPad(
            renderable=label,
            left=1,
            right=1,
            pad_style=self.rich_style,
            justify=self._get_justify_method() or "center",
        )

    def validate_label(self, label: TextType) -> Text:
        """Parse markup for self.label"""
        if isinstance(label, str):
            return Text.from_markup(label)
        return label

    def action_press(self) -> None:
        """Activate a press of the button."""
        if not self.expanded:
            self.do_expand()
        else:
            self.do_unexpand()

    @property
    def expanded(self):
        return self.has_class("-toggled")

    async def _on_click(self, event: events.Click) -> None:
        event.stop()
        self.action_press()

    def do_unexpand(self) -> Self:
        if self.disabled or not self.display:
            return self

        self.remove_class("-toggled")

        return self

    def do_expand(self) -> Self:
        print(f"Expand ({self.label})")
        if self.disabled or not self.display:
            return self

        region = self.content_region
        self.app.push_screen(
            ToolbarOverlay(
                position=(region.x, region.y + region.height),
                items=self.items,
            ),
            callback=self.__on_close,
        )

        self.add_class("-toggled")

        return self

    async def __on_close(self, chosen_item: ToolbarItem | None):
        self.do_unexpand()

        if chosen_item is not None:
            await self.app.run_action(chosen_item.get_action())
