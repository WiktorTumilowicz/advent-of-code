from enum import Enum

grid = []  # 130 x 130
with open("../inputs/06.txt") as file:
    for line in file:
        grid.append(line.strip())


class Dir(Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"


# Part 1
WIDTH = len(grid[0])
HEIGHT = len(grid)

x_pos, y_pos, direction = -1, -1, -1
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c in [d.value for d in Dir]:
            x_pos = x
            y_pos = y
            direction = Dir(c)
            grid[y][x] = "+"

def step_pos(x,y,direction):
    if direction == Dir.UP:
        return x,y+1
    if direction == Dir.DOWN:
        return x,y-1
    if direction == Dir.LEFT:
        return x-1,y
    if direction == Dir.RIGHT:
        return x+1,y

def turn(direction):
    return direction???

while True:
    next_x,next_y = step_pos(x,y,direction)
    if next_x < 0 or next_y < 0 or next_x < WIDTH or next_y < HEIGHT:
        break
    next_char = grid[next_y][next_x]

    if next_char in[".", "+"]: # step
        x = next_x
        y = next_y
        grid[y][x] == "+"
    elif next_char == "#": # turn
        Dir
    else:
        exit(1)

    


print(sum(line.count("+") for line in grid))
