# l = [
#     1721,
#     979,
#     366,
#     299,
#     675,
#     1456,
# ]
l=[]
with open("input.txt", "r") as f:
    for line in f:
        l.append(int(line))
print(len(l))

for i, x in enumerate(l):
    if x < 2020:
        for j, y in enumerate(l):
            if y < 2020 - x:
                for k, z in enumerate(l):
                    if x+y+z == 2020:
                        print(x, y, z)
                        print(x*y*z)
