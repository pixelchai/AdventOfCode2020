from utils import *

with open("input.txt", "r") as f:
    raw = f.read()

rules = defaultdict(list)

parse_state = 0
your_ticket = []
nearby_tickets = []
for line in raw.splitlines():
    if len(line.strip()) <= 0:
        continue

    if line in ["your ticket:", "nearby tickets:"]:
        parse_state += 1
        continue

    if parse_state == 0:
        field, lower_a, upper_a, lower_b, upper_b = re.match(r"(.+?):\s*(\d+)-(\d+)\s*or\s*(\d+)-(\d+)", line).groups()
        rules[field].extend([
            (int(lower_a), int(upper_a)),
            (int(lower_b), int(upper_b)),
        ])

    if parse_state == 1:
        your_ticket = list(map(int, line.split(",")))

    if parse_state == 2:
        nearby_tickets.append(list(map(int, line.split(","))))

def get_rules_satisfied_by(val):
    for rule, rule_ranges in rules.items():
        for lower, upper in rule_ranges:
            if lower <= val <= upper:
                yield rule

def is_valid(val):
    for rule_ranges in rules.values():
        for lower, upper in rule_ranges:
            if lower <= val <= upper:
                return True
    return False

def get_invalid_vals(ticket):
    for val in ticket:
        if not is_valid(val):
            yield val

def ticket_is_invalid(ticket):
    for _ in get_invalid_vals(ticket):
        return True
    return False

# part 1
s = 0
for ticket in nearby_tickets:
    s += sum(get_invalid_vals(ticket))
print(s)

# filter out all invalid tickets
nearby_tickets = [ticket for ticket in nearby_tickets if not ticket_is_invalid(ticket)]

pos = {}  # set of possible fields for each index. key=index, value=set(possible fields)
def collapse(pos):
    for i, p_set in pos.items():
        if len(p_set) == 1:
            for j in range(len(pos)):
                if j != i:
                    pos[j] = pos[j] - p_set
    return pos

for ticket in nearby_tickets:
    for i, val in enumerate(ticket):
        prev_set = pos.get(i, set(rules.keys()))
        new_set = prev_set & set(get_rules_satisfied_by(val))
        pos[i] = new_set
        pos = collapse(pos)

def field_to_index(field):
    # assumption: the number of possible fields for each index is exactly 1
    #             (for the fields we are interested in) therefore, search greedily
    for i, v in pos.items():
        if field in v:
            return i

# part 2
p = 1
for field in rules.keys():
    if field.startswith("departure"):
        p *= (your_ticket[field_to_index(field)])
print(p)
