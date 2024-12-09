with open("../inputs/03.txt") as file:
    instructions = file.read()

# Part 1

def get_positions(instructions):
    positions = {(0, 0)}
    pos_x = 0
    pos_y = 0
    for move in instructions:
        if move == "<":
            pos_x -= 1
        if move == ">":
            pos_x += 1
        if move == "v":
            pos_y -= 1
        if move == "^":
            pos_y += 1
        positions.add((pos_x, pos_y))
    return positions
positions = get_positions(instructions)
print(len(positions))

# Part 2

santa_positions = get_positions(instructions[::2])
robo_positions = get_positions(instructions[1::2])
print(len(santa_positions.union(robo_positions)))
