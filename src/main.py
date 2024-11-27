from typing import Any
from argparse import ArgumentParser, RawDescriptionHelpFormatter
from os.path import exists

from converter.internal.records.generic_record import (
    register_generic_multirecord_processors,
)
from converter.plugins import load_plugins
from converter.binary_converter import BinaryConverter
from converter.yaml_converter import YamlConverter


def existing_path(path: str):
    if not exists(path):
        raise ValueError(f"'{path}' does not exists")

    return path


def parse_args(placeholder: Any | None = None):
    epilog = "Enabled plugins:"

    plugins = list_plugins()
    if plugins:
        epilog += "\n"
        for plugin in plugins:
            epilog += f"  {plugin.__name__}\n"
    else:
        epilog += " none"

    args = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        epilog=epilog,
    )

    args.add_argument(
        "--convert",
        type=existing_path,
        required=True,
    )
    args.add_argument("--to", type=str)

    return args.parse_args(placeholder)


def main(args):
    register_generic_multirecord_processors()
    load_plugins()

    binary_converter = BinaryConverter()
    yaml_converter = YamlConverter()

    if args.convert.endswith(".yml") or args.convert.endswith(".yaml"):
        if args.to:
            print(f"Converting YAML -> BIN ({args.convert})")
        # YML -> FRU
        internal_data = yaml_converter.to_internal(args.convert)
        binary_converter.from_internal(args.to, internal_data)
    else:
        if args.to:
            print(f"Converting BIN -> YAML ({args.convert})")
        # FRU -> YML
        internal_data = binary_converter.to_internal(args.convert)
        yaml_converter.from_internal(args.to, internal_data)


if __name__ == "__main__":
    main(parse_args())
