from struct import unpack_from, calcsize


class Types:
    char = 'c'
    int8 = 'b'
    uint8 = 'B'
    int16 = 'h'
    uint16 = 'H'
    int32 = 'i'
    uint32 = 'I'
    int64 = 'q'
    uint64 = 'Q'
    float = 'f'
    double = 'd'


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
    d1 = [reader.read(Types.int16) for _ in range(2)]
    d2 = [reader.read(Types.int16) for _ in range(2)]
    return dict(D1=d1, D2=d2)


def read_c(reader):
    c1 = reader.read(Types.int64)
    c2_size = reader.read(Types.uint32)
    c2_offset = reader.read(Types.uint16)
    c2_reader = reader.jump(c2_offset)
    c2_pre = [c2_reader.read(Types.char) for _ in range(c2_size)]
    c2 = b''.join(c2_pre).decode('utf-8')
    c3_size = reader.read(Types.uint16)
    c3_offset = reader.read(Types.uint32)
    c3_reader = reader.jump(c3_offset)
    c3 = [c3_reader.read(Types.double) for _ in range(c3_size)]
    return dict(C1=c1, C2=c2, C3=c3)


def read_b(reader):
    b1 = read_c(reader)
    b2 = reader.read(Types.int16)
    b3 = reader.read(Types.int64)
    b4 = reader.read(Types.double)
    b5 = reader.read(Types.float)
    b6 = reader.read(Types.uint8)
    b7 = reader.read(Types.uint64)
    b8 = reader.read(Types.double)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5, B6=b6, B7=b7, B8=b8)


def read_a(reader):
    a1 = reader.read(Types.uint8)
    a2 = reader.read(Types.uint32)  #
    a3 = reader.read(Types.float)
    a4 = read_b(reader)
    a5 = reader.read(Types.uint64)
    a6 = reader.read(Types.uint64)
    a7 = reader.read(Types.double)
    a8_size = reader.read(Types.uint32)
    a8_offset = reader.read(Types.uint32)
    a8_jump = reader.jump(a8_offset)
    a8 = [read_d(a8_jump) for _ in range(a8_size)]
    return dict(A1=a1, A2=a2, A3=a3, A4=a4, A5=a5, A6=a6, A7=a7, A8=a8)


def main(stream):
    return read_a(BinaryReader(stream, 3))
