lines = int(input())
columns = int(input())
color = bin(lines + columns - 1)

print(color[-1])
