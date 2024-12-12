from collections import defaultdict
from typing import Dict, List, Tuple
from itertools import combinations

grid = []  # 50 x 50
with open("../inputs/08.txt") as file:
    for line in file:
        grid.append(list(line.strip()))

GRID_HEIGHT = len(grid)
GRID_WIDTH = len(grid[0])

antennas: Dict[str, List[Tuple[int, int]]] = defaultdict(list)

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c != ".":
            antennas[c].append((x, y))


def point_in_range(point):
    return 0 <= point[0] < GRID_WIDTH and 0 <= point[1] < GRID_HEIGHT


# Part 1
antinodes = set()

for points in antennas.values():
    for pair in combinations(points, 2):
        dx, dy = pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]
        antinodes.add((pair[0][0] + dx, pair[0][1] + dy))
        antinodes.add((pair[1][0] - dx, pair[1][1] - dy))

print(sum(1 for p in antinodes if point_in_range(p)))

# Part 2
antinodes = set()

for points in antennas.values():
    antinodes.update(points)
    for pair in combinations(points, 2):
        dx, dy = pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]
        decreasing_point = (pair[0][0] + dx, pair[0][1] + dy)
        while point_in_range(decreasing_point):
            antinodes.add(decreasing_point)
            decreasing_point = (decreasing_point[0] + dx, decreasing_point[1] + dy)
        increasing_point = (pair[1][0] - dx, pair[1][1] - dy)
        while point_in_range(increasing_point):
            antinodes.add(increasing_point)
            increasing_point = (increasing_point[0] - dx, increasing_point[1] - dy)

print(len(antinodes))
