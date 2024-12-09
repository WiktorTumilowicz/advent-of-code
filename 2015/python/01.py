input = ""
with open("../inputs/1.txt") as file:
    input = "".join(file.readlines())

# Part 1

print(input.count("(") - input.count(")"))

# Part 2

total = 0
for index, char in enumerate(input):
    if char == "(":
        total += 1
    if char == ")":
        total -= 1
    if total == -1:
        print(index+1)
        break


