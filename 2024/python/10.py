grid = []
with open("../inputs/10.txt") as file:
    for line in file.readlines():
        grid.append([int(x) for x in line.strip()])

if len(grid) != len(grid[0]):
    raise Exception("I like squares")

GRID_SIZE = len(grid)


def in_range(value):
    return 0 <= value < GRID_SIZE


# Part 1
def count_paths1(x, y, index):
    if not (in_range(x) and in_range(y)):
        return set()
    if grid[y][x] != index:
        return set()

    if index == 9:
        return {(x, y)}

    index += 1
    paths = set()
    paths |= count_paths1(x - 1, y, index)
    paths |= count_paths1(x + 1, y, index)
    paths |= count_paths1(x, y - 1, index)
    paths |= count_paths1(x, y + 1, index)

    return paths


total = 0
for y, row in enumerate(grid):
    for x, num in enumerate(row):
        if num == 0:
            total += len(count_paths1(x, y, num))

print(total)


# Part 2
def count_paths1(x, y, index):
    if not (in_range(x) and in_range(y)):
        return 0
    if grid[y][x] != index:
        return 0

    if index == 9:
        return 1

    index += 1
    return sum([
        count_paths1(x - 1, y, index),
        count_paths1(x + 1, y, index),
        count_paths1(x, y - 1, index),
        count_paths1(x, y + 1, index),
    ])


total = 0
for y, row in enumerate(grid):
    for x, num in enumerate(row):
        if num == 0:
            total += count_paths1(x, y, num)

print(total)
