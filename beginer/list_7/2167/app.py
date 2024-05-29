n = int(input())
values = list(map(int, input().split()))
response = 0

for i in range(0, n - 1):
    if values[i] > values[i + 1]:
        response = i + 2
        break

print(response)
