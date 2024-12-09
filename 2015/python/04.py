import hashlib

with open("../inputs/04.txt") as file:
    str2hash = file.readline()
str2hash = str2hash.strip()

# Part 1

def print_hex_index(start_str):
    index = 0
    while True:
        appended = str2hash + str(index)
        result = hashlib.md5(appended.encode())
        if result.hexdigest().startswith(start_str):
            print(index)
            break
        index += 1

print_hex_index("00000")

# Part 2
print_hex_index("000000")
# wow much difficult
