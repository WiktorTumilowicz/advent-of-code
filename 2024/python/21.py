from dataclasses import dataclass
from functools import cache
from itertools import permutations

with open("../inputs/21.txt") as file:
    codes = file.read().strip().split("\n")

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


NUMPAD = {
    "7": Pos(0, 0),
    "8": Pos(1, 0),
    "9": Pos(2, 0),
    "4": Pos(0, 1),
    "5": Pos(1, 1),
    "6": Pos(2, 1),
    "1": Pos(0, 2),
    "2": Pos(1, 2),
    "3": Pos(2, 2),
    "0": Pos(1, 3),
    "A": Pos(2, 3),
}
NUMPAD_COORDS = set(v for v in NUMPAD.values())

DPAD = {
    "^": Pos(1, 0),
    "A": Pos(2, 0),
    "<": Pos(0, 1),
    "v": Pos(1, 1),
    ">": Pos(2, 1),
}
DPAD_COORDS = set(v for v in DPAD.values())

DIRS = {"^": Pos(0, -1), ">": Pos(1, 0), "v": Pos(0, 1), "<": Pos(-1, 0)}


@cache
def calc(c_key, t_key, c_depth, t_depth):  # current, target
    pad, valid_coords = (NUMPAD, NUMPAD_COORDS) if c_depth == 0 else (DPAD, DPAD_COORDS)
    c_pos = pad[c_key]
    t_pos = pad[t_key]
    delta = t_pos - c_pos
    if c_depth == t_depth-1:
        return abs(delta.x) + abs(delta.y) + 1  # dist + press
    if c_key == t_key:  # just press
        return 1
    keys = []
    for x in range(abs(delta.x)):
        keys.append("<" if delta.x < 0 else ">")
    for y in range(abs(delta.y)):
        keys.append("^" if delta.y < 0 else "v")

    options = []
    for combo in set(permutations(keys)):
        pos = c_pos
        presses = 0
        for i, key in enumerate(combo):
            pos += DIRS[key]
            if pos not in valid_coords:
                break
            presses += calc("A" if i == 0 else combo[i - 1], key, c_depth + 1, t_depth)
        else:
            presses += calc(combo[-1], "A", c_depth + 1, t_depth)
            options.append(presses)

    return min(options)


for depth in [3,26]:
    total_complexity = 0
    for code in codes:
        complexity = calc("A", code[0], 0, depth)
        for i in range(1, len(code)):
            complexity += calc(code[i - 1], code[i], 0, depth)
        total_complexity += complexity * int(code[:-1])
    print(f"depth: {depth}")
    print(f"total_complexity: {total_complexity}")
