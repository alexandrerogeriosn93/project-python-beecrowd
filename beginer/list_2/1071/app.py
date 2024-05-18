x = int(input())
y = int(input())
sum_odds = 0

if x != 0 or y != 0:
    if x > y:
        x, y = y, x

    for i in range(x + 1, y):
        if i % 2 != 0:
            sum_odds += i

print(sum_odds)
