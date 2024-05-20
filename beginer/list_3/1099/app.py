n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    sum_odds = 0

    if x > y:
        x, y = y, x

    for j in range(x + 1, y):
        if j % 2 != 0:
            sum_odds += j

    print(sum_odds)
