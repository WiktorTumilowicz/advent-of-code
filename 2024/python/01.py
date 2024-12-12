list1 = []
list2 = []
with open("../inputs/01.txt") as file:
    for line in file:
        nums = line.split("   ")
        list1.append(int(nums[0]))
        list2.append(int(nums[1]))

list1 = sorted(list1)
list2 = sorted(list2)

# Part 1
total = 0
for num1,num2 in zip(list1,list2):
    total+=abs(num1-num2)
print(total)

# Part 2
total = 0
for num in list1:
    total += list2.count(num)*num
print(total)
