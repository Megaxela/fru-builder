from unittest import TestCase

ASCII_6BIT_MAP = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"


STR_TO_ASCII_6BIT_MAP = {
    " ": 0x00,
    "!": 0x01,
    '"': 0x02,
    "#": 0x03,
    "$": 0x04,
    "%": 0x05,
    "&": 0x06,
    "'": 0x07,
    "(": 0x08,
    ")": 0x09,
    "*": 0x0A,
    "+": 0x0B,
    ",": 0x0C,
    "-": 0x0D,
    ".": 0x0E,
    "/": 0x0F,
    "0": 0x10,
    "1": 0x11,
    "2": 0x12,
    "3": 0x13,
    "4": 0x14,
    "5": 0x15,
    "6": 0x16,
    "7": 0x17,
    "8": 0x18,
    "9": 0x19,
    ":": 0x1A,
    ";": 0x1B,
    "<": 0x1C,
    "=": 0x1D,
    ">": 0x1E,
    "?": 0x1F,
    "@": 0x20,
    "A": 0x21,
    "B": 0x22,
    "C": 0x23,
    "D": 0x24,
    "E": 0x25,
    "F": 0x26,
    "G": 0x27,
    "H": 0x28,
    "I": 0x29,
    "J": 0x2A,
    "K": 0x2B,
    "L": 0x2C,
    "M": 0x2D,
    "N": 0x2E,
    "O": 0x2F,
    "P": 0x30,
    "Q": 0x31,
    "R": 0x32,
    "S": 0x33,
    "T": 0x34,
    "U": 0x35,
    "V": 0x36,
    "W": 0x37,
    "X": 0x38,
    "Y": 0x39,
    "Z": 0x3A,
    "[": 0x3B,
    "\\": 0x3C,
    "]": 0x3D,
    "^": 0x3E,
    "_": 0x3F,
}


def ascii_6bit_to_str(data: bytes):
    result: str = ""

    symbols = (len(data) * 8) // 6

    for i in range(symbols):
        byte_index = (i * 6) // 8
        bit_index = (i * 6) % 8

        if bit_index <= 2:
            # Fits in one byte
            val = (data[byte_index] & (0b111111 << bit_index)) >> bit_index
        else:
            # Overlaps with next byte
            a = data[byte_index]
            b = data[byte_index + 1]

            val = ((a & (0b111111 << bit_index)) >> bit_index) | (
                (b & ((1 << (6 - (8 - bit_index))) - 1)) << (8 - bit_index)
            )

        if val >= len(ASCII_6BIT_MAP):
            raise RuntimeError(
                f"ASCII 6 bit character {hex(val)} ({bin(val)}) is out of range"
            )
        result += ASCII_6BIT_MAP[val]

    return result.rstrip()


def str_to_ascii_6bit(data: str) -> bytes:
    bitarray = []  # list of 1 & 0
    for symbol in data:
        val = STR_TO_ASCII_6BIT_MAP.get(symbol)
        if val is None:
            raise RuntimeError(
                f"Symbol '{symbol}' from '{data}' can not be represented with 6bit ASCII"
            )

        for i in range(6):
            bitarray.append(int((val & (1 << i)) != 0))

    # Appending padding if required
    if len(bitarray) % 8 != 0:
        bitarray += [0] * (8 - (len(bitarray) % 8))

    # Converting bit array to bytes
    result = []
    buff = 0
    for index, bit in enumerate(bitarray):
        if index != 0 and (index % 8) == 0:
            result.append(buff)
            buff = 0
        buff |= bit << (index % 8)

    result.append(buff)

    return bytes(result)


class Test6bitASCII(TestCase):
    def test_ascii_to_str_from_spec(self):
        self.assertEqual(ascii_6bit_to_str(bytes([0x29, 0xDC, 0xA6])), "IPMI")

    def test_str_to_ascii_from_spec(self):
        self.assertEqual(str_to_ascii_6bit("IPMI"), bytes([0x29, 0xDC, 0xA6]))

    def test_strings(self):
        strings = [
            "HELLO_WORLD",  # Simple check
            "!\"#$%&'()*+,-./0123456789:;<=>?ABCDEFGHIJKLMNOQRSTUVWXYZ[\\]^_",  # All symbols
            "LOL",  # Unaligned
            "HELLO WORLD",  # Value with space
        ]

        for s in strings:
            binary = str_to_ascii_6bit(s)
            conv = ascii_6bit_to_str(binary)
            self.assertEqual(s, conv)
