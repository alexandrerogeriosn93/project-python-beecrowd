from math import sqrt

while True:
    try:
        a, b, c = map(int, input().split())
        answer = int(sqrt((a * b / c) * 100))
        print(answer)
    except ValueError:
        break
