from collections import Counter

with open("input.txt", "r") as f:
    raw = f.read()

s = 0
for group in raw.split("\n\n"):
    counts = {}
    people = group.splitlines(keepends=False)
    for person in people:
        for k,v in Counter(person).items():
            counts[k] = counts.get(k, 0) + v
    for k,v in counts.items():
        if v == len(people):
            s += 1
print(s)