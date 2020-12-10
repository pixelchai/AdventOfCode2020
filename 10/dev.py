from utils import *
raw= """
(0), 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 5, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 6, 7, 10, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 11, 12, 15, 16, 19, (22)
(0), 1, 4, 7, 10, 12, 15, 16, 19, (22)""".strip()
matrix = []
for line in raw.splitlines():
    row = []
    for num in re.findall("\d+", line):
        row.append(int(num))
    matrix.append(row)

def variants_in_col(col):
    column = []
    for row in matrix:
        column.append(row[col])
    return len(Counter(column))

for col in range(len(matrix[0])):
    print(variants_in_col(col))