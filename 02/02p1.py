from collections import Counter
import re
with open("input.txt", "r") as f:
     raw = f.read()

s = 0
for line in raw.splitlines():
    lower, upper, c, pwd = re.search(r"(\d+)-(\d+)\s+(\w): (.+)", line).groups()
    if int(lower) <= Counter(pwd).get(c, 0) <= int(upper):
        s+=1
print(s)
