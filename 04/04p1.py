from utils import *

# TERRIBLE RUSHED CODE I PANICKED A BIT!!!
with open("input.txt", "r") as f:
    raw = f.read()

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
s = 0
passports = raw.split("\n\n")
for passport in passports:
    d = {}
    for match in re.finditer("("+ "|".join(fields)+ "):([\S]+)", passport):
        k,v=match.groups()
        if k == 'byr':
            if len(v) == 4 and 1920 <= int(v) <= int(2002):
                pass
            else:
                continue
        if k == "iyr":
            if len(v) == 4 and 2010 <= int(v) <= int(2020):
                pass
            else:
                continue
        if k == "eyr":
            if len(v) == 4 and 2020 <= int(v) <= int(2030):
                pass
            else:
                continue
        if k == "hgt":
            val = int(v.replace("cm", "").replace("in",""))
            if v.endswith("cm") and 150 <= val <= 193:
                pass
            elif v.endswith("in") and 59 <= val <= 76:
                pass
            else:
                continue
        if k == "hcl":
            if v[0] != '#': continue
            if not re.match("#[0-9a-f]{6}", v):
                continue
        if k == "ecl":
            if not any([v==x for x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]]):
                continue
        if k == "pid":
            if not len(v) == 9:
                continue
        if k == "cid":
            pass


        d[k] = d.get(k, 0) + 1

    if len(d) == 8:
        if all([x == 1 for x in d.values()]):
            print(d)
            s+=1
    elif len(d) == 7:
        if 'cid' not in d:
            if all([x == 1 for x in d.values()]):
                print(d)
                s += 1

print(s)