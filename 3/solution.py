import numpy as np

LETTERS = {"height": {"U", "D"}, "width": {"L", "R"}}

NEGATIVE_DIRECTIONS = {"height": "D", "width": "L"}


def read_inputs(input_file="input"):
    wire_instructions = []
    with open(input_file, "r") as wire_input:
        for wire in wire_input.readlines():
            wire_instructions.append(
                [instruction.replace("\n", "") for instruction in wire.split(",")]
            )
    return wire_instructions


def compute_wire_dimensions(wire_instructions, dimension="height"):
    position = 0
    positions = [position]
    dimension_instructions = [
        instruction
        for instruction in wire_instructions
        if instruction[0] in LETTERS[dimension]
    ]
    for instruction in dimension_instructions:
        if instruction[0] == NEGATIVE_DIRECTIONS[dimension]:
            position -= int(instruction[1:])
        else:
            position += int(instruction[1:])
        positions.append(position)

    return min(positions), max(positions)


class WireGrid:
    def __init__(self, width, height, origin):
        self.origin = origin
        self.grid = np.ndarray((height, width))


if __name__ == "__main__":
    read_inputs()
