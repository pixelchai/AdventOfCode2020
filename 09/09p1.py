from utils import *

all_nums = []
with open("input.txt", "r") as f:
    for line in f:
        all_nums.append(int(line))

def add_to(nums, target_number):
    for i, num in enumerate(nums[:-1]):
        comp = target_number - num
        if comp in nums[i+1:]:
            return num, comp
    else:
        return None

window_size = 25

def part_one():
    for i in range(len(all_nums)-window_size-1):
        window = all_nums[i:i+window_size]
        next_number = all_nums[i+window_size]
        a = add_to(window, next_number)
        if a is None:
            return next_number

def part_two(invalid_num):
    for i in range(len(all_nums)):
        for j in range(len(all_nums) - i):
            window = all_nums[i:i + j]
            if sum(window) == invalid_num:
                return min(window) + max(window)

invalid_num = part_one()
print(invalid_num)
print(part_two(invalid_num))