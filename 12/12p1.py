from utils import *
import math

with open("input.txt", "r") as f:
    raw = f.read()

cur_angle_deg=0
cur_x=0
cur_y=0
for line in raw.splitlines():
    cmd, arg = line[0], int(line[1:])
    if cmd=="F":
        cur_x += arg*math.cos(math.radians(cur_angle_deg))
        cur_y += arg*math.sin(math.radians(cur_angle_deg))
    if cmd=="L":
        cur_angle_deg += arg
    if cmd=="R":
        cur_angle_deg-= arg
    if cmd=="N":
        cur_y += arg
    if cmd=="E":
        cur_x += arg
    if cmd=="S":
        cur_y -= int(arg)
    if cmd=="W":
        cur_x -= arg

print(abs(cur_x)+abs(cur_y))