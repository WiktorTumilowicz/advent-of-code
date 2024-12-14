import re
from sympy import gcd


def ints(s):
    return [int(x) for x in re.findall("\d+", s)]


with open("../inputs/13.txt") as file:
    lines = file.read()
    machines = lines.split("\n\n")
    problems = [ints(m) for m in machines]


def minimize(a, c, b, d, tx, ty):
    # Compute coefficients for the reduced equation
    k = c * b - d * a
    t = b * ty - d * tx

    g = gcd(k, t)
    if g != abs(k):  # Check if solution exists
        return 0, 0  # No solution

    x = t // k
    y = (tx - a * x) // b
    return x, y


# Part 1
total = 0
for problem in problems:
    [Ax, Ay, Bx, By, Tx, Ty] = problem
    if (Ax + Ay) * 3 > Bx + By:  # determine which is lower total cost, A*3 or B*1
        x, y = minimize(Ax, Ay, Bx, By, Tx, Ty)
    else:
        y, x = minimize(Bx, By, Ax, Ay, Tx, Ty)
    total += x * 3 + y

print(total)

# Part 2
total = 0
xtra = 10000000000000
for problem in problems:
    [Ax, Ay, Bx, By, Tx, Ty] = problem
    if (Ax + Ay) * 3 > Bx + By:  # determine which is lower total cost, A*3 or B*1
        a, b = minimize(Ax, Ay, Bx, By, Tx + xtra, Ty + xtra)
    else:
        b, a = minimize(Bx, By, Ax, Ay, Tx + xtra, Ty + xtra)

    # gdc is faulty for very large numbers so we verify the solution
    if a * Ax + b * Bx == Tx + xtra:
        total += a * 3 + b

print(total)
