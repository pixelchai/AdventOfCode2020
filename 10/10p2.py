from utils import *

joltages = []
with open("input.txt", "r") as f:
    for line in f:
        joltages.append(int(line))

final_joltage = max(joltages) + 3  # built in adapter
joltages.append(final_joltage)

@memoize
def find_num_combs(input_joltage):
    num = 0
    for joltage in joltages:
        if 1 <= joltage - input_joltage <= 3:
            if joltage == final_joltage:
                num += 1
            else:
                num += find_num_combs(joltage)
    return num

print(find_num_combs(0))
