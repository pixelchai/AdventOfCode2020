with open("input.txt", "r") as f:
     raw = f.read()

matrix = raw.splitlines()
curx = 0
cury = 0


s = 0
while cury < len(matrix):
    curx += 3
    cury += 1
    length = len(matrix[cury])
    if matrix[cury][curx % length] == "#":
        s+=1
        print(s)