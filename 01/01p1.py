# l = [
#     1721,
#     979,
#     366,
#     299,
#     675,
#     1456,
# ]
l = []
with open("input.txt", "r") as f:
    for line in f:
        l.append(int(line))

for i, x in enumerate(l):
    if x < 2020:
        for j, y in enumerate(l[i+1:]):
            if y + x == 2020:
                print("two entries: {}, {}".format(x, y))
                print("answer: {}".format(x*y))
                exit()