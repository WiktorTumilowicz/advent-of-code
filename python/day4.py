import re

input = []
with open("../inputs/day4.txt") as file:
    for line in file:
        input.append(line)
#input = [
#    "MMMSXXMASM",
#    "MSAMXMSMSA",
#    "AMXSXMAAMM",
#    "MSAMASMSMX",
#    "XMASAMXAMM",
#    "XXAMMXXAMA",
#    "SMSMSASXSS",
#    "SAXAMASAAA",
#    "MAMMMXMMMM",
#    "MXMXAXMASX",
#]

search_str = "XMAS"


# Part 1

def findinlines(lines):
    total = 0
    for line in lines:
        matches = re.findall(search_str, line)
        total += len(matches)
        matches = re.findall(search_str, line[::-1])
        total += len(matches)
    return total


def transpose(lines):
    return ["".join(column) for column in zip(*lines)]


transposed = transpose(input)
primarydiagonal = transpose(
    [
        "_" * index + line + "_" * (len(line) - index - 1)
        for index, line in enumerate(input)
    ]
)
secondarydiagonal = transpose(
    [
        "_" * (len(line) - index - 1) + line + "_" * index
        for index, line in enumerate(input)
    ]
)

print(
    findinlines(input)
    + findinlines(transposed)
    + findinlines(primarydiagonal)
    + findinlines(secondarydiagonal)
)

# Part 2

total = 0
for i in range(1, len(input) - 1):
    for j in range(1, len(input[0]) - 1):
        if input[i][j] == "A":
            cross = (
                input[i - 1][j - 1]
                + input[i - 1][j + 1]
                + input[i + 1][j - 1]
                + input[i + 1][j + 1]
            )
            mcount = cross.count("M")
            scount = cross.count("S")
            if mcount == 2 and scount == 2 and cross[0] != cross[3]:
                total += 1

print(total)
