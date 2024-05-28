n = int(input())
h = list(map(int, input().split()))
default = 0

if n > 2:
    for i in range(2, n):
        if (h[i-2] > h[i-1] and h[i-1] < h[i]) or (h[i-2] < h[i-1] and h[i-1] > h[i]):
            default = 1
        else:
            default = 0
            break
else:
    if h[0] != h[1]:
        default = 1

print(default)
