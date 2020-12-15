from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

starting_nums = map(int, raw.strip().split(","))

d = defaultdict(list)
t = 1
last_spoken = 0
for i, starting_num in enumerate(starting_nums):
    t = i + 1
    d[starting_num].append(t)
    last_spoken = starting_num

while True:
    a = d[last_spoken]
    if len(a) < 2:
        spoken = 0
    else:
        spoken = a[1] - a.pop(0)
    t += 1
    # print(t, spoken)
    d[spoken].append(t)
    last_spoken = spoken

    if t >= 30000000:
        print(spoken)
        break