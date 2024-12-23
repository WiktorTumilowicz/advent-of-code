import re
from collections import defaultdict


def ints(s):
    return [int(x) for x in re.findall("-?\d+", s)]


with open("../inputs/22.txt") as file:
    nums = ints(file.read())

prune = 2**24


def next_secret(n):
    n = ((n << 6) ^ n) & (prune - 1)
    n = (n >> 5) ^ n
    n = ((n << 11) ^ n) & (prune - 1)
    return n


# Part 1
total = 0
prices = []
for n in nums:
    prices.append([n % 10])
    for _ in range(2000):
        n = next_secret(n)
        prices[-1].append(n % 10)
    total += n

print(total)

# Part 2
seq_price = defaultdict(int)
for p in prices:
    seen_seq = set()
    for i in range(4, len(p)):
        seq = (
            p[i - 3] - p[i - 4],
            p[i - 2] - p[i - 3],
            p[i - 1] - p[i - 2],
            p[i] - p[i - 1],
        )
        if seq in seen_seq:
            continue
        seen_seq.add(seq)
        seq_price[seq] += p[i]
print(max(seq_price.values()))
