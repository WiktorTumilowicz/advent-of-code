reports = []
with open("../inputs/02.txt") as file:
    for line in file:
        reports.append([int(num) for num in line.split(" ")])
# Part 1

total = 0
for report in reports:
    flag = False
    for a, b in zip(report, report[1:]):
        if abs(a - b) not in [1, 2, 3]:
            flag = True
    if flag:
        continue
    if sorted(report) == report:
        total += 1
    if sorted(report, reverse=True) == report:
        total += 1
print(total)

#reports = [
#    [7, 6, 4, 2, 1],
#    [1, 2, 7, 8, 9],
#    [9, 7, 6, 2, 1],
#    [1, 3, 2, 4, 5],
#    [8, 6, 4, 4, 1],
#    [1, 3, 6, 7, 9],
#]
# Part 2
total = 0


def check_close(num1, num2):
    if num1 < num2 and num1 + 3 >= num2:
        return True
    return False


def check_report(report: list):
    allowError = True
    pos = 1
    while pos < len(report):
        # print(f"{report[pos-1]}  {report[pos]}")
        if not check_close(report[pos - 1], report[pos]):
            if allowError:
                if pos == len(report) - 1 or check_close(
                    report[pos - 1], report[pos + 1]
                ):
                    pos += 1
                    allowError = False
                elif pos == 1 or check_close(report[pos - 2], report[pos]):
                    allowError = False
                else:
                    return False
            else:
                return False
        pos += 1
    print(report)
    return True


for report in reports:
    if check_report(report):
        total += 1
    else:
        report.reverse()
        if check_report(report):
            total += 1

print(total)
