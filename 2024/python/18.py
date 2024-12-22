import re
import heapq


def ints(s):
    return [int(x) for x in re.findall("-?\d+", s)]


GRIDSIZE = 71
GOAL_X, GOAL_Y = 70, 70

with open("../inputs/18.txt") as file:
    corrupted = [tuple(ints(c)) for c in file.readlines()]


def in_grid(x, y):
    return 0 <= x < GRIDSIZE and 0 <= y < GRIDSIZE


def man_dist(x, y):
    return abs(GOAL_X - x) + abs(GOAL_Y - y)


DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # up right down left

# Part 1
c1024 = set(corrupted[:1024])

# A-star implementation
Q = []
heapq.heappush(Q, (0, 0, 0, 0))  # (f, g, x, y)
costs = {}
while Q:
    _, g, x, y = heapq.heappop(Q)

    # if destination end loop
    if x == GOAL_X and y == GOAL_Y:
        break

    ng = g + 1
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy

        # Check if valid tile
        if in_grid(nx, ny) and (nx, ny) not in c1024:
            if (nx, ny) not in costs or ng < costs[(nx, ny)]:
                costs[(nx, ny)] = ng
                f = ng + man_dist(nx, ny)
                heapq.heappush(Q, (f, ng, nx, ny))

print(costs[(70, 70)])

# Part 2

# I'm lazy and i just kept changing corrupted_ind
print(len(corrupted))
corrupted_ind = 3000
while (GOAL_X, GOAL_Y) in costs:
    corrupted_ind += 1
    print(f"corrupted_inx: {corrupted_ind}")
    curr_corrupted = corrupted[:corrupted_ind]
    Q = []
    heapq.heappush(Q, (0, 0, 0, 0))  # (f, g, x, y)
    costs = {}
    while Q:
        _, g, x, y = heapq.heappop(Q)

        # if destination end loop
        if x == GOAL_X and y == GOAL_Y:
            break

        ng = g + 1
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy

            # Check if valid tile
            if in_grid(nx, ny) and (nx, ny) not in curr_corrupted:
                if (nx, ny) not in costs or ng < costs[(nx, ny)]:
                    costs[(nx, ny)] = ng
                    f = ng + man_dist(nx, ny)
                    heapq.heappush(Q, (f, ng, nx, ny))
print(corrupted[corrupted_ind - 1])
