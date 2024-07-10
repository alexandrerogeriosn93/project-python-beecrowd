from sys import stdin

n = int(stdin.readline())
sheeps = list(map(int, stdin.readline().split()))
stars = [0 for _ in range(n)]
total_sheeps = total_stars = i = 0

while True:
    if i == 0 and sheeps[i] % 2 == 0:
        stars[i] = 1

        if sheeps[i] > 0:
            sheeps[i] -= 1
        break
    elif i == n - 1 and sheeps[i] % 2 == 1:
        stars[i] = 1

        if sheeps[i] > 0:
            sheeps[i] -= 1
        break
    elif sheeps[i] % 2 == 1:
        if sheeps[i] > 0:
            sheeps[i] -= 1
        stars[i] = 1
        i += 1
    elif sheeps[i] % 2 == 0:
        stars[i] = 1
        if sheeps[i] > 0:
            sheeps[i] -= 1
        i -= 1

total_stars = sum(stars)
total_sheeps = sum(sheeps)

print(total_stars, total_sheeps)
