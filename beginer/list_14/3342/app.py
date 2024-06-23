n = int(input())
total = n * n

if n % 2 == 0:
    a = total // 2
    b = a
else:
    a = (total + 1) // 2
    b = a - 1

print(f"{a} casas brancas e {b} casas pretas")
