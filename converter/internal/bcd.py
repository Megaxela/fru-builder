import unittest

bcd_to_str_map = "0123456789 -."
str_to_bcd_map = {
    "0": 0x0,
    "1": 0x1,
    "2": 0x2,
    "3": 0x3,
    "4": 0x4,
    "5": 0x5,
    "6": 0x6,
    "7": 0x7,
    "8": 0x8,
    "9": 0x9,
    " ": 0xA,
    "-": 0xB,
    ".": 0xC,
}


def bcd_to_str(data: bytes):
    result = ""
    for byte in data:
        first_code = (byte & 0b11110000) >> 4
        second_code = (byte & 0b00001111) >> 0

        if first_code >= len(bcd_to_str_map):
            raise RuntimeError(
                f"Code {hex(first_code)} is not representable by BCD PLUS encoding"
            )
        if second_code >= len(bcd_to_str_map):
            raise RuntimeError(
                f"Code {hex(second_code)} is not representable by BCD PLUS encoding"
            )

        result += bcd_to_str_map[first_code]
        result += bcd_to_str_map[second_code]

    return result.rstrip()


def str_to_bcd(data: str):
    result = []
    for first, second in zip(data[::2], data[1::2]):
        if first not in str_to_bcd_map:
            raise RuntimeError(
                f"Symbol '{first}' is not representable by BCD PLUS encoding"
            )
        if second not in str_to_bcd_map:
            raise RuntimeError(
                f"Symbol '{second}' is not representable by BCD PLUS encoding"
            )

        result.append(str_to_bcd_map[first] << 4 | str_to_bcd_map[second])

    if len(data) % 2 != 0:
        # Met end too early. Encode last symbol as space.
        result.append(str_to_bcd_map[data[-1]] << 4 | 0xA)

    return bytes(result)


class TestBCD(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._values = {
            bytes([0b00101001]): "29",  # From spec
            bytes([0x12, 0x34]): "1234",  # Example
            bytes([0x01, 0x23, 0x45, 0x67, 0x89, 0xAB, 0xC0]): "0123456789 -.0",  # All
            bytes([0x13, 0x3A]): "133",  # Extra space at the end as padding.
        }

    def test_bcd_to_str(self):
        for k, v in self._values.items():
            self.assertEqual(v, bcd_to_str(k), v)

    def test_str_to_bcd(self):
        for k, v in self._values.items():
            self.assertEqual(k, str_to_bcd(v), k)


if __name__ == "__main__":
    unittest.main()
