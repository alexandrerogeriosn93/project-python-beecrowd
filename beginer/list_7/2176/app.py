S = input()
bits = list(S)
counter = 0

for bit in bits:
    if bit == "1":
        counter += 1

S += "0" if counter % 2 == 0 else "1"

print(S)
