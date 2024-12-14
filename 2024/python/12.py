from dataclasses import dataclass

grid = []
with open("../inputs/12.txt") as file:
    for line in file.readlines():
        grid.append(line.strip())

if len(grid) != len(grid[0]):
    raise Exception("I like squares")

GRID_SIZE = len(grid)


@dataclass(frozen=True)
class Pos:
    x: int
    y: int

    def __add__(self, other):
        return Pos(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Pos(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return isinstance(other, Pos) and (self.x, self.y) == (other.x, other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)

    def is_inbounds(self):
        return 0 <= self.x < GRID_SIZE and 0 <= self.y < GRID_SIZE

    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            yield self + delta


def dfs(pos):
    q = [pos]
    plant_type = grid[pos.y][pos.x]
    region = {pos}
    while q:
        plant = q.pop()
        for nb in plant.get_nbrs():
            if not nb.is_inbounds():
                continue
            if nb not in region and grid[nb.y][nb.x] == plant_type:
                region.add(nb)
                q.append(nb)
    return region


def get_perimeter(region):
    perimeter = 0
    for pos in region:
        perimeter += sum(1 for edge in pos.get_nbrs() if edge not in region)
    return perimeter


def get_sides(region):
    up_bounds = [[] for n in range(GRID_SIZE)]
    down_bounds = [[] for n in range(GRID_SIZE)]
    left_bounds = [[] for n in range(GRID_SIZE)]
    right_bounds = [[] for n in range(GRID_SIZE)]

    for pos in region:
        if Pos(pos.x - 1, pos.y) not in region:
            up_bounds[pos.x].append(pos.y)
        if Pos(pos.x + 1, pos.y) not in region:
            down_bounds[pos.x].append(pos.y)
        if Pos(pos.x, pos.y - 1) not in region:
            left_bounds[pos.y].append(pos.x)
        if Pos(pos.x, pos.y + 1) not in region:
            right_bounds[pos.y].append(pos.x)

    total = 0
    for dir in [up_bounds, down_bounds, left_bounds, right_bounds]:
        for line in dir:
            line.sort()
            prev = -2
            for point in line:
                if point - 1 != prev:
                    total += 1
                prev = point

    return total


locations = {Pos(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE)}
regions = []
while locations:
    region = dfs(locations.pop())
    regions.append(region)
    locations -= region

# Part 1
total = 0
for region in regions:
    total += get_perimeter(region) * len(region)

print(total)

# Part 2
total = 0
for region in regions:
    total += get_sides(region) * len(region)
print(total)
