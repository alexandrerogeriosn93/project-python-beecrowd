x = int(input())
z = x - 1
i = 2
response = x
s = 1

while z <= x:
    z = int(input())

while response <= z:
    response += x + s

    if response <= z:
        i += 1
        s += 1

print(i)
