from struct import unpack_from, calcsize
from typing import Any, Callable


class Types:
    char = "c"
    int8 = "b"
    uint8 = "B"
    int16 = "h"
    uint16 = "H"
    int32 = "i"
    uint32 = "I"
    int64 = "q"
    uint64 = "Q"
    float = "f"
    double = "d"


class BinaryReader:
    def __init__(self, stream, offset, order=">"):
        self.stream = stream
        self.offset = offset
        self.order = order

    def jump(self, offset):
        reader = BinaryReader(self.stream, offset, self.order)
        return reader

    def read(self, pattern):
        size = calcsize(pattern)
        data = unpack_from(self.order + pattern, self.stream, self.offset)
        self.offset += size
        return data[0]


def read_d(reader):
    d1 = reader.read(Types.int8)  #
    d2 = reader.read(Types.uint32)  #
    d3 = reader.read(Types.int16)  #
    d4 = reader.read(Types.int8)  #
    return dict(D1=d1, D2=d2, D3=d3, D4=d4)


def read_c(reader):
    c1 = reader.read(Types.uint32)  #
    c2 = reader.read(Types.uint64)  #
    c3 = reader.read(Types.int8)  #
    c4 = reader.read(Types.int32)  #
    c5 = [reader.read(Types.uint8) for _ in range(2)]  #
    return dict(C1=c1, C2=c2, C3=c3, C4=c4, C5=c5)


def read_b(reader):
    b1 = read_c(reader)  #
    b2 = reader.read(Types.float)  #
    return dict(B1=b1, B2=b2)


def read_a(reader):
    a1 = [reader.read(Types.uint8) for _ in range(2)]  #

    a2_offset = reader.read(Types.uint16)  #
    a2_reader = reader.jump(a2_offset)
    a2 = read_b(a2_reader)

    a3_size = reader.read(Types.uint16)
    a3_offset = reader.read(Types.uint16)
    a3_reader = reader.jump(a3_offset)
    a3 = [read_d(a3_reader) for _ in range(a3_size)]

    a4 = reader.read(Types.float)  #
    a5 = reader.read(Types.uint32)  #
    a6 = [reader.read(Types.uint8) for _ in range(5)]  #
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6)


def main(stream):
    return read_a(BinaryReader(stream, 4))
