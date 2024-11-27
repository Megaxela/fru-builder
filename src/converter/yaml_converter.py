from yaml import load, dump, FullLoader

from converter.basic_converter import BasicConverter
from converter.internal.fru_data import FruData
from converter.internal.errors import YamlFormatError


class YamlConverter(BasicConverter):
    def __init__(self):
        pass

    def to_internal(self, path: str) -> FruData:
        with open(path, "rb") as f:
            data = load(f, Loader=FullLoader)

        if data is None:
            raise YamlFormatError(f"Provided file is empty")

        return FruData.from_yaml(data)

    def from_internal(self, path: str | None, internal_data: FruData):
        str_yaml = dump(internal_data.to_yaml(), sort_keys=False)
        if path:
            with open(path, "w") as f:
                f.write(str_yaml)
        else:
            print(str_yaml)
