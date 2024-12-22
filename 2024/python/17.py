import re


def ints(s):
    return [int(x) for x in re.findall("-?\d+", s)]


with open("../inputs/17.txt") as file:
    lines = [line.strip() for line in file.readlines()]
    regA = ints(lines[0])[0]
    regB = ints(lines[1])[0]
    regC = ints(lines[2])[0]
    operations = ints(lines[4])


# Part 1
def run(A, B, C):
    def combo(n):
        if n in range(4):
            return n
        if n == 4:
            return A
        if n == 5:
            return B
        if n == 6:
            return C
        raise Exception("invalid combo wombo")

    out = []
    ptr = 0
    while ptr + 1 < len(operations):
        instruciton = int(operations[ptr])
        op = int(operations[ptr + 1])
        if instruciton == 0:
            A = A >> combo(op)
        if instruciton == 1:
            B = B ^ op
        if instruciton == 2:
            B = combo(op) % 8
        if instruciton == 3:
            if A != 0:
                ptr = op
                continue
        if instruciton == 4:
            B = B ^ C
        if instruciton == 5:
            out.append(combo(op) % 8)
        if instruciton == 6:
            B = A // (2 ** combo(op))
        if instruciton == 7:
            C = A // (2 ** combo(op))
        ptr += 2
    return out


print(",".join(str(n) for n in run(regA, regB, regC)))

# Part 2
possiblities = [""]
index = 1
while index <= len(operations):
    new_pos = []
    for p in possiblities:
        for n in range(8):
            oct_A = p + str(n)
            if operations[-index:] == run(int(oct_A, 8), regB, regC):
                new_pos.append(oct_A)
    possiblities = new_pos
    index += 1
print(min(int(p, 8) for p in possiblities))
