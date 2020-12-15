import time

with open("input.txt", "r") as f:
    raw = f.read()

starting_nums = list(map(int, raw.strip().split(",")))

d = {}
t = 0
last_spoken = 0

while True:
    if len(starting_nums) > 0:
        spoken = starting_nums.pop(0)
    elif last_spoken in d:
        spoken = t - d[last_spoken]
    else:
        spoken = 0

    d[last_spoken] = t
    t += 1
    last_spoken = spoken

    if t >= 30000000:
        print(spoken)
        break
