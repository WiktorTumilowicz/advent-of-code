from functools import cache

with open("../inputs/19.txt") as file:
    lines = file.readlines()
    pieces = lines[0].strip().split(", ")
    designs = [line.strip() for line in lines[2:]]


@cache  # Magic python bs
def check(design):
    total = 0
    for p in pieces:
        n = len(p)
        if n > len(design):
            continue
        if design[:n] == p:
            if n == len(design):
                total += 1
            else:
                total += check(design[n:])
    return total


# Part 1
print(sum(1 for d in designs if check(d)))
# Part 2
print(sum(check(d) for d in designs))
