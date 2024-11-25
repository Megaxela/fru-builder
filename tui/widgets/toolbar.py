from typing import List
import dataclasses

from textual.app import ComposeResult, Binding
from textual.containers import HorizontalGroup

from tui.widgets.toolbar_group import ToolbarGroup
from tui.widgets.toolbar_data import ToolbarMenu


class Toolbar(HorizontalGroup):
    DEFAULT_CSS = """
    Toolbar {
        height: auto;
        dock: top;
        margin: 1 0 0 0;
    }
    """

    def __init__(self, menus: List[ToolbarMenu], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._menus = menus

    def compose(self) -> ComposeResult:
        for menu in self._menus:
            yield ToolbarGroup(label=menu.title, items=menu.items)
