import re
import os
import time


def ints(s):
    return [int(x) for x in re.findall("-?\d+", s)]


with open("../inputs/14.txt") as file:
    robots = [ints(line) for line in file.readlines()]

WIDTH = 101
HEIGHT = 103


def update_grid(second):
    """Update the grid based on the robots' positions at the given second."""
    grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for robot in robots:
        x, y, dx, dy = robot
        x = (x + dx * second) % WIDTH
        y = (y + dy * second) % HEIGHT
        grid[y][x] += 1
    return grid


# Part 1

grid = update_grid(100)
s1, s2, s3, s4 = 0, 0, 0, 0
for line in grid[: HEIGHT >> 1]:
    s1 += sum(line[: WIDTH >> 1])
    s2 += sum(line[(WIDTH >> 1) + 1 :])

for line in grid[(HEIGHT >> 1) + 1 :]:
    s3 += sum(line[: WIDTH >> 1])
    s4 += sum(line[(WIDTH >> 1) + 1 :])

print(s1 * s2 * s3 * s4)

# Part 2


# Visualize the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(" " if x == 0 else "#" for x in row))


# Animate the grid, hopefully the tree is visible
for second in range(7000, 8000):
    grid = update_grid((second))

    os.system("clear")

    print(f"Time: {second}s")
    print_grid(grid)

    time.sleep(0.01)

tree_time = 7344
print(f"TREE TIME: {tree_time}")
grid = update_grid(tree_time)
print_grid(grid)
