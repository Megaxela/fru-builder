import typing as tp
import yaml

from .basic_converter import BasicConverter
from .internal.fru_data import FruData


class YamlConverter(BasicConverter):
    def __init__(self):
        pass

    def to_internal(self, path: str) -> FruData:
        with open(path, "rb") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return FruData.from_yaml(data)

    def from_internal(self, path: tp.Optional[str], internal_data: FruData):
        str_yaml = yaml.dump(
            internal_data.to_yaml(),
            sort_keys=False,
        )
        if path:
            with open(path, "w") as f:
                f.write(str_yaml)
        else:
            print(str_yaml)
