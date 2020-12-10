from utils import *

all_joltages = []
with open("input.txt", "r") as f:
    for line in f:
        all_joltages.append(int(line))

terminal_joltage = max(all_joltages) + 3  # built in adapter
all_joltages.append(terminal_joltage)

def find_combs():
    chains = [[0]]
    joltages = set(all_joltages.copy())

    @memoize
    def find_valid_next_adapters(chain):
        for joltage in joltages - set(chain):
            if 1 <= joltage - chain[-1] <= 3:
                yield joltage

    while len(chains) > 0:
        for i, chain in enumerate(chains):
            # tuple for memoization
            for k, adapter in enumerate(find_valid_next_adapters(tuple(chain))):
                new_iteration = chain + [adapter]

                if adapter != terminal_joltage:
                    if k == 0:
                        chains[i] = new_iteration
                    else:
                        chains.append(chain + [adapter])
                else:
                    yield chains.pop(i) + [adapter]

combs = list(find_combs())
print(len(combs))