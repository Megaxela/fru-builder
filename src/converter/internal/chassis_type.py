from enum import Enum, auto


# Types from DMTC SMBIOS specification.
class ChassisType(Enum):
    Other = auto()
    Unknown = auto()
    Desktop = auto()
    LowProfileDesktop = auto()
    PizzaBox = auto()
    MiniTower = auto()
    Tower = auto()
    Portable = auto()
    Laptop = auto()
    Notebook = auto()
    HandHeld = auto()
    DockingStation = auto()
    AllInOne = auto()
    SubNotebook = auto()
    SpaceSaving = auto()
    LunchBox = auto()
    MainServerChassis = auto()
    ExpansionChassis = auto()
    SubChassis = auto()
    BusExpansionChassis = auto()
    PeripheralChassis = auto()
    RAIDChassis = auto()
    RackMountChassis = auto()
    SealedCasePC = auto()
    MultiSystemPC = auto()
    CompactPCI = auto()
    AdvancedTCA = auto()
    Blade = auto()
    BladeEnclosure = auto()
    Tabled = auto()
    Convertible = auto()
    Detachable = auto()
    IoTGateway = auto()
    EmbeddedPC = auto()
    MiniPC = auto()
    StickPC = auto()


VALUE_TO_CHASSIS_TYPE_MAP = [
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

CHASSIS_TYPE_TO_VALUE_MAP = {
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

CHASSIS_TYPE_TO_NAME_MAP = {
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

NAME_TO_CHASSIS_TYPE_MAP = {
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Other]: ChassisType.Other,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Unknown]: ChassisType.Unknown,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Desktop]: ChassisType.Desktop,
    CHASSIS_TYPE_TO_NAME_MAP[
        ChassisType.LowProfileDesktop
    ]: ChassisType.LowProfileDesktop,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.PizzaBox]: ChassisType.PizzaBox,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.MiniTower]: ChassisType.MiniTower,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Tower]: ChassisType.Tower,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Portable]: ChassisType.Portable,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Laptop]: ChassisType.Laptop,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Notebook]: ChassisType.Notebook,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.HandHeld]: ChassisType.HandHeld,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.DockingStation]: ChassisType.DockingStation,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.AllInOne]: ChassisType.AllInOne,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.SubNotebook]: ChassisType.SubNotebook,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.SpaceSaving]: ChassisType.SpaceSaving,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.LunchBox]: ChassisType.LunchBox,
    CHASSIS_TYPE_TO_NAME_MAP[
        ChassisType.MainServerChassis
    ]: ChassisType.MainServerChassis,
    CHASSIS_TYPE_TO_NAME_MAP[
        ChassisType.ExpansionChassis
    ]: ChassisType.ExpansionChassis,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.SubChassis]: ChassisType.SubChassis,
    CHASSIS_TYPE_TO_NAME_MAP[
        ChassisType.BusExpansionChassis
    ]: ChassisType.BusExpansionChassis,
    CHASSIS_TYPE_TO_NAME_MAP[
        ChassisType.PeripheralChassis
    ]: ChassisType.PeripheralChassis,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.RAIDChassis]: ChassisType.RAIDChassis,
    CHASSIS_TYPE_TO_NAME_MAP[
        ChassisType.RackMountChassis
    ]: ChassisType.RackMountChassis,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.SealedCasePC]: ChassisType.SealedCasePC,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.MultiSystemPC]: ChassisType.MultiSystemPC,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.CompactPCI]: ChassisType.CompactPCI,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.AdvancedTCA]: ChassisType.AdvancedTCA,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Blade]: ChassisType.Blade,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.BladeEnclosure]: ChassisType.BladeEnclosure,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Tabled]: ChassisType.Tabled,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Convertible]: ChassisType.Convertible,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.Detachable]: ChassisType.Detachable,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.IoTGateway]: ChassisType.IoTGateway,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.EmbeddedPC]: ChassisType.EmbeddedPC,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.MiniPC]: ChassisType.MiniPC,
    CHASSIS_TYPE_TO_NAME_MAP[ChassisType.StickPC]: ChassisType.StickPC,
}


def value_to_chassis_type(value: int) -> ChassisType:
    if value < 1 or value > len(VALUE_TO_CHASSIS_TYPE_MAP):
        return None

    return VALUE_TO_CHASSIS_TYPE_MAP[value]


def name_to_chassis_type(name: str) -> ChassisType:
    lc_name = name.lower()
    val = NAME_TO_CHASSIS_TYPE_MAP.get(lc_name)
    if val is None:
        raise ValueError(
            f"Unknown chassis type '{lc_name}'. Available values: [{', '.join(NAME_TO_CHASSIS_TYPE_MAP.keys())}]"
        )
    return val


def chassis_type_to_name(c: ChassisType) -> str:
    return CHASSIS_TYPE_TO_NAME_MAP[c]


def chassis_type_to_value(c: ChassisType) -> int:
    return CHASSIS_TYPE_TO_VALUE_MAP[c]
