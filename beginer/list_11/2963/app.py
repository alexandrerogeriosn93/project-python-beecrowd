n = int(input())
first_value = int(input())

e = "S"

for _ in range(1, n):
    value = int(input())

    if value > first_value:
        e = "N"

print(e)
