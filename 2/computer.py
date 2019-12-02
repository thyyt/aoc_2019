def read_inputs(input_file="input"):
    with open(input_file) as f:
        line = f.readline()
        input_integers = [int(i) for i in line.split(",")]

    return input_integers


class Computer:
    def __init__(self, inputs):
        self.inputs = inputs
        self.memory = inputs
        self.position = 0
        self.halted = False

    def reset(self):
        self.halted = False
        self.position = 0
        self.memory = self.inputs

    def insert_noun_and_verb(self, noun, verb):
        self.memory[1] = noun
        self.memory[2] = verb

    def initial_replacements(self, mappings):
        for key, value in mappings.items():
            self.memory[key] = value

    def operate(self, left, right, opcode):
        if opcode == 1:
            return left + right
        elif opcode == 2:
            return left * right

    def next_operation(self):
        opcode = self.memory[self.position]
        if opcode == 99:
            self.halted = True

        else:
            left_input = self.memory[self.memory[self.position + 1]]
            right_input = self.memory[self.memory[self.position + 2]]
            output_position = self.memory[self.position + 3]
            self.memory[output_position] = self.operate(left_input, right_input, opcode)
            self.position += 4

    def compute(self):
        while not self.halted:
            self.next_operation()

        return self.memory[0]

    def get_memory(self):
        return self.memory


def compute_first_part():
    inputs = read_inputs()
    first_computer = Computer(inputs)
    first_computer.initial_replacements({1: 12, 2: 2})
    output = first_computer.compute()
    print("State of the memory after halt:")
    print(first_computer.get_memory())
    print(f"Position 0 after halt: {output}")


def find_noun_and_verb(output=19690720):
    inputs = read_inputs()
    computer = Computer(inputs)
    for noun in range(100):
        for verb in range(100):
            computer.reset()
            old_memory = computer.get_memory()
            computer.insert_noun_and_verb(noun, verb)
            new_memory = computer.get_memory()

            print(sum([a - b for a, b in zip(old_memory, new_memory)]))
            # print(computer.get_memory())
            program_output = computer.compute()

            print(noun, verb, program_output)

            if program_output == output:
                print("Noun and verb to produce {output} are: {noun}, {verb}")
                return noun, verb


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

    find_noun_and_verb()
