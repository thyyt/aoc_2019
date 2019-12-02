import readline
import numpy as np


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
        if opcode == 99:
            self.halted = True

        else:
            left_input = self.memory[self.memory[self.position + 1]]
            right_input = self.memory[self.memory[self.position + 2]]
            output_position = self.memory[self.position + 3]
            print(left_input, right_input, opcode, output_position)
            self.memory[output_position] = self.operate(left_input, right_input, opcode)
            self.position += 4

    def compute(self):
        while not self.halted:
            self.next_operation()

        print("State of the memory after halt:")
        print(self.memory)
        print(f"Position 0 after halt: {self.memory[0]}")

    def get_memory(self):
        return self.memory


def compute_first_part():
    inputs = read_inputs()
    first_computer = Computer(inputs)
    first_computer.compute()


test_computer1 = Computer([1, 0, 0, 0, 99])
test_computer1.compute()
assert test_computer1.get_memory() == [2, 0, 0, 0, 99]

test_computer2 = Computer([2, 3, 0, 3, 99])
test_computer2.compute()
assert test_computer2.get_memory() == [2, 3, 0, 6, 99]

test_computer3 = Computer([2, 4, 4, 5, 99, 0])
test_computer3.compute()
assert test_computer3.get_memory() == [2, 4, 4, 5, 99, 9801]

test_computer4 = Computer([1, 1, 1, 4, 99, 5, 6, 0, 99])
test_computer4.compute()
assert test_computer4.get_memory() == [30, 1, 1, 4, 2, 5, 6, 0, 99]

if __name__ == "__main__":
    compute_first_part()
