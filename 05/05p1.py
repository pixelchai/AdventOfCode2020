with open("input.txt", "r") as f:
    raw = f.read()

def parse_line_col(line):
    values = list(range(8))
    for c in line[-3:]:
        if c == 'L':
            values = values[:len(values) // 2]
        elif c == 'R':
            values = values[len(values) // 2:]
    return values[0]

def parse_line_row(line):
    values = list(range(128))
    for c in line[:7]:
        if c=='F':
            values = values[:len(values) // 2]
        elif c=='B':
            values = values[len(values) // 2:]
    return values[0]

def get_id(line):
    return parse_line_row(line) * 8 + parse_line_col(line)

ids = []
for line in raw.splitlines():
    ids.append(get_id(line))

for i in range(max(ids)):
    if i not in ids:
        if (i + 1) in ids and (i - 1) in ids:
            print(i)
