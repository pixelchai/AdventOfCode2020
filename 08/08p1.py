import re
from typing import Tuple

with open("input.txt", "r") as f:
    raw = f.read()

def exec_instructions(instructions) -> Tuple[bool, int]:
    """
    :return: safely terminates?, accumulator value
    """
    run_counts = [0 for _ in instructions]

    accumulator = 0
    cur_line = 0
    while True:
        try:
            op, arg = instructions[cur_line]
        except IndexError:
            return cur_line == len(instructions), accumulator

        # increment counts
        run_counts[cur_line] += 1
        if any([x > 1 for x in run_counts]):
            return False, accumulator

        # instruction handling
        if op == "jmp":
            cur_line += int(arg) - 1
        elif op == "acc":
            accumulator += int(arg)
        cur_line += 1

if __name__ == '__main__':
    # parse instructions
    raw_instructions = []
    for line in raw.splitlines():
        raw_instructions.append(re.match(r"(\w+) ([+-]\d+)", line).groups())

    # part one
    print(exec_instructions(raw_instructions)[1])

    # part two
    for i in range(len(raw_instructions)):
        if raw_instructions[i][0] == "acc":
            continue  # ignore because won't get flipped

        # construct copy of raw_instructions
        # but with instruction at line i flipped jmp <-> nop
        instructions = [
            instruction if j != i else
            ("jmp" if instruction[0] == "nop" else "nop", instruction[1])
            for j, instruction in enumerate(raw_instructions)
        ]
        terminated, value = exec_instructions(instructions)
        if terminated:
            print(value)
            break
