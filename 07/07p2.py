from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

rule_dict = {}
for line in raw.splitlines():
    pre, post = line.split("contain")
    pre_bag = pre.replace("bags", "").strip()
    if post.strip().startswith("no other"):
        rule_dict[pre_bag] = {}
    else:
        allowed_dict = {}
        for match in re.finditer(r"(\d) (\w+ \w+) bags?", post):
            count, bag_type = match.groups()
            allowed_dict[bag_type] = count
        rule_dict[pre_bag] = allowed_dict

def count_bags(bag):
    """
    count bags (including self)
    """
    a = rule_dict[bag]
    s = 1
    for k, v in a.items():
        s += count_bags(k)*int(v)
    return s

if __name__ == '__main__':
    print(count_bags("shiny gold")-1)