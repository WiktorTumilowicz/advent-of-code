with open("../inputs/11.txt") as file:
    stones = [int(x) for x in file.read().strip().split()]

computes = [{} for _ in range(99)]


def compute(num, depth):
    if depth == 0:
        return 1
    depth -= 1

    if num in computes[depth]:
        return computes[depth][num]

    if num == 0:
        result = compute(1, depth)
        computes[depth][num] = result
        return result

    s = str(num)
    length = len(s)
    if length % 2 == 0:
        half_length = length >> 1
        result = compute(int(s[:half_length]), depth) + compute(
            int(s[half_length:]), depth
        )
        computes[depth][num] = result
        return result

    result = compute(num * 2024, depth)
    computes[depth][num] = result
    return result


# Part 1
print(sum(compute(stone, 25) for stone in stones))

# Part 2
print(sum(compute(stone, 75) for stone in stones))
