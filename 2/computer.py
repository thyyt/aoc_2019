import readline
import numpy as np


OPCODE_MAPPING = {1: np.sum, 2: np.multiply, 99: "halt"}


def read_inputs(input_file="input"):
    with open(input_file) as f:
        line = f.readline()
        input_integers = [int(i) for i in line.split(",")]

    return input_integers


class Computer:
    def __init__(self, inputs):
        self.memory = inputs
        self.position = 0
        self.halted = False

    def operate(self, left, right, opcode):
        if opcode == 1:
            return left + right
        else:
            return left * right

    def next_operation(self):
        opcode = self.memory[self.position]
        if OPCODE_MAPPING[opcode] == "halt":
            self.halted = True

        else:
            left_input = self.memory[self.memory[self.position + 1]]
            right_input = self.memory[self.memory[self.position + 2]]
            self.memory[self.position + 3] = self.operate(
                left_input, right_input, opcode
            )
            self.position += 4

    def compute(self):
        while not self.halted:
            self.next_operation()

        print("State of the memory after halt:")
        print(self.memory)
        print(f"Position 0 after halt: {self.memory[0]}")


def compute_first_part():
    inputs = read_inputs()
    first_computer = Computer(inputs)
    first_computer.compute()


if __name__ == "__main__":
    compute_first_part()
