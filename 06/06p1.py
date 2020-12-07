from collections import Counter

with open("input.txt", "r") as f:
    raw = f.read()

s = 0
for group in raw.split("\n\n"):
    s += len(Counter(group.replace("\n", "")))
print(s)