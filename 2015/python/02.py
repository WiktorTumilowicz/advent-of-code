input = []
with open("../inputs/2.txt") as file:
    input = file.readlines()

# Part 1

total = 0
for box in input:
    l, w, h = map(int, box.split("x"))
    sides = [l * w, w * h, h * l]
    total += min(sides) + sum(sides) * 2
print(total)

# Part 2
total = 0
for box in input:
    l, w, h = map(int, box.split("x"))
    perimeters = [l + w, w + h, h + l]
    total += min(perimeters) * 2 + l * w * h
print(total)
