import pytest

from converter.internal.fru_data import FruData


@pytest.mark.parametrize(
    "input_filename",
    [
        "fru_empty.bin",
        "fru_full.bin",
        "fru_only_board_info.bin",
        "fru_only_board_info_custom_fields.bin",
        "fru_only_chassis_info.bin",
        "fru_only_chassis_info_custom_fields.bin",
        "fru_only_product_info.bin",
        "fru_only_product_info_custom_fields.bin",
    ],
)
def test_yaml_binary_yaml(static, input_filename):
    initial_value = static.read_file(input_filename, "rb")

    # 1. Binary To Internal
    internal_1 = FruData.from_binary(initial_value)

    # 2. Internal To Yaml
    yaml = internal_1.to_yaml()

    # 3. Yaml To Internal
    internal_2 = FruData.from_yaml(yaml)

    # 4. Internal To Binary
    result = internal_2.to_binary()

    assert initial_value == result
