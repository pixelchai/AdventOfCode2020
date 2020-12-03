import re
import math
from collections import Counter

with open("input.txt", "r") as f:
     raw = f.read()

matrix = raw.splitlines(keepends=False)

def f():
    try:
        curx = 0
        cury = 0

        s = 0
        while cury < len(matrix):
            curx += 1
            cury += 2
            length = len(matrix[cury])
            if matrix[cury][curx % length] == "#":
                s+=1
                print(s)
    except:
        return s

print(f())