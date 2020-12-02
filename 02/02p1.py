from collections import Counter
import re

# raw = """
# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# """.strip()
with open("input.txt", "r") as f:
     raw = f.read()

s = 0
for line in raw.splitlines():
    lower, upper, c, pwd = re.search("(\d+)-(\d+)\s+(\w)\: (.+)", line).groups()
    valid = int(lower) <= Counter(pwd).get(c, 0) <= int(upper)
    if valid:
        s+=1
print(s)