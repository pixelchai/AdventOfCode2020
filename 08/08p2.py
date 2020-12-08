from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

def exec_instructions(instructions):
    print(instructions)
    run_counts = []
    for i in range(len(instructions)):
        run_counts.append(0)

    accumulator = 0
    cur_line = 0
    while True:
        try:
            op, arg = instructions[cur_line]
        except IndexError:
            if cur_line == len(instructions):
                print("GOOD")
                return True
        run_counts[cur_line] += 1
        if any([x>1 for x in run_counts]):
            print("BAD!")
            return False
        if op == "jmp":
            cur_line += int(arg)
        else:
            if op == "acc":
                accumulator += int(arg)
            cur_line += 1
        print("", end="")
        print("accumulator: ", accumulator)
    # print(run_counts)

if __name__ == '__main__':
    instructions = []
    for line in raw.splitlines():
        instructions.append(re.match(r"(\w+) ([+-]\d+)", line).groups())

    for i in range(len(instructions)):
        insts = instructions.copy()
        op, arg = insts[i]
        if op == "jmp":
            insts[i] = ("nop", arg)
        elif op == "nop":
            insts[i] = ("jmp", arg)
        else:
            continue
        res = exec_instructions(insts)
        if res == True:
            exit()
    exec_instructions(instructions)