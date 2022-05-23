import typing as tp
import argparse
import sys
import os

import converter.binary_converter


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


def main(args):
    binary_converter = converter.binary_converter.BinaryConverter()

    if args.convert.endswith(".yml") or args.convert.endswith(".yaml"):
        print("Converting YAML -> BIN")
        # YML -> FRU
        pass
    else:
        print("Converting BIN -> YAML")
        # FRU -> YML
        internal_data = binary_converter.to_internal(args.convert)


if __name__ == "__main__":
    main(parse_args())
