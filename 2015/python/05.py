with open("../inputs/05.txt") as file:
    gremlins = file.readlines()

# gremlins = [
#    "ugknbfddgicrmopn",
#    "aaa",
#    "jchzalrnumimnmhp",
#    "haegwjzuvuyypxyu",
#    "dvszwmarrgswjxmb",
# ]

# Part 1

vowels = "aeiou"
illegals = ["ab", "cd", "pq", "xy"]


def is_nice1(kobold):
    vowel_count = sum(1 for char in kobold if char in vowels)
    if vowel_count < 3:
        return False

    for illegal in illegals:
        if illegal in kobold:
            return False

    has_double = False
    for i in range(len(kobold) - 1):
        if kobold[i] == kobold[i + 1]:
            has_double = True
            break

    return has_double


print(sum(1 for gremlin in gremlins if is_nice1(gremlin.strip())))


# Part 2
def is_nice2(kobold):
    has_double_pair = False
    for i in range(len(kobold) - 3):
        pair1 = kobold[i : i + 2]
        for j in range(i + 2, len(kobold) - 1):
            pair2 = kobold[j : j + 2]
            if pair1 == pair2:
                has_double_pair = True
                break

    has_double = False
    for i in range(len(kobold) - 2):
        if kobold[i] == kobold[i + 2]:
            has_double = True
            break

    return has_double and has_double_pair


print(sum(1 for gremlin in gremlins if is_nice2(gremlin.strip())))
