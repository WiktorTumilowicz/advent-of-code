from collections import defaultdict

pagegraph: dict[list[int]] = defaultdict(list)
pageorders: list[list[int]] = []

# Part 1

with open("../inputs/05.txt") as file:
    line = file.readline()
    while line != "":
        num1, num2 = line.split("|")
        pagegraph[int(num2)].append(int(num1))
        line = file.readline()
        line = line.strip()
    line = file.readline()
    while line:
        pageorders.append(list(map(int, line.strip().split(","))))
        line = file.readline()

total = 0
for line in pageorders:
    is_valid = True
    for index, page in enumerate(line):
        for after_page in line[index + 1 :]:
            if after_page in pagegraph[page]:
                is_valid = False
    if is_valid:
        total += line[int((len(line) - 1) / 2)]

print(total)

# Part 2
total = 0
for line in pageorders:
    is_valid = True
    for index, page in enumerate(line):
        for after_page in line[index + 1 :]:
            if after_page in pagegraph[page]:
                is_valid = False
    if not is_valid:
        relevant_constraints = {
            num: [n for n in line if n in pagegraph[num]] for num in line
        }
        ordered = []
        while relevant_constraints:
            k = [k for k, v in relevant_constraints.items() if v == []]
            if len(k) != 1:
                print("faiL")
                break
            k = k[0]
            ordered.append(k)
            for ln in relevant_constraints.values():
                if k in ln:
                    ln.remove(k)
            relevant_constraints.pop(k)

        total += ordered[int((len(line) - 1) / 2)]
print(total)
