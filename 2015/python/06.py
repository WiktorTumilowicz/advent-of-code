import numpy as np
import re

with open("../inputs/06.txt") as file:
    instructions = file.readlines()

# Part 1


def on(lights, rect):
    lights[rect[0] : rect[2] + 1, rect[1] : rect[3] + 1] = True


def off(lights, rect):
    lights[rect[0] : rect[2] + 1, rect[1] : rect[3] + 1] = False


def toggle(lights, rect):
    lights[rect[0] : rect[2] + 1, rect[1] : rect[3] + 1] ^= True


lights = np.zeros((1000, 1000), dtype=bool)

search = r"(\d+),(\d+) through (\d+),(\d+)"
for instruction in instructions:
    rect = list(map(int, re.search(search, instruction).groups()))
    if "on" in instruction:
        on(lights, rect)
    if "off" in instruction:
        off(lights, rect)
    if "toggle" in instruction:
        toggle(lights, rect)

print(lights.sum())

# def visualize_lights(lights):
#    for row in lights[::10]:
#        print("".join("#" if cell else "." for cell in row[::4]))
# visualize_lights(lights)

# Part 2


def on2(lights, rect):
    lights[rect[0] : rect[2] + 1, rect[1] : rect[3] + 1] += 1


def off2(lights, rect):
    lights[rect[0] : rect[2] + 1, rect[1] : rect[3] + 1] -= 1
    lights[lights < 0] = 0


def toggle2(lights, rect):
    lights[rect[0] : rect[2] + 1, rect[1] : rect[3] + 1] += 2


lights = np.zeros((1000, 1000), dtype=int)

search = r"(\d+),(\d+) through (\d+),(\d+)"
for instruction in instructions:
    rect = list(map(int, re.search(search, instruction).groups()))
    if "on" in instruction:
        on2(lights, rect)
    if "off" in instruction:
        off2(lights, rect)
    if "toggle" in instruction:
        toggle2(lights, rect)

print(lights.sum())
