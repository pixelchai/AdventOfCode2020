from utils import *

all_joltages = []
with open("input.txt", "r") as f:
    for line in f:
        all_joltages.append(int(line))

all_joltages = sorted(all_joltages)
all_joltages.append(max(all_joltages) + 3)  # built in adapter

joltages = all_joltages.copy()
def find_valid_adapter(input_joltage):
    for i, joltage in enumerate(joltages):
        if 1 <= joltage - input_joltage <= 3:
            return joltages.pop(i)

def adapter_chain_differences():
    prev_outlet_joltage = 0
    outlet_joltage = 0
    while len(joltages) > 0:
        outlet_joltage = find_valid_adapter(outlet_joltage)
        yield outlet_joltage - prev_outlet_joltage
        prev_outlet_joltage = outlet_joltage

diffs_counter = Counter(adapter_chain_differences())
print(diffs_counter.get(1, 0) * diffs_counter.get(3, 0))