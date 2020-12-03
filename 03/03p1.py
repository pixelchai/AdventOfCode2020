import math

with open("input.txt", "r") as f:
    grid = f.read().splitlines()
row_length = len(grid[0])

def count(vec):
    """
    :param vec: (dx, dy)
    """
    curx = 0
    cury = 0

    s = 0
    while cury < len(grid) - 1:
        curx += vec[0]
        cury += vec[1]
        if grid[cury][curx % row_length] == "#":
            s += 1
    return s

# part 1
print(count((3, 1)))

# part 2
print(math.prod(map(count, ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))))
