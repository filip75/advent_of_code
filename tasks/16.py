from math import prod

from aoc import *

VERSION_LENGHT = 3
TYPE_LENGTH = 3


def get_data() -> str:
    data = read_file(16)

    return "".join([f"{int(x, base=16):b}".zfill(4) for x in data])


class Packet:
    def __init__(self, bits: str) -> None:
        self.version = int(bits[:3], base=2)
        self.type_id = int(bits[3:6], base=2)

        self.length = 0
        self.literal = 0
        self.packets = []

        if self.type_id == 4:
            self._prepare_literal(bits)
        else:
            self._prepare_control(bits)

    def _prepare_literal(self, bits: str) -> None:
        s = ""
        pointer = VERSION_LENGHT + TYPE_LENGTH

        while True:
            s += bits[pointer + 1 : pointer + 1 + 4]
            if bits[pointer] == "0":
                break
            pointer += 5

        self.literal = int(s, base=2)
        self.length = pointer + 5

    def _prepare_control(self, bits: str) -> None:
        packet_length = VERSION_LENGHT + TYPE_LENGTH + 1
        length_type = bits[6]

        if length_type == "0":
            packet_length += 15
            length = int(bits[7 : 7 + 15], base=2)
            pointer = VERSION_LENGHT + TYPE_LENGTH + 1 + 15
            while pointer < 7 + 15 + length:
                self.packets.append(Packet(bits[pointer:]))
                pointer += len(self.packets[-1])
                packet_length += len(self.packets[-1])

        elif length_type == "1":
            packet_length += 11
            length = int(bits[7 : 7 + 11], base=2)
            pointer = VERSION_LENGHT + TYPE_LENGTH + 1 + 11
            for _ in range(length):
                self.packets.append(Packet(bits[pointer:]))
                pointer += len(self.packets[-1])
                packet_length += len(self.packets[-1])

        self.length = packet_length

    def evaluate(self) -> int:
        values = [p.evaluate() for p in self.packets]
        print(values, self.type_id)
        if self.type_id == 0:
            return sum(values)
        elif self.type_id == 1:
            return prod(values)
        elif self.type_id == 2:
            return min(values)
        elif self.type_id == 3:
            return max(values)
        elif self.type_id == 4:
            return self.literal
        elif self.type_id == 5:
            return 1 if values[0] > values[1] else 0
        elif self.type_id == 6:
            return 1 if values[0] < values[1] else 0
        elif self.type_id == 7:
            return 1 if values[0] == values[1] else 0

    def get_version(self) -> int:
        return self.version + sum((packet.get_version() for packet in self.packets))

    def __len__(self) -> int:
        return self.length


def first() -> int:
    data = get_data()
    return Packet(data).get_version()


def second() -> int:
    data = get_data()
    return Packet(data).evaluate()
