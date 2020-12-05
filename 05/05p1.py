from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

def parse_line_col(line):
    return parse_line_seat(line[-3:])

def parse_line_seat(line):
    values = list(range(128))
    for c in line:
        if c=='F':
            values = values[:len(values)//2]
        elif c=='B':
            values = values[len(values)//2:]
    return values[0]

def get_id(line):
    return parse_line_seat(line)*8+parse_line_col(line)

ids=[]
for line in raw.splitlines():
    ids.append(get_id(line))

not_ins=[]
for i in range(10000000):
    if i not in ids:
        not_ins.append(i)

for a in not_ins:
    if (a+1) in ids and (a-1) in ids:
        print(a)