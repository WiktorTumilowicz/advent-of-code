import re
import math

deer_info = []
with open("../inputs/14.txt") as file:
    for line in file.readlines():
        deer_info.append([int(num) for num in re.findall(r"\d+", line)])

time = 2503

# Part 1

def get_distances(deer_info, time):
    deer_distances = []
    for info in deer_info:
        laptime = info[1] + info[2]
        laps = math.floor(time / laptime)
        extra_time = time - (laps * laptime)
        extra_time = min(extra_time, info[1])
        traveling_time = extra_time + info[1] * laps
        distance = info[0] * traveling_time
        deer_distances.append(distance)
    return deer_distances

print(max(get_distances(deer_info, time)))

# Part 2

point_tally = [0 for _ in range(len(deer_info))]
for i in range(1,time+1):
    deer_distances = get_distances(deer_info, i)
    # add points to furthest deer
    point_tally[deer_distances.index(max(deer_distances))] += 1
print(max(point_tally))
