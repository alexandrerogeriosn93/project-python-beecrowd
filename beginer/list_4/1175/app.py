vet = [0 for _ in range(20)]

for i in range(20):
    vet[i] = int(input())

vet = vet[::-1]

for i in range(20):
    print(f"N[{i}] = {vet[i]}")
