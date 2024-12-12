import re

input = ""
with open("../inputs/03.txt") as file:
    for line in file:
        input += line
search_str = r"mul\((\d{1,3}),(\d{1,3})\)"

# Part 1
matches = re.findall(search_str, input)
total = 0
for match in matches:
    total += int(match[0]) * int(match[1])

print(total)

# Part 2

doing = True
index = 0
total = 0
match = re.search(search_str, input[index:])
while match:
    domatch = re.findall("do\(\)", input[index : index + match.start()])
    dontmatch = re.findall("don't\(\)", input[index : index + match.start()])
    if domatch and dontmatch:
        doing = domatch[-1].end() > dontmatch[-1].end()
    elif dontmatch:
        doing = False
    elif domatch:
        doing = True

    if doing:
        total += int(match[1]) * int(match[2])

    index += match.end()
    match = re.search(search_str, input[index:])

print(total)
