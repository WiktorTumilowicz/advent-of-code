with open("../inputs/16.txt") as file:
    grid = file.read().strip().split("\n")

GRID_SIZE = len(grid)
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up right down left

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c == "S":
            start_x, start_y = x, y
        if c == "E":
            end_x, end_y = x, y

queue = [(0, start_x, start_y, 1)]
costs = {}

# Part 1
while queue:
    cost, x, y, dir = queue.pop(0)
    if (x, y, dir) in costs and costs[(x, y, dir)] <= cost:
        continue
    costs[(x, y, dir)] = cost
    dx, dy = DIRS[dir]
    nx, ny = x + dx, y + dy
    if grid[ny][nx] != "#":
        queue.append((cost + 1, nx, ny, dir))
    queue.append((cost + 1000, x, y, (dir + 1) % 4))
    queue.append((cost + 1000, x, y, (dir + 3) % 4))


total = min(costs[end_x, end_y, dir] for dir in range(4))
print(total)

# Part 2
costs2 = {}
queue = [(0, end_x, end_y, dir) for dir in range(4)]
while queue:
    cost, x, y, dir = queue.pop(0)
    if (x, y, dir) in costs2 and costs2[(x, y, dir)] <= cost:
        continue
    costs2[(x, y, dir)] = cost
    dx, dy = DIRS[(dir + 2) % 4]
    nx, ny = x + dx, y + dy
    if grid[ny][nx] != "#":
        queue.append((cost + 1, nx, ny, dir))
    queue.append((cost + 1000, x, y, (dir + 1) % 4))
    queue.append((cost + 1000, x, y, (dir + 3) % 4))

places = set()
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        for dir in range(4):
            if (x, y, dir) in costs and costs[x, y, dir] + costs2[x, y, dir] == total:
                places.add((x, y))
print(len(places))

# s = ""
# for y in range(GRID_SIZE):
#    for x in range(GRID_SIZE):
#        if (x,y) in places:
#            s +="O"
#        else:
#            s += " "
#
#    s +="\n"
# print(s)
