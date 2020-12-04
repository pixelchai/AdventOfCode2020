import re

with open("input.txt", "r") as f:
    raw = f.read()

fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid")
s = 0
for passport in raw.split("\n\n"):
    d = {}
    for match in re.finditer(r"("+ "|".join(fields)+ r"):([\S]+)", passport):
        k, v = match.groups()
        if k == 'byr' and not(len(v) == 4 and 1920 <= int(v) <= int(2002)):
            continue
        if k == "iyr" and not(len(v) == 4 and 2010 <= int(v) <= int(2020)):
            continue
        if k == "eyr" and not(len(v) == 4 and 2020 <= int(v) <= int(2030)):
            continue
        if k == "hgt" and not(v.endswith("cm") and 150 <= int(v[:-2]) <= 193) \
                      and not(v.endswith("in") and 59 <= int(v[:-2]) <= 76):
            continue
        if k == "hcl" and not re.fullmatch(r"#[0-9a-f]{6}", v):
            continue
        if k == "ecl" and not any([v==x for x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")]):
            continue
        if k == "pid" and not (len(v) == 9 and v.isnumeric()):
            continue

        d[k] = d.get(k, 0) + 1

    if all([x == 1 for x in d.values()]):
        if len(d) == 8 or ('cid' not in d and len(d) == 7):
            s += 1

print(s)
