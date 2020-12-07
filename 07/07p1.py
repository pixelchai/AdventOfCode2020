import re

with open("input.txt", "r") as f:
    raw = f.read()

# parse rules
rule_dict = {}
for line in raw.splitlines():
    pre, post = line.split("contain")
    pre_bag = pre.replace("bags", "").strip()

    constraint_dict = {}
    for match in re.finditer(r"(\d) (\w+ \w+) bags?", post):
        count, bag_type = match.groups()
        constraint_dict[bag_type] = int(count)
    rule_dict[pre_bag] = constraint_dict

def has_target(bag, target):
    if target in rule_dict[bag]:
        return True
    else:
        return any([has_target(k, target) for k in rule_dict[bag].keys()])

def count_bags(bag):
    """
    count bags (including self)
    """
    s = 1
    for k, v in rule_dict[bag].items():
        s += count_bags(k)*v
    return s

# part one
s = 0
for top_level_bag in rule_dict.keys():
    if has_target(top_level_bag, "shiny gold"):
        s+=1
print(s)

# part two
# -1 because considering how many OTHER bags inside shiny gold (discount self)
print(count_bags("shiny gold")-1)
