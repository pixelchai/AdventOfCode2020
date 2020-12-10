from utils import *

all_joltages = []
with open("input.txt", "r") as f:
    for line in f:
        all_joltages.append(int(line))

final_joltage = max(all_joltages) + 3  # built in adapter
all_joltages.append(final_joltage)

# NB: this method is far less efficient when it comes to counting the number of combs
#     than the other solution. Unlike the other solution, however, it is able to
#     produce an exhaustive list of all the combinations, given enough computing power.
#     Although it works nicely for smaller inputs, due to the size of the aoc
#     puzzle input, answering the aoc question with this method is not feasible.
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

                if adapter != final_joltage:
                    if k == 0:
                        chains[i] = new_iteration
                    else:
                        chains.append(chain + [adapter])
                else:
                    yield chains.pop(i) + [adapter]

print(list(find_combs()))