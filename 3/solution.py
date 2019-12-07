import numpy as np

LETTERS = {"height": {"U", "D"}, "width": {"L", "R"}}

NEGATIVE_DIRECTIONS = {"height": "D", "width": "L"}


def manhattan(arrya_x, arrya_y):
    distance = 0
    for x, y in zip(arrya_x, arrya_y):
        distance += abs(x - y)
    return distance


def read_inputs(input_file="input"):
    wire_instructions = []
    with open(input_file, "r") as wire_input:
        for wire in wire_input.readlines():
            wire_instructions.append(
                [instruction.replace("\n", "") for instruction in wire.split(",")]
            )
    return wire_instructions


class WireGrid:
    def __init__(self, wire_instructions):
        width_dimensions = [
            self.compute_wire_dimensions(instruction, "width")
            for instruction in wire_instructions
        ]
        height_dimensions = [
            self.compute_wire_dimensions(instruction, "height")
            for instruction in wire_instructions
        ]

        self.height, start_from_down = self.compute_dimension_range(height_dimensions)
        self.width, origin_w = self.compute_dimension_range(width_dimensions)
        self.origin = (self.height - 1 - start_from_down, origin_w)
        self.wires = []

        for instructions in wire_instructions:
            wire = self.create_wire(instructions)
            self.wires.append(wire)

    def compute_wire_dimensions(self, wire_instructions, dimension="height"):
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

    def compute_dimension_range(self, dimensions):
        low = min([dim[0] for dim in dimensions])
        high = max([dim[1] for dim in dimensions])

        size = abs(high) + abs(low) + 1

        return size, -low

    def create_wire(self, instructions):
        position_h = self.origin[0]
        position_w = self.origin[1]
        wire_location = np.zeros((self.height, self.width))
        wire_length = 0

        for instruction in instructions:
            direction = instruction[0]
            length = int(instruction[1:])
            new_array = np.arange(wire_length + 1, wire_length + length + 1)

            if direction == "U":
                wire_location[position_h - length : position_h, position_w] = new_array[
                    ::-1
                ]
                wire_length += length
                position_h -= length
            elif direction == "D":
                wire_location[
                    position_h + 1 : position_h + 1 + length, position_w
                ] = new_array
                wire_length += length
                position_h += length
            elif direction == "R":
                wire_location[
                    position_h, position_w + 1 : position_w + length + 1
                ] = new_array
                wire_length += length
                position_w += length
            elif direction == "L":
                wire_location[position_h, position_w - length : position_w] = new_array[
                    ::-1
                ]
                wire_length += length
                position_w -= length

        return wire_location

    def get_intersections(self):
        wire_sum = np.clip(a=self.wires[0], a_min=0, a_max=1) + np.clip(
            a=self.wires[1], a_min=0, a_max=1
        )
        intersections = list(zip(*np.where(wire_sum == 2)))
        return intersections

    def wire_distance(self, location):
        return (
            self.wires[0][location[0], location[1]]
            + self.wires[1][location[0], location[1]]
        )


if __name__ == "__main__":
    instructions = read_inputs()
    first_grid = WireGrid(instructions)
    intersections = first_grid.get_intersections()
    manhattan_distances = [
        manhattan(first_grid.origin, intersection) for intersection in intersections
    ]
    intersection_distances = [
        first_grid.wire_distance(intersection) for intersection in intersections
    ]
    print(f"Shortest manhattan distance from start is {min(manhattan_distances)}")
    wire_distances = [
        first_grid.wire_distance(intersection) for intersection in intersections
    ]
    print(f"Shortest wire distance to an intersection is {int(min(wire_distances))}")
