values = input().split()
a = int(values[0])
n = int(values[len(values) - 1])
response = 0

while n <= 0:
    n = int(input())

for i in range(n):
    response += a + i

print(response)
