import enum

# Types from DMTC SMBIOS specification.
class ChassisType(enum.Enum):
    Other = enum.auto()
    Unknown = enum.auto()
    Desktop = enum.auto()
    LowProfileDesktop = enum.auto()
    PizzaBox = enum.auto()
    MiniTower = enum.auto()
    Tower = enum.auto()
    Portable = enum.auto()
    Laptop = enum.auto()
    Notebook = enum.auto()
    HandHeld = enum.auto()
    DockingStation = enum.auto()
    AllInOne = enum.auto()
    SubNotebook = enum.auto()
    SpaceSaving = enum.auto()
    LunchBox = enum.auto()
    MainServerChassis = enum.auto()
    ExpansionChassis = enum.auto()
    SubChassis = enum.auto()
    BusExpansionChassis = enum.auto()
    PeripheralChassis = enum.auto()
    RAIDChassis = enum.auto()
    RackMountChassis = enum.auto()
    SealedCasePC = enum.auto()
    MultiSystemPC = enum.auto()
    CompactPCI = enum.auto()
    AdvancedTCA = enum.auto()
    Blade = enum.auto()
    BladeEnclosure = enum.auto()
    Tabled = enum.auto()
    Convertible = enum.auto()
    Detachable = enum.auto()
    IoTGateway = enum.auto()
    EmbeddedPC = enum.auto()
    MiniPC = enum.auto()
    StickPC = enum.auto()


value_to_chassis_type_map = [
    None,
    ChassisType.Other,
    ChassisType.Unknown,
    ChassisType.Desktop,
    ChassisType.LowProfileDesktop,
    ChassisType.PizzaBox,
    ChassisType.MiniTower,
    ChassisType.Tower,
    ChassisType.Portable,
    ChassisType.Laptop,
    ChassisType.Notebook,
    ChassisType.HandHeld,
    ChassisType.DockingStation,
    ChassisType.AllInOne,
    ChassisType.SubNotebook,
    ChassisType.SpaceSaving,
    ChassisType.LunchBox,
    ChassisType.MainServerChassis,
    ChassisType.ExpansionChassis,
    ChassisType.SubChassis,
    ChassisType.BusExpansionChassis,
    ChassisType.PeripheralChassis,
    ChassisType.RAIDChassis,
    ChassisType.RackMountChassis,
    ChassisType.SealedCasePC,
    ChassisType.MultiSystemPC,
    ChassisType.CompactPCI,
    ChassisType.AdvancedTCA,
    ChassisType.Blade,
    ChassisType.BladeEnclosure,
    ChassisType.Tabled,
    ChassisType.Convertible,
    ChassisType.Detachable,
    ChassisType.IoTGateway,
    ChassisType.EmbeddedPC,
    ChassisType.MiniPC,
    ChassisType.StickPC,
]

chassis_type_to_value_map = {
    ChassisType.Other: 0x01,
    ChassisType.Unknown: 0x02,
    ChassisType.Desktop: 0x03,
    ChassisType.LowProfileDesktop: 0x04,
    ChassisType.PizzaBox: 0x05,
    ChassisType.MiniTower: 0x06,
    ChassisType.Tower: 0x07,
    ChassisType.Portable: 0x08,
    ChassisType.Laptop: 0x09,
    ChassisType.Notebook: 0x0A,
    ChassisType.HandHeld: 0x0B,
    ChassisType.DockingStation: 0x0C,
    ChassisType.AllInOne: 0x0D,
    ChassisType.SubNotebook: 0x0E,
    ChassisType.SpaceSaving: 0x0F,
    ChassisType.LunchBox: 0x10,
    ChassisType.MainServerChassis: 0x11,
    ChassisType.ExpansionChassis: 0x12,
    ChassisType.SubChassis: 0x13,
    ChassisType.BusExpansionChassis: 0x14,
    ChassisType.PeripheralChassis: 0x15,
    ChassisType.RAIDChassis: 0x16,
    ChassisType.RackMountChassis: 0x17,
    ChassisType.SealedCasePC: 0x18,
    ChassisType.MultiSystemPC: 0x19,
    ChassisType.CompactPCI: 0x1A,
    ChassisType.AdvancedTCA: 0x1B,
    ChassisType.Blade: 0x1C,
    ChassisType.BladeEnclosure: 0x1D,
    ChassisType.Tabled: 0x1E,
    ChassisType.Convertible: 0x1F,
    ChassisType.Detachable: 0x20,
    ChassisType.IoTGateway: 0x21,
    ChassisType.EmbeddedPC: 0x22,
    ChassisType.MiniPC: 0x23,
    ChassisType.StickPC: 0x24,
}

