n, m = map(int, input().split())

for i in range(m):
    action = input()

    n = n + 1 if action == "fechou" else n - 1

print(n)
