from math import sqrt

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first_dist = sqrt(abs(x1) ** 2 + abs(y1) ** 2)
second_dist = sqrt(abs(x2) ** 2 + abs(y2) ** 2)

if first_dist == second_dist:
    result = int(x1), int(y1)
else:
    if first_dist > second_dist:
        result = int(x2), int(y2)
    else:
        result = int(x1), int(y1)

print(result)

