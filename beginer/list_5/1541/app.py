from math import sqrt

while True:
    try:
        a, b, c = map(int, input().split())
        print(int(sqrt(((a * b) / c) * 100)))
    except ValueError:
        break
