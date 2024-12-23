from collections import defaultdict

C = defaultdict(set)
with open("../inputs/23.txt") as file:
    for line in file.read().strip().split("\n"):
        A, B = line.split("-")
        C[A].add(B)
        C[B].add(A)

# Part 1
codes = sorted(C.keys())

total = 0
for i, a in enumerate(codes):
    for j in range(i + 1, len(codes)):
        for k in range(j + 1, len(codes)):
            b = codes[j]
            c = codes[k]
            if a in C[b] and b in C[c] and c in C[a]:
                if a[0] == "t" or b[0] == "t" or c[0] == "t":
                    total += 1
print(total)


# Part 2
def max_cluster(nodes):
    if len(nodes) == 0:
        return set()
    nodes_cp = nodes.copy()
    node = nodes_cp.pop()
    excluding = max_cluster(nodes_cp)
    including = max_cluster(C[node] & nodes_cp) | {node}
    return including if len(including) > len(excluding) else excluding


print(",".join(c for c in sorted(max_cluster(set(codes)))))
