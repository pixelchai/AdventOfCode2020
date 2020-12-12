from utils import *
import math

with open("input.txt", "r") as f:
    raw = f.read()

cur_angle_deg=0
cur_x=0
cur_y=0
for line in raw.splitlines():
    cmd, arg = re.match(r"(\w)(\d+)", line).groups()
    if cmd=="F":
        cur_x += int(arg)*math.cos(math.radians(cur_angle_deg))
        cur_y += int(arg)*math.sin(math.radians(cur_angle_deg))
    if cmd=="L":
        cur_angle_deg+=int(arg)
    if cmd=="R":
        cur_angle_deg-=int(arg)
    if cmd=="N":
        cur_y += int(arg)
    if cmd=="E":
        cur_x += int(arg)
    if cmd=="S":
        cur_y -= int(arg)
    if cmd=="W":
        cur_x -= int(arg)

print(abs(cur_x)+abs(cur_y))