def calc_bottles(x, y):
    return int(x % y + x // y)

t =  int(input())

for _ in range(t):
    n, k = map(int, input().split())
    bottles = calc_bottles(n, k)
    print(bottles)
