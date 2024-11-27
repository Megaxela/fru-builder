import asyncio

from typing import List

from textual.app import ComposeResult
from textual.widgets import ListView, ListItem, Label, Static
from textual.containers import HorizontalGroup
from textual.geometry import Size
from textual.screen import ModalScreen, Screen
from textual import events

from tui.widgets.toolbar_data import ToolbarItem


class Item(HorizontalGroup):
    DEFAULT_CSS = """
    Item {
        height: 1;
    }

    #name {
        dock: left;
        height: 1;
        content-align: left middle;
        text-align: left;
        width: auto;
        padding-left: 4
    }

    #binding {
        dock: right;
        content-align: right middle;
        text-align: right;
        width: auto;
    }
    """

    def __init__(self, item, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._item = item

    def compose(self):
        yield Static(self._item.title, id="name", shrink=True)
        if self._item.binding:
            yield Static(self._item.binding.key, id="binding")


class ToolbarOverlay(Screen):
    CSS = """
    ToolbarOverlay {
        background: transparent;
    }

    ToolbarOverlay ToolbarOverlayListView {
        height: 30%;
        width: 30%;
    }
    """

    def __init__(self, position=None, items=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._list_view: ToolbarOverlayListView | None = None
        self.__position = position
        self.__items = items

    def _on_overlay_result(self, result):
        print("OVERLAY RESULT")
        pass

    def compose(self):
        yield ToolbarOverlayListView()

    def _on_mount(self, event):
        self._list_view = self.query_one("ToolbarOverlayListView")
        self._list_view.offset = self.__position
        self._list_view.set_items(self.__items)

    def _on_click(self, event: events.Click):
        event.stop()
        self.dismiss()


class ToolbarOverlayListView(ListView):
    DEFAULT_CSS = """
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._items: List[ToolbarItem] = list()

    def compose(self) -> ComposeResult:
        print(f"Composing with {self._items}")
        for item in self._items:
            yield ListItem(Item(item=item))

    def set_items(self, items: List[ToolbarItem] | None):
        if items is None:
            items = list()

        self._items = items

        max_title_width = 0
        max_binding_width = 0
        for item in self._items:
            max_title_width = max(
                max_title_width,
                len(item.title),
            )

            if item.binding:
                max_binding_width = max(max_binding_width, len(item.binding.key))

        self.styles.height = max(len(items), 1)
        self.styles.width = max_title_width + max_binding_width + 6

        self.refresh(recompose=True)

    def on_list_item__child_clicked(self, item):
        self.parent.dismiss(item.item.children[0]._item)

    def action_select_cursor(self):
        self.parent.dismiss(self._items[self.index])
