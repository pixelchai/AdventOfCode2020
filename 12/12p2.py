from utils import *
import math

with open("input.txt", "r") as f:
    raw = f.read()

cur_x=0
cur_y=0
way_x=10
way_y=1
for line in raw.splitlines():
    cmd, arg = line[0], int(line[1:])
    if cmd=="F":
        off_x = (way_x - cur_x) * arg
        off_y = (way_y - cur_y) * arg

        cur_x += off_x
        cur_y += off_y

        way_x += off_x
        way_y += off_y

    if cmd in ["L", "R"]:
        alpha = math.atan2(way_y - cur_y, way_x-cur_x) \
                + math.radians(arg) * (-1 if cmd == "R" else 1)

        d = math.sqrt(math.pow(way_x-cur_x, 2) + math.pow(way_y-cur_y, 2))
        way_x = d*math.cos(alpha) + cur_x
        way_y = d*math.sin(alpha) + cur_y

    if cmd=="N":
        way_y += arg
    if cmd=="E":
        way_x += arg
    if cmd=="S":
        way_y -= arg
    if cmd=="W":
        way_x -= arg

print(abs(cur_x)+abs(cur_y))
