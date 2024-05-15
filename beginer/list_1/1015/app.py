from math import pow, sqrt

x1, y1 = [float(x) for x in input().split(" ")]
x2, y2 = [float(x) for x in input().split(" ")]

distance = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

print(f"{distance:.4f}")
