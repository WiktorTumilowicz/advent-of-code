with open("../inputs/09.txt") as file:
    input = file.read().strip()

# Part 1
# t = 0
# for i, c in enumerate("0099811188827773336446555566"):
#    p = i * int(c)
#    t += p
#    print(f"{i}: {p}\t\t{t}")
#
# input = "2333133121414131402"

total = 0
p1 = 0
# (p1>>1) is the index of block 1
p2 = len(input) - 1
# (p2>>1) is the index of block 2
index = 0
reg1 = int(input[p1])
reg2 = int(input[p2])


while p1 < p2:
    if p1 % 2 == 0:  # In place block
        t = total
        triangle = ((reg1 * (reg1 - 1)) >> 1) + index * reg1
        total += (p1 >> 1) * (triangle)
        index += reg1
        p1 += 1
        reg1 = int(input[p1])
    else:  # Pull block from rhs
        if reg1 == 0:
            p1 += 1
            reg1 = int(input[p1])
            continue
        if reg2 == 0:
            p2 -= 2
            reg2 = int(input[p2])
            continue
        reg1 -= 1
        reg2 -= 1
        total += index * (p2 >> 1)
        index += 1
# flush reg2 if we ended by overflowing reg1
if p1 == p2:
    triangle = ((reg2 * (reg2 - 1)) >> 1) + index * reg2
    total += (p2 >> 1) * (triangle)

print(total)

# Part 2
MAX_LEN = 9999999999


def find_next(fs, index, size):
    while index < len(fs):
        if fs[index][0] == -1:
            if fs[index][1] == size:
                return index
        index += 1
    return MAX_LEN


filesystem = []
for i, c in enumerate(input):
    block_size = int(c)
    if block_size == 0:
        continue
    if i % 2 == 0:
        filesystem.append((i >> 1, block_size))  # (position, size)
    else:
        filesystem.append((-1, block_size))  # -1 indicates free memory

free_spaces = [MAX_LEN] * 10  # We are wasting index 0
for i, block in enumerate(filesystem):
    if block[0] != -1:
        continue
    block_size = block[1]
    if free_spaces[block_size] == MAX_LEN:
        free_spaces[block_size] = i

fs_pos = len(filesystem) - 1
block_pos = filesystem[-1][0]
while block_pos > 0:
    # find next block
    while filesystem[fs_pos][0] != block_pos:
        fs_pos -= 1
    block_pos -= 1  # once the block is found this shouldn't be used at all
    move_block_size = filesystem[fs_pos][1]

    move_loc = min(free_spaces[move_block_size:])
    if move_loc > fs_pos:  # skip block if no valid locations
        continue
    move_loc_size = filesystem[move_loc][1]
    remaining_space = move_loc_size - move_block_size

    filesystem[move_loc] = (-1, remaining_space)  # reduce size of remaining_space
    filesystem.insert(move_loc, filesystem[fs_pos])
    fs_pos += 1  # increment as we have performed an insert
    filesystem[fs_pos] = (-1, move_block_size)  # replace with empty block
    move_loc += 1  # updates due to insert
    free_spaces = [x + 1 if x != MAX_LEN and x > move_loc else x for x in free_spaces]

    if free_spaces[remaining_space] > move_loc:
        free_spaces[remaining_space] = move_loc

    free_spaces[move_loc_size] = find_next(filesystem, move_loc, move_loc_size)

print(filesystem)
total = 0
counter = 0
for block in filesystem:
    if block[0] == -1:
        counter += block[1]
        continue
    size = block[1]
    triangle = ((size * (size - 1)) >> 1) + size * counter
    total += block[0] * (triangle)
    counter += size

print(total)
