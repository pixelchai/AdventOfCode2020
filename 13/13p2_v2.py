from utils import *

# NB: incomplete + messy code I wrote while experimenting and trying to find a solution. Kept for archiving purposes.
#     see 13p2.py for my final solution

def is_seq(input_list, alt=True):
    last=-1
    for val in input_list:
        if alt:
            if val == 0:
                return False
        if val < last:
            return False
        last = val
    return True

def just_over(n, target):
    return n*(target//n + (1 if target% n > 0 else 0))

def just_under(n, target):
    return n*(target//n)

with open("input.txt", "r") as f:
    eariest_time = int(f.readline())
    line = f.readline()
    raw_bus_ids = [(int(x) if x != "x" else None) for x in line.split(",")]
    bus_ids = [(int(x) if x != "x" else None) for x in line.split(",") if x != "x"]

target_offs=[]
none_count = 0
for i, raw_bus_id in enumerate(raw_bus_ids):
    if raw_bus_id is not None:
        target_offs.append(i)
print(target_offs)

def meets_target(input_list):
    first_val = input_list[0]
    for i, val in enumerate(input_list):
        if val != first_val+target_offs[i]:
            return False
    return True


print(bus_ids)
print()

initial_max = max(bus_ids)
initial = initial_max
j = 1
while True:
    l = [0 for i in range(len(bus_ids))]
    rem_ids = [0 if x is None else x for x in bus_ids]

    prev_max_rem = initial*j
    prev_max_rem_i = -1
    # a = 1068780 - 59 > prev_max_rem
    # print()
    while len(rem_ids) > 0:
        max_rem = max(rem_ids)
        max_rem_i = bus_ids.index(max_rem)
        rem_ids.remove(max_rem)

        if max_rem_i > prev_max_rem_i:
            l[max_rem_i] += just_over(max_rem, prev_max_rem)
        else:
            l[max_rem_i] += just_under(max_rem, prev_max_rem)

        # if is_seq(l):
        #     print(l)
        #     exit()
        if not is_seq([x for x in l if x != 0]):
            break

        prev_max_rem = l[max_rem_i]
        prev_max_rem_i = max_rem_i
        # print(l)
    # print(l)
    if meets_target(l):
        print(l)
        exit()
    j+=1