from utils import *

with open("input.txt", "r") as f:
    earliest_time = int(f.readline())
    bus_ids = [(int(x) if x != "x" else None) for x in f.readline().split(",")]
print(earliest_time)
print(bus_ids)

l=[]
for bus_id in bus_ids:
    if bus_id is None:
        l.append(1000000000000)
        continue
    a = 0
    while a < earliest_time:
        a += bus_id
    l.append(a)
print(l)
m = min(l)
print(l.index(m))
print((m - earliest_time) * bus_ids[l.index(m)])