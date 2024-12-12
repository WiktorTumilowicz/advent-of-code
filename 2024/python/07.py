equations = []
with open("../inputs/07.txt") as file:
    for line in file:
        key, values = line.split(":")
        equations.append([int(key)] + list(map(int, values.strip().split())))


# Part 1: yay recursion
def eval1(target, current, nums):
    if len(nums) == 0:
        return current == target
    return eval1(target, current * nums[0], nums[1:]) or eval1(
        target, current + nums[0], nums[1:]
    )


total = 0
for eq in equations:
    if eval1(eq[0], eq[1], eq[2:]):
        total += eq[0]

print(total)


# Part 2
def eval2(target, current, nums):
    if len(nums) == 0:
        return current == target
    return (
        eval2(target, current * nums[0], nums[1:])
        or eval2(target, current + nums[0], nums[1:])
        or eval2(target, int(str(current) + str(nums[0])), nums[1:])
    )

total = 0
for eq in equations:
    if eval2(eq[0], eq[1], eq[2:]):
        total += eq[0]

print(total)
