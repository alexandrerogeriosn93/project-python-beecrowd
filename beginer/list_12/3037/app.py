def calc_values(i):
    player = 0

    for _ in range(i):
        x, d = map(int, input().split())
        player += x * d

    return player


n = int(input())

for _ in range(n):
    j = m = 0

    j = calc_values(3)
    m = calc_values(3)

    if j > m:
        print("JOAO")
    elif m > j:
        print("MARIA")
