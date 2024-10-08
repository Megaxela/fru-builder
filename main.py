import typing as tp
import argparse
import sys
import os

sys.path.append(os.path.split(__file__)[0])

from converter.internal.records.generic_record import (
    register_generic_multirecord_processors,
)
import converter.plugins
import converter.binary_converter
import converter.yaml_converter


def existing_path(path: str):
    if not os.path.exists(path):
        raise ValueError(f"'{path}' does not exists")

    return path


def parse_args(placeholder: tp.Optional[tp.Any] = None):
    args = argparse.ArgumentParser()

    args.add_argument(
        "--convert",
        type=existing_path,
        required=True,
    )
    args.add_argument("--to", type=str)

    return args.parse_args(placeholder)


def main():
    args = parse_args()
    register_generic_multirecord_processors()
    converter.plugins.load_plugins()

    binary_converter = converter.binary_converter.BinaryConverter()
    yaml_converter = converter.yaml_converter.YamlConverter()

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
    main()
