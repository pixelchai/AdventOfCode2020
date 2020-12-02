import re
with open("input.txt", "r") as f:
     raw = f.read()

s = 0
for line in raw.splitlines():
    lower, upper, c, pwd = re.search("(\d+)-(\d+)\s+(\w)\: (.+)", line).groups()
    valid = bool(pwd[int(lower)-1] == c) != bool(pwd[int(upper)-1] == c)
    if valid:
        s+=1
print(s)
