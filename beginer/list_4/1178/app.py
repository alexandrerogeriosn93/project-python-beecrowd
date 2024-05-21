n = float(input())
vet = [0 for _ in range(100)]

for i in range(100):
    vet[i] = n
    n /= 2

for i in range(100):
    print(f"N[{i}] = {(vet[i]):.4f}")
