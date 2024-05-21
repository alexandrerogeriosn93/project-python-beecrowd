b, S = 1, 0

for i in range(1, 40, 2):
    m = i / b
    S += m
    b *= 2

print(f"{S:.2f}")
