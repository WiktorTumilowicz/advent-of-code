def mapchar(c):
    if c == "#":
        return -2
    if c == ".":
        return -1
    if c == "E":
        return -1
    if c == "S":
        return 0


with open("../inputs/20.txt") as file:
    grid = [[mapchar(c) for c in line] for line in file.read().strip().split("\n")]

R = len(grid)
C = len(grid[0])

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up right down left


def in_bounds(x, y):
    return 0 <= x < C and 0 <= y < R


# find start
for y in range(R):
    for x in range(C):
        if grid[y][x] == 0:
            cx, cy = x, y

# label grid
current = 0
found_next = True
while found_next:
    current += 1
    found_next = False
    for dx, dy in DIRS:
        if grid[cy + dy][cx + dx] == -1:
            cy += dy
            cx += dx
            grid[cy][cx] = current
            found_next = True
            break


def get_jumps(x, y, dist):
    neighbors = []
    for dx in range(-dist, dist + 1):
        for dy in range(-dist + abs(dx), dist - abs(dx) + 1):
            if in_bounds(x + dx, y + dy) and grid[y + dy][x + dx] != -2:
                distance = abs(dx) + abs(dy)
                neighbors.append((x + dx, y + dy, distance))
    return neighbors


def count_cheats(dist, min_cheat):
    total = 0
    for y in range(R):
        for x in range(C):
            v1 = grid[y][x]
            if v1 != -2:
                jumps = get_jumps(x, y, dist)
                for jx, jy, d in jumps:
                    v2 = grid[jy][jx]
                    if v1 - d - v2 >= min_cheat:
                        total += 1
    return total


# Part 1
print(count_cheats(2, 100))
# Part 2
print(count_cheats(20, 100))
