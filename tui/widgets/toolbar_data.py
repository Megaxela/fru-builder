import dataclasses
from typing import List

from textual.app import Binding


@dataclasses.dataclass()
class ToolbarItem:
    title: str
    action: str | None = None
    binding: Binding | None = None

    def get_action(self):
        if self.action is not None:
            return self.action
        if not self.binding:
            return None
        return self.binding.action


@dataclasses.dataclass()
class ToolbarMenu:
    title: str
    items: List[ToolbarItem]
