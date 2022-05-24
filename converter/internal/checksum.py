import typing as tp


def calculate_checksum(data: tp.Union[bytes, bytearray]):
    return (255 ^ (sum(data) & 0b1111_1111)) + 1
