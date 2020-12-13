from utils import *

with open("input.txt", "r") as f:
    eariest_time = int(f.readline())
    line = f.readline()
    raw_bus_ids = [(int(x) if x != "x" else None) for x in line.split(",")]
    bus_ids = [(int(x) if x != "x" else None) for x in line.split(",") if x != "x"]

def earliest_ts(n, target):
    return n*(target//n + (1 if target% n > 0 else 0))

def lcm(*denominators):
    # https://stackoverflow.com/a/49816058/5013267
    return reduce(lambda a,b: a*b // math.gcd(a,b), denominators)

target_offs=[]
none_count = 0
for i, raw_bus_id in enumerate(raw_bus_ids):
    if raw_bus_id is not None:
        target_offs.append(i)
print(target_offs)

ts = 0
step = 1
num_found = 0
while True:
    for around_off in range(-(num_found+1), (num_found+2)):
        dev_ts = ts + around_off
        if dev_ts > 0:
            dev_string = "{:05d}".format(dev_ts)
            dev_string += "!" if dev_ts == ts else " "
            for bus_id in bus_ids:
                dev_string += "\tD" if dev_ts % bus_id == 0 else "\t."
            print(dev_string)
    print("...")

    if ts%7 == 0 and (ts+target_offs[1])%13==0:
        print("aaaaaaaaaaaa")

    # if ts%7 == 0 and (ts+target_offs[1])%13==0 and (ts+target_offs[2])%59 ==0:
    #     print("aaaaaaaaaaaa")

    # if ts%7 == 0 and (ts+target_offs[1])%13==0 and (ts+target_offs[2])%59 ==0:
    #     print(ts)

    ts += step

    if ts > 2000:
        break