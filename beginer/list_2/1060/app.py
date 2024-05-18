quantity_positives = 0

for i in range(6):
    if float(input()) > 0:
        quantity_positives += 1

print(f"{quantity_positives} valores positivos")
