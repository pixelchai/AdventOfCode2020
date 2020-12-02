from collections import Counter
import re

s = 0
with open("input.txt", "r") as f:
    for line in f:
        lower, upper, c, pwd = re.search(r"(\d+)-(\d+)\s+(\w): (.+)", line).groups()
        if int(lower) <= Counter(pwd).get(c, 0) <= int(upper):
            s+=1
print(s)
