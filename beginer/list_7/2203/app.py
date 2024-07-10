from math import sqrt

while True:
    try:
        x1, y1, x2, y2, vi, r1, r2 = map(int, input().split())
        distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        distance += vi * 1.5
        radius = float(r1 + r2)

        print("N" if distance > radius else "Y")
    except EOFError:
        break
