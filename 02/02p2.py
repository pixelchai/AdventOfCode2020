import re
with open("input.txt", "r") as f:
     raw = f.read()

s = 0
for line in raw.splitlines():
    lower, upper, c, pwd = re.search(r"(\d+)-(\d+)\s+(\w): (.+)", line).groups()
    if bool(pwd[int(lower)-1] == c) != bool(pwd[int(upper)-1] == c):
        s+=1
print(s)
