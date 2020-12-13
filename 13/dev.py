from utils import *

def lcm(*nums):
  return functools.reduce(lambda n, lcm: lcm * n // math.gcd(lcm, n), nums)

print(lcm(7,13))  # = 91

for i in range(1000):
    # print(f"{i:05d} {i*7:05d} {i*13:05d}" + ("!" if (i%7==0 and i%13==0) else ""))
    print(f"{i:05d}" + ("\tD" if i%7==0 else "\t.") + ("\tD" if i%13==0 else "\t."))

# 77, 168, 259
# = lcm*0 + m, lcm*1 + m, lcm*2 + m, lcm*3 + m, ...