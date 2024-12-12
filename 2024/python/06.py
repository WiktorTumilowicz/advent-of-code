from enum import Enum
import copy

grid = []  # 130 x 130
with open("../inputs/06.txt") as file:
    for line in file:
        grid.append(list(line.strip()))


class Dir(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


# Part 1
WIDTH = len(grid[0])
HEIGHT = len(grid)

start_x, start_y, start_direction = -1, -1, -1
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c in [d.value for d in Dir]:
            start_x = x
            start_y = y
            start_direction = Dir(c)
            grid[y][x] = "+"

start_grid = copy.deepcopy(grid)


def step_pos(x, y, direction):
    if direction == Dir.UP:
        return x, y - 1
    if direction == Dir.DOWN:
        return x, y + 1
    if direction == Dir.LEFT:
        return x - 1, y
    if direction == Dir.RIGHT:
        return x + 1, y
    raise Exception("invalid direction when stepping")


def turn(direction):
    if direction == Dir.UP:
        return Dir.RIGHT
    if direction == Dir.DOWN:
        return Dir.LEFT
    if direction == Dir.LEFT:
        return Dir.UP
    if direction == Dir.RIGHT:
        return Dir.DOWN
    raise Exception("invalid direction when turning")


x, y, direction = start_x, start_y, start_direction
while True:
    next_x, next_y = step_pos(x, y, direction)
    if next_x < 0 or next_y < 0 or next_x >= WIDTH or next_y >= HEIGHT:
        break  # guard has left, computation complete

    next_char = grid[next_y][next_x]
    if next_char in [".", "+"]:  # step
        x = next_x
        y = next_y
        grid[y][x] = "+"
    elif next_char == "#":  # turn
        direction = turn(direction)
    else:
        raise Exception("invalid character in grid")


print(sum(row.count("+") for row in grid))


# Part 2
def compute(grid_2):
    x, y, direction = start_x, start_y, start_direction
    past_turns = set()
    while True:
        next_x, next_y = step_pos(x, y, direction)
        if next_x < 0 or next_y < 0 or next_x >= WIDTH or next_y >= HEIGHT:
            return False  # guard has left, computation complete

        next_char = grid_2[next_y][next_x]
        if next_char in [".", "+"]:  # step
            x = next_x
            y = next_y
            grid_2[y][x] = "+"
        elif next_char == "#":  # turn
            if (next_x, next_y, direction) in past_turns:
                return True
            past_turns.add((next_x, next_y, direction))
            direction = turn(direction)
        else:
            raise Exception("invalid character in grid_2")


grid[start_y][start_x] = (
    "O"  # exclude start position as impossible to place object here
)
stepped_indices = [
    (x, y) for y, line in enumerate(grid) for x, c in enumerate(line) if c == "+"
]

grid_2 = copy.deepcopy(start_grid)
grid_2[start_y][start_x] = "."
total = 0
for index, (stepped_x, stepped_y) in enumerate(stepped_indices):
    # print(index) # uncomment to see progress
    grid_2[stepped_y][stepped_x] = "#"  # insert obstacle
    if compute(grid_2):
        total += 1
    grid_2[stepped_y][stepped_x] = "."  # insert obstacle

print(total)
