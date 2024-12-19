from dataclasses import dataclass
import copy
#import os
#import time
from enum import Enum


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
        return 0 <= self.x < GRID_WIDTH and 0 <= self.y < GRID_HEIGHT

    def get_nbrs(self):
        for delta in (Pos(0, 1), Pos(0, -1), Pos(1, 0), Pos(-1, 0)):
            yield self + delta


class Cell(Enum):
    ROBOT = "@"
    WALL = "#"
    EMPTY = "."
    LEFT = "["
    RIGHT = "]"


with open("../inputs/15.txt") as file:
    input = file.read()
    grid_str, moves = input.split("\n\n")
    moves = moves.replace("\n", "")
    grid_str = grid_str.replace(".", "..")
    grid_str = grid_str.replace("@", "@.")
    grid_str = grid_str.replace("O", "[]")
    grid_str = grid_str.replace("#", "##")
    grid_split = grid_str.split()
    grid = {
        Pos(x, y): Cell(char)
        for y, line in enumerate(grid_split)
        for x, char in enumerate(line)
    }
grid_cp = copy.deepcopy(grid)

GRID_WIDTH = len(grid_split[0])
GRID_HEIGHT = len(grid_split)
robot_pos = next((pos for pos, cell in grid.items() if cell == Cell.ROBOT))


def get_dir(dir) -> Pos:
    if dir == "<":
        return Pos(-1, 0)
    if dir == ">":
        return Pos(1, 0)
    if dir == "^":
        return Pos(0, -1)
    if dir == "v":
        return Pos(0, 1)
    raise Exception(f"unknown direction: '{dir}'")


def print_grid():
    print()
    for y in range(GRID_HEIGHT):
        row = ""
        for x in range(GRID_WIDTH):
            cell = grid.get(Pos(x, y))
            row += " " if cell == Cell.EMPTY else cell.value
        print(row)


# Part 1
def move_robot1(move_dir, robot_pos):
    if move_dir.y == 0:
        move_dir = move_dir + move_dir

    final_pos = robot_pos + move_dir
    while grid[final_pos] == Cell.LEFT:
        final_pos = final_pos + move_dir

    if grid[final_pos] == Cell.WALL:
        return robot_pos
    elif grid[final_pos] == Cell.EMPTY:
        new_pos = robot_pos + move_dir
        grid[robot_pos] = Cell.EMPTY
        grid[robot_pos + Pos(1, 0)] = Cell.EMPTY
        grid[final_pos] = Cell.LEFT
        grid[final_pos + Pos(1, 0)] = Cell.RIGHT
        grid[new_pos] = Cell.ROBOT
        grid[new_pos + Pos(1, 0)] = Cell.EMPTY
        return new_pos
    raise Exception("invalid move")


for move in moves:
    dir = get_dir(move)
    robot_pos = move_robot1(dir, robot_pos)

print_grid()

total = 0
for pos, cell in grid.items():
    if cell == Cell.LEFT:
        total += pos.x // 2 + pos.y * 100

print(total)


# Part 2
grid = grid_cp
robot_pos = next((pos for pos, cell in grid.items() if cell == Cell.ROBOT))


def move_robot2(move_dir, robot_pos):
    pos_to_move = [robot_pos]
    pos_to_check = [robot_pos + move_dir]
    hit_wall = False

    while pos_to_check:
        next_check = []
        for pos1 in pos_to_check:
            pos2 = pos1
            cell = grid[pos1]
            if cell == Cell.WALL:
                hit_wall = True
                next_check.clear()
                break
            elif cell == Cell.EMPTY:
                continue
            elif cell == Cell.LEFT:
                pos2 += Pos(1, 0)
            else:
                pos2 += Pos(-1, 0)
            for pos in [pos1, pos2]:
                if pos not in pos_to_move:
                    pos_to_move.append(pos)
                next_pos = pos + move_dir
                if not (grid[pos] == Cell.RIGHT and grid[next_pos] == Cell.RIGHT):
                    if next_pos not in next_check:
                        next_check.append(next_pos)
            if move_dir.y == 0:  # prevent recursion in horizontal case
                next_check.pop(0)
        pos_to_check = next_check

    if hit_wall:
        return robot_pos
    else:
        for cell in reversed(pos_to_move):
            grid[cell + move_dir] = grid[cell]
            grid[cell] = Cell.EMPTY
        return robot_pos + move_dir


for move in moves:
    dir = get_dir(move)
    robot_pos = move_robot2(dir, robot_pos)
    # os.system("clear")
    # print_grid()
    # time.sleep(0.1)

print_grid()

total = 0
for pos, cell in grid.items():
    if cell == Cell.LEFT:
        total += pos.x + pos.y * 100

print(total)
