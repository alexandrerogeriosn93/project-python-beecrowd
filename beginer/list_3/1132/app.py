x = int(input())
y = int(input())
response = 0

if x > y:
    x, y = y, x

for i in range(x, y + 1):
    if i % 13 != 0:
        response += i

print(response)
