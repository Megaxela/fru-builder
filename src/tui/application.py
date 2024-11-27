from pathlib import Path

from textual.app import App, ComposeResult
from textual.widgets import (
    Placeholder,
    OptionList,
    Label,
    Static,
    ListView,
    TabbedContent,
    TabPane,
    Button,
)
from textual.containers import Container, VerticalGroup
from textual.binding import Binding
from textual_fspicker import FileOpen, FileSave, Filters

from textual import on

from tui.widgets.toolbar import Toolbar
from tui.widgets.toolbar_data import ToolbarItem, ToolbarMenu
from tui.widgets.header import Header
from tui.widgets.sections_list import SectionsList
from tui.widgets.basic_section import BasicSection
from tui.widgets.ui_editor import UiEditor
from tui.widgets.yaml_editor import YamlEditor
from tui.widgets.sections_editor import SectionsEditor

from converter.internal.fru_data import FruData
from converter.binary_converter import BinaryConverter
from converter.yaml_converter import YamlConverter
from converter.internal.errors import FormatError, FruValidationError


class Application(App):
    CSS = """
    Screen {
        layers: below above;
    }

    #sections_group {
        height: auto;
    }
    """

    BINDINGS = [
        Binding(
            key="ctrl+n",
            action="new",
            description="Openew",
            tooltip="Create new FRU",
        ),
        Binding(
            key="ctrl+o",
            action="open",
            description="Open",
            tooltip="Open FRU binary or YAML",
        ),
        Binding(
            key="ctrl+q",
            action="quit",
            description="Quit",
            tooltip="Closes application",
        ),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__current_fru_data: FruData | None = None

        self.__yaml_converter = YamlConverter()
        self.__binary_converter = BinaryConverter()

    def compose(self) -> ComposeResult:
        with TabbedContent(initial="ui_editor_tab"):
            with TabPane("UI Editor", id="ui_editor_tab"):
                with Container():
                    yield SectionsEditor(id="sections")
                    yield UiEditor(id="editor")
            with TabPane("YAML Editor", id="yaml_editor_tab"):
                with Container():
                    yield YamlEditor(id="yaml_editor")
        yield Header(id="header")
        yield Toolbar(
            id="toolbar",
            menus=[
                ToolbarMenu(
                    title="File",
                    items=[
                        ToolbarItem(
                            title="New",
                            binding=self.BINDINGS[0],
                        ),
                        ToolbarItem(
                            title="Open",
                            binding=self.BINDINGS[1],
                        ),
                        ToolbarItem(title="Export To Binary"),
                        ToolbarItem(title="Export To Yaml"),
                        ToolbarItem(title="Quit", binding=self.BINDINGS[-1]),
                    ],
                ),
                ToolbarMenu(
                    title="Tools",
                    items=[
                        ToolbarItem(title="New"),
                    ],
                ),
            ],
        )

    @on(BasicSection.Pressed)
    def on_section_selected(self, message: BasicSection.Pressed):
        self.query_one(UiEditor).section_id = message.section.section_id

    def on_mount(self) -> None:
        self.title = "FRU Builder"

        self.__load_file(
            Path(
                "/home/megaxela/Development/Projects/Python/delta-fru-builder/examples/eeprom_simple.yaml"
            )
        )

    def action_open(self) -> None:
        self.push_screen(
            FileOpen(
                ".",
                filters=Filters(
                    ("Any", lambda _: True),
                    ("YAML", lambda p: p.suffix.lower() in {".yml", ".yaml"}),
                    ("Binary", lambda p: p.suffix.lower() in {".raw", ".bin"}),
                ),
            ),
            callback=self.__load_file,
        )

    def __load_file(self, path: Path | None) -> None:
        if path is None:
            return

        parse_result = None
        try:
            if path.suffix in {".yml", ".yaml"}:
                parse_result = self.__yaml_converter.to_internal(str(path))
            else:
                parse_result = self.__binary_converter.to_internal(str(path))
        except FormatError as e:
            self.notify(
                title="Unable to open file",
                message=str(e),
                severity="error",
            )
        except FruValidationError as e:
            self.notify(
                title="File validation failed",
                message=str(e),
                severity="error",
            )

        if parse_result is not None:
            self.sub_title = str(path)
            self.__current_fru_data = parse_result

        self.query_one(SectionsList).set_fru_data(self.__current_fru_data)
        self.query_one(UiEditor).set_fru_data(self.__current_fru_data)
