from utils import *

matrix = []
with open("input.txt", "r") as f:
    for line in f:
        matrix.append(list(line.rstrip()))

def update(matrix):
    new_matrix = [row.copy() for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            seats = GridUtils(matrix).adjacents(row, col)
            if new_matrix[row][col] == "L" and all([x != "#" for x in seats]):
                new_matrix[row][col] = "#"
            elif new_matrix[row][col] == "#" and sum([x == "#" for x in seats]) >= 4:
                new_matrix[row][col] = "L"
    return new_matrix

def update_v2(matrix):
    new_matrix = [row.copy() for row in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            final_seats = []
            for ray_list in GridUtils(matrix).adjacent_rays(row, col, lambda val: val in ["#", "L"]):
                try:
                    final_seats.append(ray_list[-1])
                except IndexError:
                    pass
            if new_matrix[row][col] == "#" and sum([x == "#" for x in final_seats]) >= 5:
                new_matrix[row][col] = "L"
            if new_matrix[row][col] == "L" and all([x != "#" for x in final_seats]):
                new_matrix[row][col] = "#"
    return new_matrix

def update_until_stable(matrix, update_method):
    last_matrix = None
    while True:
        matrix = update_method(matrix)
        if last_matrix == matrix:
            break
        last_matrix = [row.copy() for row in matrix]
    return matrix

def count_occupied(matrix):
    s = []
    for row in matrix:
        s.append(sum([val == "#" for val in row]))
    return sum(s)

print(count_occupied(update_until_stable(matrix, update)))  # part one
print(count_occupied(update_until_stable(matrix, update_v2)))  # part two