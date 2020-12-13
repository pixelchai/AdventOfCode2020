from utils import *

target_offs = []
bus_ids = []
with open("input.txt", "r") as f:
    earliest_time = int(f.readline())

    line = f.readline()
    for i, x in enumerate(line.split(",")):
        if x != "x":
            target_offs.append(i)
            bus_ids.append(int(x))

def lcm(*denominators):
    # https://stackoverflow.com/a/49816058/5013267
    return reduce(lambda a,b: a*b // math.gcd(a,b), denominators)

ts = 0
step = 1
max_valid_count = 1
while True:
    # Debug stuff:
    # for around_off in range(-20, 20):
    #     dev_ts = ts + around_off
    #     if dev_ts > 0:
    #         dev_string = "{:05d}".format(dev_ts)
    #         dev_string += "!" if dev_ts == ts else " "
    #         for bus_id in bus_ids:
    #             dev_string += "\tD" if dev_ts % bus_id == 0 else "\t."
    #         print(dev_string)
    # print("...")

    valid = []
    for i, bus_id in enumerate(bus_ids):
        if (ts+target_offs[i]) % bus_id == 0:
            valid.append(bus_id)

    valid_count = len(valid)
    if valid_count > max_valid_count:
        max_valid_count = valid_count
        step = lcm(*valid)

        if valid_count >= len(bus_ids):
            break

    ts += step

print(ts)