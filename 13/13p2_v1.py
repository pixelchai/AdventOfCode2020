from utils import *

with open("input.txt", "r") as f:
    eariest_time = int(f.readline())
    bus_ids = [(int(x) if x != "x" else None) for x in f.readline().split(",")]

def earliest_ts(n, target):
    return n*(target//n + (1 if target% n > 0 else 0))

ts = 1068780
while True:
    boo_flag = False
    for i, bus_id in enumerate(bus_ids):
        if bus_id is None:
            continue
        if (ts+i)%bus_id != 0:
            boo_flag = True
            break
    else:
        print(ts)
    ts += 1
    if boo_flag:
        continue
