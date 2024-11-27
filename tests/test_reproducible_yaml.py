import pytest

from converter.internal.fru_data import FruData


@pytest.mark.parametrize(
    "input_filename",
    [
        "fru_empty.yaml",
        "fru_full.yaml",
        "fru_only_board_info.yaml",
        "fru_only_board_info_custom_fields.yaml",
        "fru_only_chassis_info.yaml",
        "fru_only_chassis_info_custom_fields.yaml",
        "fru_only_product_info.yaml",
        "fru_only_product_info_custom_fields.yaml",
    ],
)
def test_yaml_binary_yaml(static, input_filename):
    initial_value = static.read_yaml(input_filename)

    # 1. Yaml To Internal
    internal_1 = FruData.from_yaml(initial_value)

    # 2. Internal To Binary
    binary = internal_1.to_binary()

    # 3. Binary To Internal
    internal_2 = FruData.from_binary(binary)

    # 4. Internal To Yaml
    result = internal_2.to_yaml()

    assert initial_value == result
