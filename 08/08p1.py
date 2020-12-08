from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

instructions = []
for line in raw.splitlines():
    instructions.append(re.match(r"(\w+) ([+-]\d+)", line).groups())

run_counts = []
for i in range(len(instructions)):
    run_counts.append(0)

accumulator = 0
cur_line = 0
while True:
    op, arg = instructions[cur_line]
    run_counts[cur_line] += 1
    if any([x>1 for x in run_counts]):
        break
    if op == "jmp":
        cur_line += int(arg)
    else:
        if op == "acc":
            accumulator += int(arg)
        cur_line += 1
print(accumulator)
print(run_counts)