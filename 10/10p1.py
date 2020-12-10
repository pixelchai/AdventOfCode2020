from utils import *

joltages = [0]
with open("input.txt", "r") as f:
    for line in f:
        joltages.append(int(line))

joltages = sorted(joltages)
joltages.append(max(joltages) + 3)  # built in adapter

diff_dict = defaultdict(int)
for i in range(len(joltages) - 1):
    diff_dict[joltages[i+1] - joltages[i]] += 1

print(diff_dict[1] * diff_dict[3])
