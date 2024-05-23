n = int(input())
x = input().split()

for i in range(n):
    x[i] = int(x[i])

result = x.index(min(x)) + 1

print(result)