chassis_type_to_name_map = {
    ChassisType.Other: "other",
    ChassisType.Unknown: "unknown",
    ChassisType.Desktop: "desktop",
    ChassisType.LowProfileDesktop: "lowprofiledesktop",
    ChassisType.PizzaBox: "pizzabox",
    ChassisType.MiniTower: "minitower",
    ChassisType.Tower: "tower",
    ChassisType.Portable: "portable",
    ChassisType.Laptop: "laptop",
    ChassisType.Notebook: "notebook",
    ChassisType.HandHeld: "handheld",
    ChassisType.DockingStation: "dockingstation",
    ChassisType.AllInOne: "allinone",
    ChassisType.SubNotebook: "subnotebook",
    ChassisType.SpaceSaving: "spacesaving",
    ChassisType.LunchBox: "lunchbox",
    ChassisType.MainServerChassis: "mainserverchassis",
    ChassisType.ExpansionChassis: "expansionchassis",
    ChassisType.SubChassis: "subchassis",
    ChassisType.BusExpansionChassis: "busexpansionchassis",
    ChassisType.PeripheralChassis: "peripheralchassis",
    ChassisType.RAIDChassis: "raidchassis",
    ChassisType.RackMountChassis: "rackmountchassis",
    ChassisType.SealedCasePC: "sealedcasepc",
    ChassisType.MultiSystemPC: "multisystempc",
    ChassisType.CompactPCI: "compactpci",
    ChassisType.AdvancedTCA: "advancedtca",
    ChassisType.Blade: "blade",
    ChassisType.BladeEnclosure: "bladeenclosure",
    ChassisType.Tabled: "tabled",
    ChassisType.Convertible: "convertible",
    ChassisType.Detachable: "detachable",
    ChassisType.IoTGateway: "iotgateway",
    ChassisType.EmbeddedPC: "embeddedpc",
    ChassisType.MiniPC: "minipc",
    ChassisType.StickPC: "stickpc",
}

name_to_chassis_type_map = {
    "other": ChassisType.Other,
    "unknown": ChassisType.Unknown,
    "desktop": ChassisType.Desktop,
    "lowprofiledesktop": ChassisType.LowProfileDesktop,
    "pizzabox": ChassisType.PizzaBox,
    "minitower": ChassisType.MiniTower,
    "tower": ChassisType.Tower,
    "portable": ChassisType.Portable,
    "laptop": ChassisType.Laptop,
    "notebook": ChassisType.Notebook,
    "handheld": ChassisType.HandHeld,
    "dockingstation": ChassisType.DockingStation,
    "allinone": ChassisType.AllInOne,
    "subnotebook": ChassisType.SubNotebook,
    "spacesaving": ChassisType.SpaceSaving,
    "lunchbox": ChassisType.LunchBox,
    "mainserverchassis": ChassisType.MainServerChassis,
    "expansionchassis": ChassisType.ExpansionChassis,
    "subchassis": ChassisType.SubChassis,
    "busexpansionchassis": ChassisType.BusExpansionChassis,
    "peripheralchassis": ChassisType.PeripheralChassis,
    "raidchassis": ChassisType.RAIDChassis,
    "rackmountchassis": ChassisType.RackMountChassis,
    "sealedcasepc": ChassisType.SealedCasePC,
    "multisystempc": ChassisType.MultiSystemPC,
    "compactpci": ChassisType.CompactPCI,
    "advancedtca": ChassisType.AdvancedTCA,
    "blade": ChassisType.Blade,
    "bladeenclosure": ChassisType.BladeEnclosure,
    "tabled": ChassisType.Tabled,
    "convertible": ChassisType.Convertible,
    "detachable": ChassisType.Detachable,
    "iotgateway": ChassisType.IoTGateway,
    "embeddedpc": ChassisType.EmbeddedPC,
    "minipc": ChassisType.MiniPC,
    "stickpc": ChassisType.StickPC,
}


def value_to_chassis_type(value: int) -> ChassisType:
    if value < 1 or value > len(value_to_chassis_type_map):
        return None

    return value_to_chassis_type_map[value]


def name_to_chassis_type(name: str) -> ChassisType:
    val = name_to_chassis_type_map.get(name)
    if val is None:
        raise RuntimeError(
            f"Unknown chassis type '{name}'. Available values: [{', '.join(name_to_chassis_type_map.keys())}]"
        )
    return val


def chassis_type_to_name(c: ChassisType) -> str:
    return chassis_type_to_name_map[c]


def chassis_type_to_value(c: ChassisType) -> int:
    return chassis_type_to_value[c]
