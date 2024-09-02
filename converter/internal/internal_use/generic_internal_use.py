import dataclasses

from converter.internal.internal_use.basic_internal_use import BasicInternalUse

YAML_NAME_DATA_KEY = "data"


@dataclasses.dataclass()
class GenericInternalUse(BasicInternalUse):
    data: bytearray

    def probe(self, data: bytes) -> bool:
        return True

    def to_binary(self, data: bytes) -> bytes:
        return bytes(self.data)

    def to_yaml(self):
        return {
            YAML_NAME_DATA_KEY: self.data.hex(),
        }

    def from_binary(self, data: bytes) -> "GenericInternalUse":
        return GenericInternalUse(data=bytearray(data))

    def from_yaml(self, data: tp.Any) -> "GenericInternalUse":
        mandatory_fields = [
            YAML_NAME_DATA_KEY,
        ]
        for field in mandatory_fields:
            if field not in data:
                raise YamlFormatError(
                    f"Generic Internal Use has no mandatory field '{field}'"
                )

        return GenericInternalUse(data=bytearray.fromhex(data[YAML_NAME_DATA_KEY]))
